'''i/p:"hello:5438,car:214,book:8799,apple:2187"
o/p:oaxp-->len(hello) is 5 5th position is o;
len(car) is 3 3 is not present,nearest 3rd position is 2,2nd position has a so take a;
len(book) is 4 4th position not there 4th nearest is 3 3rd position also not present take x,and less positions than 3 are not present; 
len(apple)5  nearest is 2 2nd position has p take p--->o/p is oaxp
def extract_first_letter(input_string):
    words = s.split(',')
    output = ''.join(word[0] for word in words)
    return output
s= "hello:5438,car:214,book:8799,apple:2187"
result = extract_first_letter(s)
print(result)
def extract_letters(input_string):
    words = input_string.split(',')
    #output = ""
    for i in words:
        b=i.split(',')
        word, num = word.split(':')
        num = int(num)
        pos = (num - 1) % len(word)  
        letter = word[pos] 
        output += letter
    return output '''

inp = "hello:5438,car:214,book:8799,apple:2187"

def leng(x, y):
    xi = len(x)
    while xi not in map(int, str(y)):
        xi -= 1
        if xi < 1:
            return 0  # Return xi if it becomes less than 1
    return xi
s = ''
for i in inp.split(','):
    x, y = i.split(':')
    if str(len(x)) in str(y):
        s += x[len(x) - 1]
    else:
        length = leng(x, y)
        if length < 1:
            s += 'x'
        else:
            s += x[length-1]
print(s)

