// SPDX-FileCopyrightText: 2023 Pablo Jiménez Pascual <pablo@jimpas.me>
//
// SPDX-License-Identifier: GPL-3.0-or-later

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[100];
    int sum = 0;

    while (fgets(line, sizeof(line), file) != NULL) {
        char line_concat[3] = {'\0', '\0', '\0'};
        for (int i = 0; i < strlen(line); i++) {
            if (line[i] >= '0' && line[i] <= '9') {
                if (line_concat[0] == '\0') {
                    line_concat[0] = line[i];
                }
                line_concat[1] = line[i];
            }
        }
        sum += atoi(line_concat);
    }

    printf("%d\n", sum);

    return 0;
}
