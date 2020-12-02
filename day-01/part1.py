# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Find two numbers in a given file that sum another number, print their product
"""
import sys
sum = int(sys.argv[2])
data = set()
with open(sys.argv[1], "r") as file:
    for line in file:
        n1 = int(line.strip())
        data.add(n1)
        n2 = sum - n1
        if n2 in data:
            print(n1*n2)
            exit(0)
