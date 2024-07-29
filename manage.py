#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    pyversion = sys.version_info
    if pyversion.major==3 and pyversion.minor==12 and pyversion.micro==3:
        print(f'Recommended Python version 3.12.3 detected.')
    else:
        print(f'WARNING: Expected Python version 3.12.3, but version {pyversion.major}.{pyversion.minor}.{pyversion.micro} detected. \n',
              'This may cause unexpected functionality or program failure.')
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'verademo-python.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
