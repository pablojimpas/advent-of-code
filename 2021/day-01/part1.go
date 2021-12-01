// SPDX-FileCopyrightText: 2021 Pablo Jiménez Pascual <pablo@jimpas.me>
//
// SPDX-License-Identifier: GPL-3.0-or-later

package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("usage: %s input.txt\n", os.Args[0])
		os.Exit(1)
	}
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatalf("open error: %v", err)
	}
	defer file.Close()

	count := 0
	last := math.MaxInt
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		current, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatalf("atoi error: %v", err)
		}
		if current > last {
			count++
		}
		last = current
	}
	if err := scanner.Err(); err != nil {
		log.Fatalf("scan error: %v", err)
	}
	fmt.Println(count)
}
