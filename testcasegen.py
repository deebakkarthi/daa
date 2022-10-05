#!/usr/bin/env python3
import sys
import random
from math import floor


def usage():
    print("Usage: testcasegen NUM [FILE]")


if len(sys.argv) < 2:
    usage()
    sys.exit(0)


if len(sys.argv) > 2:
    sys.stdout = open(sys.argv[2], 'w')

for i in range(int(sys.argv[1])):
    print(random.random(), end=" ")
print()
