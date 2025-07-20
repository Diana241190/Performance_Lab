from statistics import median
import sys


with open(sys.argv[1], 'r') as f:
    nums = list(map(int, f.read().split()))

med = round(median(nums))
count = 0
for index, value in enumerate(nums):
    while value != med:
        if value > med:
            value -= 1
            nums[index] -= 1
        elif value < med:
            value += 1
            nums[index] += 1
        count += 1
print(count)