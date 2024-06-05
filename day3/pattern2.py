'''Pattern:
ip:4
op:
    ....a....
    ...aba...
    ..abcba..
    .abcdcba.  '''

row = int(input())
a = 96
for i in range(1,row+1):
    for j in range(1, row+1-i):
        print(' ', end='')
    for j in range(1,i+1):
        print('%c' %(a+j), end='')
    for j in range(i-1,0,-1):
        print('%c' %(a+j), end='')
    print()
