# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

function count(b) {
	if (length(bags[b]) == 0) {
		return length(counters)
	}

	for (i in bags[b]) {
		counters[i] = 1
		count(i)
	}
	return length(counters)
}
{
	outerBag = $1" "$2
	for (i = 6; i < NF; i += 4) {
		innerBag = $i" "$(i + 1)
		bags[innerBag][outerBag] = 1
	}
}
END {
	print count("shiny gold")
}
