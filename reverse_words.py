'''
Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print ''.join(message)
'''


def reverse_words(message):
    left_index = 0
    right_index = len(message) - 1
    reverse_char(message, left_index, right_index)
    current_start = 0
    for i in range(len(message)+1):
        if (message[i] == ' ') or (i == len(message)):
            reverse_char(message, current_start, i-1)
            current_start = i + 1

def reverse_char(arr, left_index, right_index):
    while (left_index < right_index):
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        left_index += 1
        right_index -= 1

print(reverse_words([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]))