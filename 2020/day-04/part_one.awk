# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

BEGIN {
	RS="\n\n" # Record separator = empty line
}

# If a record matches all the regular expressions is valid
/byr/ && /iyr/ && /eyr/ && /hgt/ && /hcl/ && /ecl/ && /pid/ {
	valid++
}

END {
	print valid
}
