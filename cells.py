def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    states.insert(0,0)
    states.insert(len(states),0)
    print (states)
    new_list = list()
    for j in range(0,days):
        for i in range(1,len(states)-1):
            print i
            print (states[i-1])
            print (states[i+1])
            if (states[i+1] == 0 and states[i-1] == 0) or (states[i+1] == 1 and states[i-1] == 1) :
                states[i] = 0
            else:
                states[i] = 1
        return states
result = cellCompete([1,0,0,0,0,1,0,0], 1)
print(result)


'''
def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    states.insert(0,0)
    states.insert(len(states),0)
    print states
    while days > 0:
        new_list = list()
        for i in range(1,8):
            print i
            print states[i-1]
            print states[i+1]
            if (states[i+1] == 0 and states[i-1] == 0) or (states[i+1] == 1 and states[i-1] == 1) :
                states[i] = 0
            else:
                states[i] = 1
        return states    
'''