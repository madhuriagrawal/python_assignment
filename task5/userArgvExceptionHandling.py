import sys

try:
    f = open(sys.argv[1], "r")
except Exception:
    print("File doesn't exist, give another file name")


