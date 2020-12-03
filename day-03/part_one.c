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

	int treeCounter = 0;
	int index = 0;

	while (getline(&line, &tam, file) != -1) {
		char c = line[index];
		if (c == '#') {
			treeCounter++;
		}
		index = (index + 3) % (strlen(line) - 1);
	}

	printf("%d", treeCounter);

	free(line);
	fclose(file);

	return 0;
}
