#! /bin/awk -f
# SPDX-FileCopyrightText: 2023 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

{
    line_concat = ""

    for (i = 1; i <= length($0); i++) {
        if (substr($0, i, 1) ~ /[0-9]/) {
            if (line_concat == "") {
                line_concat = substr($0, i, 1)
            }
            last_digit = substr($0, i, 1)
        }
    }

    line_concat = line_concat last_digit

    sum+=line_concat
}

END { print sum }
