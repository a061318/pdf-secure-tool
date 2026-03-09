                path = Path(filename)
                output_path = path.parent / f"{path.stem}_encrypted.pdf"
                self.encrypt_output.set(str(output_path))
    
    def browse_encrypt_output(self):
        """浏览加密输出文件"""
        filename = filedialog.asksaveasfilename(
            title="保存PDF文件",
            defaultextension=".pdf",
            filetypes=[("PDF文件", "*.pdf"), ("所有文件", "*.*")]
        )
        if filename:
            self.encrypt_output.set(filename)
    
    def browse_batch_input(self):
        """浏览批量输入目录"""
        directory = filedialog.askdirectory(title="选择输入目录")
        if directory:
            self.batch_input.set(directory)
    
    def browse_batch_output(self):
        """浏览批量输出目录"""
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            self.batch_output.set(directory)
    
    def preview_watermark(self):
        """预览水印效果"""
        messagebox.showinfo("预览", "水印预览功能将在后续版本中添加")
    
    def log_message(self, message):
        """添加日志消息"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update()
    
    def add_watermark_to_pdf(self, input_file, output_file, text, opacity, angle, fontsize, color):
        """添加水印到PDF"""
        try:
            # 颜色映射
            color_map = {
                "gray": (0.7, 0.7, 0.7),
                "lightgray": (0.9, 0.9, 0.9),
                "red": (0.8, 0.2, 0.2),
                "blue": (0.2, 0.2, 0.8),
                "black": (0.1, 0.1, 0.1)
            }
            rgb_color = color_map.get(color, (0.7, 0.7, 0.7))
            
            # 创建临时水印PDF
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                watermark_pdf = tmp.name
            
            # 生成水印
            c = canvas.Canvas(watermark_pdf, pagesize=A4)
            width, height = A4
            
            c.setFillAlpha(opacity)
            c.setFillColorRGB(*rgb_color)
            c.setFont("Helvetica", fontsize)
            
            spacing = 150
            for y in range(-int(height), int(height * 2), spacing):
                for x in range(-int(width), int(width * 2), spacing):
                    c.saveState()
                    c.translate(x, y)
                    c.rotate(angle)
                    c.drawString(0, 0, text)
                    c.restoreState()
            
            c.save()
            
            # 合并水印
            pdf_reader = PdfReader(input_file)
            watermark_reader = PdfReader(watermark_pdf)
            watermark_page = watermark_reader.pages[0]
            
            pdf_writer = PdfWriter()
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page.merge_page(watermark_page)
                pdf_writer.add_page(page)
            
            # 保存
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
            
            # 清理
            os.unlink(watermark_pdf)
            
            return True, "水印添加成功"
            
        except Exception as e:
            return False, f"添加水印失败: {str(e)}"
    
    def encrypt_pdf_file(self, input_file, output_file, user_pass, owner_pass, permissions):
        """加密PDF文件"""
        try:
            pdf_reader = PdfReader(input_file)
            pdf_writer = PdfWriter()
            
            # 复制页面
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            # 复制元数据
            if pdf_reader.metadata:
                pdf_writer.add_metadata(pdf_reader.metadata)
            
            # 设置加密
            pdf_writer.encrypt(
                user_password=user_pass,
                owner_password=owner_pass or user_pass,
                permissions_flag=permissions
            )
            
            # 保存
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
            
            return True, "PDF加密成功"
            
        except Exception as e:
            return False, f"PDF加密失败: {str(e)}"
    
    def execute_watermark(self):
        """执行水印添加"""
        if self.processing:
            return
        
        # 验证输入
        input_file = self.watermark_input.get()
        output_file = self.watermark_output.get()
        text = self.watermark_text.get()
        
        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("错误", "请选择有效的输入文件")
            return
        
        if not output_file:
            messagebox.showerror("错误", "请指定输出文件")
            return
        
        if not text:
            messagebox.showerror("错误", "请输入水印文本")
            return
        
        # 开始处理
        self.processing = True
        self.status_var.set("正在添加水印...")
        
        def process():
            success, message = self.add_watermark_to_pdf(
                input_file, output_file, text,
                self.watermark_opacity.get(),
                self.watermark_angle.get(),
                self.watermark_fontsize.get(),
                self.watermark_color.get()
            )
            
            self.root.after(0, lambda: self.process_complete(success, message))
        
        thread = threading.Thread(target=process)
        thread.daemon = True
        thread.start()
    
    def execute_encrypt(self):
        """执行加密"""
        if self.processing:
            return
        
        # 验证输入
        input_file = self.encrypt_input.get()
        output_file = self.encrypt_output.get()
        user_pass = self.user_password.get()
        confirm_pass = self.confirm_password.get()
        
        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("错误", "请选择有效的输入文件")
            return
        
        if not output_file:
            messagebox.showerror("错误", "请指定输出文件")
            return
        
        if not user_pass:
            messagebox.showerror("错误", "请输入用户密码")
            return
        
        if user_pass != confirm_pass:
            messagebox.showerror("错误", "两次输入的密码不一致")
            return
        
        # 构建权限
        permissions = {
            'print': self.allow_print.get(),
            'modify': self.allow_modify.get(),
            'copy': self.allow_copy.get(),
            'annotate': self.allow_annotate.get(),
            'fill_forms': False,
            'extract': False,
            'assemble': False
        }
        
        # 开始处理
        self.processing = True
        self.status_var.set("正在加密PDF...")
        
        def process():
            success, message = self.encrypt_pdf_file(
                input_file, output_file,
                user_pass, self.owner_password.get(),
                permissions
            )
            
            self.root.after(0, lambda: self.process_complete(success, message))
        
        thread = threading.Thread(target=process)
        thread.daemon = True
        thread.start()
    
    def execute_batch(self):
        """执行批量处理"""
        if self.processing:
            return
        
        # 验证输入
        input_dir = self.batch_input.get()
        output_dir = self.batch_output.get()
        operation = self.batch_operation.get()
        
        if not input_dir or not os.path.exists(input_dir):
            messagebox.showerror("错误", "请选择有效的输入目录")
            return
        
        if not output_dir:
            messagebox.showerror("错误", "请指定输出目录")
            return
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 验证参数
        if operation in ['watermark', 'both'] and not self.batch_watermark.get():
            messagebox.showerror("错误", "请输入水印文本")
            return
        
        if operation in ['encrypt', 'both'] and not self.batch_password.get():
            messagebox.showerror("错误", "请输入密码")
            return
        
        # 开始处理
        self.processing = True
        self.status_var.set("正在批量处理...")
        self.log_text.delete('1.0', tk.END)
        
        def process():
            try:
                # 查找PDF文件
                pdf_files = list(Path(input_dir).glob("*.pdf"))
                total = len(pdf_files)
                
                if total == 0:
                    self.root.after(0, lambda: self.process_complete(False, "未找到PDF文件"))
                    return
                
                self.log_message(f"找到 {total} 个PDF文件")
                
                success_count = 0
                
                for i, pdf_file in enumerate(pdf_files, 1):
                    output_file = Path(output_dir) / f"{pdf_file.stem}_processed.pdf"
                    
                    self.log_message(f"处理 {i}/{total}: {pdf_file.name}")
                    
                    if operation == 'watermark':
                        success, msg = self.add_watermark_to_pdf(
                            str(pdf_file), str(output_file),
                            self.batch_watermark.get(),
                            0.3, 45, 40, "gray"
                        )
                    elif operation == 'encrypt':
                        success, msg = self.encrypt_pdf_file(
                            str(pdf_file), str(output_file),
                            self.batch_password.get(), None,
                            {'print': True, 'modify': False, 'copy': False, 'annotate': False}
                        )
                    else:  # both
                        # 先添加水印到临时文件
                        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                            temp_file = tmp.name
                        
                        success1, msg1 = self.add_watermark_to_pdf(
                            str(pdf_file), temp_file,
                            self.batch_watermark.get(),
                            0.3, 45, 40, "gray"
                        )
                        
                        if success1:
                            success2, msg2 = self.encrypt_pdf_file(
                                temp_file, str(output_file),
                                self.batch_password.get(), None,
                                {'print': True, 'modify': False, 'copy': False, 'annotate': False}
                            )
                            success = success2
                            msg = msg2 if success2 else msg1
                            os.unlink(temp_file)
                        else:
                            success = False
                            msg = msg1
                    
                    if success:
                        success_count += 1
                        self.log_message(f"  ✅ 成功: {output_file.name}")
                    else:
                        self.log_message(f"  ❌ 失败: {msg}")
                
                message = f"批量处理完成: {success_count}/{total} 成功"
                self.root.after(0, lambda: self.process_complete(success_count > 0, message))
                
            except Exception as e:
                self.root.after(0, lambda: self.process_complete(False, f"批量处理失败: {str(e)}"))
        
        thread = threading.Thread(target=process)
        thread.daemon = True
        thread.start()
    
    def process_complete(self, success, message):
        """处理完成回调"""
        self.processing = False
        
        if success:
            self.status_var.set("操作成功")
            messagebox.showinfo("成功", message)
        else:
            self.status_var.set("操作失败")
            messagebox.showerror("错误", message)

def main():
    """主函数"""
    if not HAS_LIBS:
        messagebox.showerror("错误", "缺少必要的库: PyPDF2 和 reportlab\n请安装: pip install PyPDF2 reportlab")
        return
    
    root = tk.Tk()
    
    # 设置样式
    style = ttk.Style()
    style.theme_use('clam')
    
    # 创建主窗口
    app = PDFSecureGUI(root)
    
    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    main()