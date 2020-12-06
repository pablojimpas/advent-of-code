# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

with open(sys.argv[1], "r") as file:
    letters_seen = dict()
    counts = list()
    n_members_group = 0
    for line in file:
        if not line.strip():
            cont = 0
            for l in letters_seen:
                if letters_seen[l] == n_members_group:
                    cont = cont + 1
            counts.append(cont)
            letters_seen = dict()
            n_members_group = 0
            continue
        n_members_group = n_members_group + 1
        for c in line.strip():
            if c in letters_seen:
                letters_seen[c] = letters_seen[c] + 1
            else:
                letters_seen[c] = 1
    cont = 0
    for l in letters_seen:
        if letters_seen[l] == n_members_group:
            cont = cont + 1
    counts.append(cont)
    print(sum(counts))

