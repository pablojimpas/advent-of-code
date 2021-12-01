# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

with open(sys.argv[1], "r") as file:
    # Load program instructions
    program = list()
    for instruction in file:
        (operation, argument) = instruction.strip().split(" ")
        argument = int(argument)
        program.append((operation, argument))

    # Execute the program
    seen = set()
    pc = 0 # Program counter
    acc = 0 # Accumulator
    while pc not in seen:
        seen.add(pc)
        (operation, argument) = program[pc]
        if operation == "nop":
            pc = pc + 1
        elif operation == "acc":
            acc = acc + argument
            pc = pc + 1
        elif operation == "jmp":
            pc = pc + argument
    print("Infinite loop, last acc: ", acc)
