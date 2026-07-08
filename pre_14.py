
sen = input("Enter a sentence: ")
word_freq = {}
for word in sen.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequency:")

for word, freq in word_freq.items():
    print(f"{word}: {freq}")    


