#! /usr/bin/python3
"""
This program will check for palindromes and return the amount found
"""
import sys
find_pali = "wordlist.txt"
def load(file):
    try:
        with open(file) as pal_file:
            word_list = pal_file.read().strip().split('\n')
            word_list = [x.lower() for x in word_list]
            palindromes = []
            for x in word_list:
                if len(x) > 1 and x[::-1] == x:
                    palindromes.append(x)
            print("Number of palindromes found = {}".format(len(palindromes)))
            # the splat operator " * " is used to expand inputs into positional arguments
            print(*palindromes, sep=" <---PALINDROME---> ")
    except IOError as e:
        print("{}\nError uploading file {}".format(e,file),file=sys.stderr)
        # the '1' indicates an error and did not close succesfully
        sys.exit(1)

load(find_pali)
