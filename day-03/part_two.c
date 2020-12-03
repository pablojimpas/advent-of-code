// SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
//
// SPDX-License-Identifier: GPL-3.0-or-later

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "%s", "Incorrect number of arguments");
		exit(1);
	}
	const char *filename = argv[1];
	FILE *file;
	size_t tam = 100;
	char *line = malloc(sizeof(char) * tam);
	if (line == NULL) {
		fprintf(stderr, "%s", "Error allocating memory");
		exit(1);
	}
	file = fopen(filename, "r");
	if (file == NULL) {
		fprintf(stderr, "%s", "Error opening the file");
		exit(1);
	}

	/*
	 * One counter & index for each movement:
	 * Right 1, down 1.
	 * Right 3, down 1.
	 * Right 5, down 1.
	 * Right 7, down 1.
	 * Right 1, down 2. Special case. lineCont % 2 == 0
	 */
	int treeCounters[5] = {0, 0, 0, 0, 0};
	int indexes[5] = {0, 0, 0, 0, 0};
	int rightMov[5] = {1, 3, 5, 7, 1};
	int lineCont = 0;

	while (getline(&line, &tam, file) != -1) {
		if (lineCont % 2 == 0) {
			int index = indexes[4];
			char c = line[index];
			if (c == '#') {
				treeCounters[4]++;
			}
			indexes[4] = (index + rightMov[4]) % (strlen(line) - 1);
		}
		lineCont++;
		for (int i = 0; i < 4; i++) {
			int index = indexes[i];
			char c = line[index];
			if (c == '#') {
				treeCounters[i]++;
			}
			indexes[i] = (index + rightMov[i]) % (strlen(line) - 1);
		}
	}

	long long result = 1;
	for (int i = 0; i < 5; i++) {
		result = result * treeCounters[i];
	}

	printf("%lld", result);

	free(line);
	fclose(file);

	return 0;
}
