def reverse_part(word, ch):
    if ch in word:
        # Find the index of the first occurrence of the character 'ch'
        index = word.index(ch)
        
        # Reverse the substring from the beginning up to the found index
        reversed_word = word[:index+1][::-1] + word[index+1:]
    else:
        # If 'ch' is not in the word, return the original word
        reversed_word = word
    
    return reversed_word

# Example usage
word = "abcdefd"
ch = "d"
result = reverse_part(word, ch)
print(result)  # Output: "dcbaefd"
