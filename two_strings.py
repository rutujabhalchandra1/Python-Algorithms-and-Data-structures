def twoStrings(s1, s2):
    var = ''
    for i in s1:
        if i in s2:
            var = 'YES'
            break
        else:
            var = 'NO'
    return var

twoStrings('aardvark', 'apple')
