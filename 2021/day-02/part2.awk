#! /bin/awk -f
# SPDX-FileCopyrightText: 2021 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later
/forward/ {
	horizontal += $2
	depth += aim * $2
}
/down/ {
	aim += $2
}
/up/ {
	aim -= $2
}
END {
	print horizontal * depth
}
