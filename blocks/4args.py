# =========================================================
#   jeszcze nie wiem jak to dziala
#
# =========================================================

import re, os, sys


def main(argv):
    if len(argv) > 2:
        print "Error. To many parameters. Allowed maximum four."
        exit(1)
    else:
        print "Number of parameters Ok"
        if len(argv) > 0:
            if argv[0] == "-p":
                analize(alarmfile, argv[1])
            if argv[0] == "-c":
                config_fail(alarmfile, argv[1])
            if (argv[0] == '-i'):
                ftp_srv_IP = argv[1]
                analize(alarmfile)
            else:
                print "Bad parameter"
        else:
            print 'dupa'


if __name__ == "__main__":
    main(sys.argv[1:])