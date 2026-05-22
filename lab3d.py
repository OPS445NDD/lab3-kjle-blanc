#!/usr/bin/env python3

# Author ID: [kjle-blanc]

import subprocess

def free_space():
    # Run the command: df -h | grep '/$' | awk '{print $4}'
    result = subprocess.check_output(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True
    )
    return result.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
