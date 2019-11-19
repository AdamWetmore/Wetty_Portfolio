def binary_array_to_number(arr):
    total = 0
    multiplier = 2 ** (len(arr) - 1) 
    for i in arr:
        total += i * multiplier
        multiplier = multiplier / 2
    return total
