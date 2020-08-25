#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Timothy K Reynoso"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    # Your code here
    with open(filename) as file:
        data = file.read()
        data_case_sensitive = data.lower()
        #print(data.count('the'))
        word_list = list(filter(None, data_case_sensitive.split(' ')))
        new_dic = {}
        for word in word_list:
            if word not in new_dic.keys():
                new_dic[word] = 1
            else:
                new_dic[word] += 1
            #new_dic.update({word : word_list.count(word)})
    return new_dic


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    ##
    #d = list(create_word_dict(filename))
    word_dict = create_word_dict(filename)
    dual_words = [n for n in word_dict.items()]
    #print([f"{word}" for word in d])
    # Your code here
       # print(new_dic.sort())
    highest_word_count = sorted(word_dict.values())[-1]
    #for i in range(highest_word_count):
    new_list = []
    [new_list.append(k) for k in word_dict.items()]
    #[print(k[1]) for k in l.items() if l.get(k) > 100]
    #[print() for ]
    #[print(k[1]) for k in l.items()]
    [print(f"{key} : {value}") for key, value in dict(sorted(new_list)).items()]
    return 


def print_top(filename):
    """Prints the top count listing for the given file."""
    raw_word_dict = create_word_dict(filename)
    #highest_word_count = sorted(raw_word_dict.values())[-1]
    def myFunc(e):
        return e[1]
    elem = list(raw_word_dict.items())
    elem.sort(key=myFunc)
    [print(elem[-i - 1]) for i in range(20)]
        
    #def myFunc(e):
        #new_dicts = dict(key=e[0], value=e[1])
        #new_list.append(new_dicts)
        #print(new_dicts)
        ##[print(dict.fromkeys(k,v)) for k, v in dict(e).items()]
        #return e
    
    #new_dict = list(raw_word_dict.items())
    #[new_dict.sort(key=myFunc)]
    #print(highest_word_count)
    #print(new_list)
    #for item in new_dict:
        #print(item)
    #[print(key) for key in list(raw_word_dict.items())]
    #[print( i, k) for i, k in enumerate(sorted())]

    return 


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
