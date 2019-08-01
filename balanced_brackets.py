def isBalanced(s):
    if len(s) % 2 != 0:
        return 'NO'
    my_stack = []
    opening_braces = ['(', '{','[']
    matching_tuple = (('(',')'),('[',']'),('{','}'))
    for i in s:
        if i in opening_braces:
            my_stack.append(i)
        else:
            try:
                last_open = my_stack.pop()
                if (last_open, i) not in matching_tuple:
                    return 'NO'
            except IndexError:
                return 'NO'
    if len(my_stack) == 0:
        return 'YES'
    else:
        return 'NO'


print(isBalanced('{{()'))