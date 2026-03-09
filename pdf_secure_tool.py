                'fill_forms': args.allow_fill_forms,
                'extract': args.allow_extract,
                'assemble': args.allow_assemble
            }
            
            success = tool.encrypt_pdf(
                args.input, args.output, args.password,
                owner_password=args.owner_password,
                permissions=permissions
            )
            
        elif args.command == 'both':
            watermark_opts = {
                'opacity': args.watermark_opacity,
                'angle': args.watermark_angle,
                'color': args.watermark_color
            }
            
            encrypt_opts = {
                'owner_password': None  # 使用与用户密码相同的所有者密码
            }
            
            success = tool.watermark_and_encrypt(
                args.input, args.output,
                args.watermark_text, args.password,
                watermark_opts, encrypt_opts
            )
            
        elif args.command == 'batch':
            if args.operation in ['watermark', 'both'] and not args.text:
                print("❌ watermark/both操作需要 --text 参数")
                sys.exit(1)
            if args.operation in ['encrypt', 'both'] and not args.password:
                print("❌ encrypt/both操作需要 --password 参数")
                sys.exit(1)
            
            batch_kwargs = {}
            if args.operation in ['watermark', 'both']:
                batch_kwargs['watermark_text'] = args.text
                batch_kwargs['opacity'] = args.opacity
                batch_kwargs['angle'] = args.angle
            if args.operation in ['encrypt', 'both']:
                batch_kwargs['password'] = args.password
            
            results = tool.batch_process(
                args.input_dir, args.output_dir,
                args.operation, **batch_kwargs
            )
            
            success = results['success'] > 0
            
        else:
            print(f"❌ 未知命令: {args.command}")
            sys.exit(1)
        
        if success:
            print("\n" + "=" * 60)
            print("✅ 操作成功完成!")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("❌ 操作失败!")
            print("=" * 60)
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n操作被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()