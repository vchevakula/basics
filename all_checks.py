#!/usr/bin/env python3
import os
import sys
import shutil


def check_reboot():
    """ Returns True if the computer has a pending reboot"""
    return os.path.exists('/var/run/reboot-required')

def disk_usage():
    path = "/home/vchevakula/"
    stat = shutil.disk_usage(path)
    gb = 10 ** 9
    print('Total Space: {:6.2f} GB'.format(stat[0] /gb))
    print('Total Used Space: {:6.2f} GB'.format(stat[1] /gb))
    print('Total Free Space: {:6.2f} GB'.format(stat[2] /gb))

def main():
    """ Main function """
    disk_usage()
    if check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()


