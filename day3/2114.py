sentences = ["alice and bob love leetcode", "i think so too",
             "this is great thanks very much"]
max_words = max(len(sentence.split()) for sentence in sentences)

print(max_words)
