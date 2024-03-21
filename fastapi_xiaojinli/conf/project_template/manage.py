import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('FASTAPI_SETTINGS_MODULE', 'application.settings')
    try:
        from fastapi_xiaojinli.management import shell
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    shell()


if __name__ == '__main__':
    main()
