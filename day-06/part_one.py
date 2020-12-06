# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

with open(sys.argv[1], "r") as file:
    letters_seen = set()
    counts = list()
    for line in file:
        if not line.strip():
            counts.append(len(letters_seen))
            letters_seen = set()
        for c in line.strip():
            if c not in letters_seen:
                letters_seen.add(c)
    counts.append(len(letters_seen))
    print(sum(counts))

