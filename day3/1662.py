def are_concatenated_words_equal(word1, word2):
    concatenated_word1 = ''.join(word1)
    concatenated_word2 = ''.join(word2)
    return concatenated_word1 == concatenated_word2

# Example usage
word1 = ["ab", "c"]
word2 = ["a", "bc"]
result = are_concatenated_words_equal(word1, word2)
print(result)  # Output: True
