# =========================================================
#   jeszcze nie wiem jak to dziala
#
# =========================================================

import re, os, sys


def main(argv):
    if len(argv) > 2:
        print("Error. To many parameters. Allowed maximum four.")
        exit(1)
    else:
        print("Number of parameters Ok")
        if len(argv) > 0:
            if argv[0] == "-p":
                print("parameter -p")
            if argv[0] == "-c":
                print("parameter -c")
            if (argv[0] == '-i'):
                print("parameter -i")
            else:
                print("Bad parameter")
        else:
            print('fail - no parameters')


if __name__ == "__main__":
    main(sys.argv[1:])