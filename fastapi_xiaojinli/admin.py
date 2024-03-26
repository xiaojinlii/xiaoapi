import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('FASTAPI_SETTINGS_MODULE', 'fastapi_xiaojinli.conf.global_settings')
    try:
        from fastapi_xiaojinli.management import admin_commands
    except ImportError as exc:
        raise ImportError(
            "Couldn't import fastapi_xiaojinli. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    admin_commands()


if __name__ == '__main__':
    main()
