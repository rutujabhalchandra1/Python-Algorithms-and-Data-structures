def countingValleys(n, s):
    sea_level = 0
    num_of_valleys = 0
    num_negatives = 0
    for i in range(0,n):
        if s[i] == 'U':
            sea_level += 1
        else:
            sea_level -= 1
            num_negatives += 1
        if sea_level == 0 and s[i] == 'U':
            num_of_valleys += 1
    return num_of_valleys

result = countingValleys(12,'DDUUDDUDUUUD')
print(result)
