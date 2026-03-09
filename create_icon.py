#!/usr/bin/env python3
"""
创建简单的图标文件（如果没有现成的图标）
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """创建一个简单的PDF图标"""
    # 创建一个256x256的图像
    img = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制PDF文档形状
    # 主体
    draw.rectangle([50, 50, 206, 206], fill=(220, 50, 50), outline=(180, 30, 30), width=3)
    
    # 折角
    draw.polygon([206, 50, 206, 100, 156, 50], fill=(200, 40, 40), outline=(180, 30, 30), width=3)
    
    # 文字 "PDF"
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        # 回退到默认字体
        font = ImageFont.load_default()
    
    draw.text((80, 90), "PDF", fill=(255, 255, 255), font=font)
    
    # 保存为ICO格式
    img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    
    print("✅ 图标文件已创建: icon.ico")

if __name__ == "__main__":
    create_icon()