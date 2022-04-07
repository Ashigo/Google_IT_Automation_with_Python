#!/usr/bin/env python3
import re

name = input("Enter name, devided by ',': ")

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

result_name = rearrange_name(name)
print(result_name)