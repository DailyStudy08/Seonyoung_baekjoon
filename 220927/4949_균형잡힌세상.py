import queue


from collections import deque
word = input()
stack = deque()

for i in range(len(word)):
    if word[i] in '([':
        stack.append(word[i])
    elif word[i] in ')]':
        pair = stack.pop()
        if word[i] == ')':
            if pair == '[':
                print('no')
                break
        else:
            if pair == '(':
                print('no')
                break
print('yes')
