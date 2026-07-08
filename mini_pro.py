#Word Frequency: Take a sentence and count how many times each word appears using a
#dictionary.only use list tuple set and dict data structures. Do not use any built in functions except for print and input.while for loop

count ={}
sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
for word, frequency in count.items():
    print(word, frequency)

        # Continuation:# Add a function to sort the dictionary by value (frequency) and print it
def sort_by_value(my_dict):
    return sorted(my_dict.items(), key=lambda x: x[1], reverse=True)    
sorted_count = sort_by_value(count)
print("\nSorted word frequencies:")
for word, frequency in sorted_count:
    print(word, frequency)# Continuation:# Add a function to filter out common stop words (like "the", "is", "and") from the count
def filter_stop_words(my_dict):
    stop_words = {"the", "is", "and", "a", "an", "in", "on", "at", "to", "for"}
    filtered_dict = {}
    for word, frequency in my_dict.items():
        if word not in stop_words:
            filtered_dict[word] = frequency
    return filtered_dict
filtered_count = filter_stop_words(count)
print("\nFiltered word frequencies (without stop words):")
for word, frequency in filtered_count.items():
    print(word, frequency)
    def sort_by_value(my_dict):
    return sorted(my_dict.items(), key=lambda x: x[1], reverse=True)    
sorted_count = sort_by_value(count)
print("\nSorted word frequencies:")
for word, frequency in sorted_count:
    print(word, frequency)
  
def filter_stop_words(my_dict):


