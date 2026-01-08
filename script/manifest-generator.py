from typing import Any

import yaml

banned_flags_list = ['a','b','B','c','C','D','E','F','g','G','h','H','L','N','P','t','W','x','Y']

#   gen:
#     name: Gender Factor
#     abbr: gen
#     type: Numerical
#     min: -100
#     max: 100
#     default_value: 0
#     is_flag: true
#     flag: g

def add_entry():
    yaml.YAMLObject

def make_flag():
    flag_abbreviation = input("What is the abbreviation of the flag?")
    flag_name = input("What is the full name of the flag?")
    type_number = input("What type of flag is it? 1=Bool, 2=option, 3=Numerical, 4=Curve")
    if type_number == 1:
        print("Selected: Boolean")

    elif type_number == 2:
        print("Selected: Option")
    elif type_number == 3:
        print("Selected: Numerical")
    elif type_number == 4:
        print("Selected: Curve")
    else:
        print("invalid type; starting over </3")
        make_flag()

def __init__():
    exe_name = input("Please input the name of the resampler (without file extension)")

