def count_primes(low,high):
    count = 0
    for i in range(low, high + 1):
        check = True
        if i > 1:
            for z in range(2, int(((i ** .5) + 1))):
                if (i % z) == 0:
                    check = False
            if check == True:
                count += 1
                print(str(i) + ' is prime')
    return count
