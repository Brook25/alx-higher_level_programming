#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    add = 0
    stg = roman_string
    for i in range(len(stg)):
        for key in rom_dict:
            if stg[i] == key:
                add += rom_dict[key]
                if i < len(stg) - 1 and rom_dict[stg[i]] < rom_dict[stg[i + 1]]:
                    add -= 2 * rom_dict[stg[i]]
    return add
