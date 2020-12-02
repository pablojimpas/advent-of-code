"""
Find three numbers in a given file that sum another number, print their product
"""
import sys
sum = int(sys.argv[2])
with open(sys.argv[1], "r") as file:
    data = [int(line.strip()) for line in file]
    data.sort()
    size = len(data)
    for i in range(size-2):
        left = i + 1
        right = size - 1
        while (left < right):
            if (data[i] + data[left] + data[right] == sum):
                print(data[i] * data[left] * data[right])
                exit(0)
            elif (data[i] + data[left] + data[right] < sum):
                left += 1
            else:
                right -= 1
