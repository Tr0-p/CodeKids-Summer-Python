"""

@Author: Timothy
@Date: 5th June 2024

Reading and writing files

"""

uppercase = []
with open("story.txt", "r") as file:
    story = file.readlines()
    for i in range(0, len(story)):
        newSentence = story[i].upper()
        uppercase.append(newSentence)

with open("uppercase_story.txt", "w") as newFile:
    for i in range(0, len(uppercase)):
        newFile.write(uppercase[i])

all_words = []
for i in range(0, len(story)):
    words = story[i].lower().strip().split(" ")
    for j in range(0, len(words)):
        all_words.append(words[j])

# print(all_words[:20])
# print(len(all_words))

# counting the number of words

# step 1: go through the entire list of words
# step 2: if we see a new word, add it to our tally
# step 3: if we see a repeating word, increase the tally by 1

# What is something we can use to store our counting data?
# Hint: Dictionary

word_counter = {}
for i in range(0, len(all_words)):
    word = all_words[i]

    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] = word_counter[word] + 1

with open("word_counter.txt", "w") as wordCounterFile:
    for word, number in word_counter.items():
        wordCounterFile.write(f"{word}: {number}\n")
