
def unique_words(para):
    words = para.split()
    unique = set(words)
    return unique

paragraph = input("Enter a paragraph: ")
unique = unique_words(paragraph)
print("Unique words in the paragraph:")

for word in unique:
    print(word)



