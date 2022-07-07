#!/usr/bin/python3

def number_keys(a_dictionary):
    key_holder = []
    for keys in a_dictionary:
        key_holder.append(keys)

    return "Number of keys: {:d}".format(len(key_holder))
