#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "breaze.settings")
    try:
        from django.core.management import execute_from_command_line

	# Allow API to be accessed externally
        args = sys.argv[:]  # Grab a copy of argv
        if len(args) == 2 and sys.argv[1] == 'runserver':
            # Default to serving externally if not told otherwise
            args = sys.argv + ['0.0.0.0:8000']
        # Continue as normal
        execute_from_command_line(args)

    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
