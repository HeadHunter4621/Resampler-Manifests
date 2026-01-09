from typing import Any

import yaml

banned_flags_list = ['a','b','B','c','C','D','E','F','g','G','h','H','L','N','P','t','W','x','Y']

# Example YAML entry:
#   gen:
#     name: Gender Factor
#     abbr: gen
#     type: Numerical
#     min: -100
#     max: 100
#     default_value: 0
#     is_flag: true
#     flag: g

# example flag entry:
# ["gen", "Gender Factor", 'Numerical', -100, 100, 0, True, "g"]
# [Abbreviation, Name, Type, Min, Max, Default, is_flag?, flag]

flags = [
    [],
    []
]

resampler_name = 'TIPS'







