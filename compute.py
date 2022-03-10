#!/usr/bin/env python3
import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

# I am assuming that the input runs through threshold first, then limit
total = 0
for line in sys.stdin:
    curr = float(line.strip())
    threshold_result = max(0.0, curr - threshold)
    if limit > 0:
        limit_result = limit if limit < threshold_result else threshold_result
        total = total + limit_result
        print(limit_result)
        limit = limit - threshold_result
    else:
        limit = 0
        print(0.0)
print(total)

