# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

def convert_to_dec(text):
    dec = 0
    for c in text:
        dec = dec * 2 + 1
        if c == 'F' or c == 'L':
            dec = dec - 1
    return dec


def seat_id(line):
    row = convert_to_dec(line[:7])
    column = convert_to_dec(line[7:10])
    return row * 8 + column


with open(sys.argv[1], "r") as file:
    max = 0
    for line in file:
        current = seat_id(line)
        if current > max:
            max = current
    print(max)
