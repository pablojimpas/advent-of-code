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

    for (i, (operation, argument)) in enumerate(program):
        if operation not in ("nop", "jmp"):
            continue

        mod_prog = program.copy()
        mod_opt = "jmp" if operation == "nop" else "nop"
        mod_prog[i] = (mod_opt, argument)

        # Execute the program
        seen = set()
        pc = 0 # Program counter
        acc = 0 # Accumulator
        while True:
            if pc in seen:
                break
            if pc >= len(program):
                print("End, acc: ", acc)
                exit()
            seen.add(pc)
            (operation, argument) = mod_prog[pc]
            if operation == "nop":
                pc = pc + 1
            elif operation == "acc":
                acc += argument
                pc = pc + 1
            elif operation == "jmp":
                pc = pc + argument
