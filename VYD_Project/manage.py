#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'VYD_Project.settings'
from kmls_management.views import write_ip

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VYD_Project.settings")

    from django.core.management import execute_from_command_line

    ip = sys.argv.pop(1)
    print ip
    write_ip(ip)


    execute_from_command_line(sys.argv)
