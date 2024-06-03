encoded=[1,2,3]
first=
arr=[first]
for i in range(len(encoded)):
    arr=(arr[i]^encoded[i])
print(encoded)
