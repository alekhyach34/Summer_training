key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
def decode(key, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for char in message:
        if char in alphabet:
            key_index = key.find(char)
            result += alphabet[key_index]
        else:
            result += char
    return result
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decode(key, message))  