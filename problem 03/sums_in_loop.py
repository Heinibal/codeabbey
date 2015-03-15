#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    error = True
    try:
        inputfile = sys.argv[1]
        f = open(inputfile, 'r')
        error = False
    except:
        print("Filename of Inputfile is needed as command line argument.")
    if not error:
        number_of_sums = int(f.readline())
        for i in range(number_of_sums):
            line = f.readline()
            numbers = line.split()
            print(int(numbers[0]) + int(numbers[1]))

if __name__ == '__main__':
    main()