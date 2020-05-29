from app import create_app, create_parser



if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    app = create_app(config_obj=args.config)

    app.run(

        host=args.host,
        port=args.port,
        debug=args.debug,
    )
