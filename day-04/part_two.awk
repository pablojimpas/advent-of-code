# SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
#
# SPDX-License-Identifier: GPL-3.0-or-later

BEGIN {
	RS="\n\n" # Record separator = empty line
}

# helper function for checking all the fields
function check(passport) {
	byr = passport["byr"];
	iyr = passport["iyr"];
	eyr = passport["eyr"];
	hgt = passport["hgt"];
	hcl = passport["hcl"];
	ecl = passport["ecl"];
	pid = passport["pid"];
	# Check birth year
	if (byr < 1920 || byr > 2002) {
		return 0;
	}
	# Check issue year
	if (iyr < 2010 || iyr > 2020) {
		return 0;
	}
	# Check expiration year
	if (eyr < 2020 || eyr > 2030) {
		return 0;
	}
	# Check height with units symbol
	if (hgt !~ /cm$/ && hgt !~ /in$/) {
		return 0;
	}
	# Check "cm" in range
	if (hgt ~ /cm$/) {
		split(hgt, value, "cm")
		hgt = value[1]
		if (hgt < 150 || hgt > 193) {
			return 0;
		}
	}
	# Check "in" in range
	if (hgt ~ /in$/) {
		split(hgt, value, "in")
		hgt = value[1]
		if (hgt < 59 || hgt > 76) {
			return 0;
		}
	}
	# Check hair color, hex value with 6 chars
	if (hcl !~ /^#([0-9]|[a-f]){6}$/) {
		return 0;
	}
	# Check eye color, maybe there is a better way of doing this
	if (!(ecl == "amb" || ecl == "blu" || ecl == "brn" || ecl == "gry" || ecl == "grn" || ecl == "hzl" || ecl == "oth")) {
		return 0;
	}
	# Check passport ID, nine-digit number
	if (pid !~ /^[0-9]{9}$/) {
		return 0;
	}
	# Everything is okay
	return 1;
}

# If a record matches all the regular expressions is valid
/byr/ && /iyr/ && /eyr/ && /hgt/ && /hcl/ && /ecl/ && /pid/ {
	# Iterate every field of the record
	for (i = 1; i <= NF; i++) {
		split($i, field, ":")
		passport[field[1]] = field[2]
	}
	if (check(passport)) {
		valid++
	}
}

END {
	print valid
}
