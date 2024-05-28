'''S=input()
for i in S:
    if i in 'aeiou':
        i.upper()
print(S)
input='placement'
output='plAcEmEnt' 
S = 'placement'
vowels = 'aeiouAEIOU'
result = ''

for char in S:
    if char in vowels:
        result += char.upper()
    else:
        result += char

print(result)
'''

S = input()
result = S.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
print(result)
