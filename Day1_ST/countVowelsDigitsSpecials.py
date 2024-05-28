'''input:
oputput:"qe234$#@yghSioDFGHA@"
count of:
lowecasevowel-
uppercasevowel-
lowercaseconsonants-
uppercaseconsonants-
digits-
specialcharacters-'''
def count_characters(S):
    lv,uv,lc,uc,d,s = 0,0,0,0,0,0
    for char in S:
        if char.isalpha():
            if char.lower() in 'aeiou':
                if char.islower():
                    lv += 1
                else:
                    uv += 1
            else:
                if char.islower():
                    lc += 1
                else:
                    uc += 1
        elif char.isdigit():
            d += 1
        else:
            s += 1
    return lv, uv, lc, uc, d, s
S = "qe234$#@yghSioDFGHA@"
results = count_characters(S)
print("lv -", results[0])
print("uv -", results[1])
print("lc -", results[2])
print("uc -", results[3])
print("d -", results[4])
print("s -", results[5])
    
#ONLY SPECIAL CHARACTERS:
def count_special_characters(S):
    s = 0
    for char in S:
        if not char.isalnum():
            s+= 1
    return s

S = "qe234$#@yghSioDFGHA@"
s = count_special_characters(S)
print("s -", s)

    
