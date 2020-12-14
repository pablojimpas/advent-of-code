# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

function count(b, _c) {
	_c = 0
	if (length(bags[b]) == 0) {
		return 0
	}

	for (i in bags[b]) {
		n = bags[b][i]
		_c = _c + n + n * count(i)
	}
	return _c
}
{
	outerBag = $1" "$2
	for (i = 5; i < NF; i += 4) {
		quantity = $i
		innerBag = $(i + 1)" "$(i + 2)
		if (n != "no") {
			bags[outerBag][innerBag] = quantity
		}
	}
}
END {
	print count("shiny gold")
}
