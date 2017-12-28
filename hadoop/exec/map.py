#!/usr/local/bin/python3

# Do Mapping

import sys
import os

def dwheeler_dangerous_functions(input_str):
    bad_str_list = {
        "strcpy": "strncpy",
        "strcat": "strncat",
        "sprintf": "snprintf",
        "vsprintf": "snprintf",
        "gets": "fgets"
    }

    for key, val in bad_str_list.items():
        if key in input_str:
            return str(key) + "() is dangerous; use " + val + "() instead."

    forbidden_list = {
        "strlen": "strlen() should be avoided unless you can guarantee a terminating NULL character.",
        "scanf": "scanf() (and variants) should be avoided unless you control maximum length.",
        "realpath": "realpath() is dangerous.",
        "getopt": "getopt() is dangerous.",
        "getpass": "getpass() is dangerous.",
        "streadd": "streadd() is dangerous.",
        "strecpy": "strecpy() is dangerous.",
        "strtrns": "strtrns() is dangerous.",
        "getwd": "getwd() is dangerous unless you can guarantee the input buffer is at least PATH_MAX bytes in length.",
        "FD_SET": "select() helper macros do not check that the index fd is within bounds; make sure that fd >= 0 and fd <= FD_SETSIZE",
        "FD_CLR": "select() helper macros do not check that the index fd is within bounds; make sure that fd >= 0 and fd <= FD_SETSIZE",
        "FD_ISSET": "select() helper macros do not check that the index fd is within bounds; make sure that fd >= 0 and fd <= FD_SETSIZE"
    }

    for key, val in forbidden_list.items():
        if key in input_str:
            return str(val)

    # Okay
    return None

def check_line(input_str):
    dwheeler_resp = dwheeler_dangerous_functions(input_str)
    if dwheeler_resp is not None:
        return dwheeler_resp + "   Credit: https://www.dwheeler.com/secure-programs/Secure-Programs-HOWTO/dangers-c.html"

    return None

# MAIN

file_name = os.getenv('map_input_file')
line_num = 0

for line in sys.stdin:
    result = check_line(line.strip())
    if result is not None:
        print(str(file_name) + "\t" + result + " @ line: " + str(line_num))

    line_num += 1
