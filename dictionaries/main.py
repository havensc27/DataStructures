filename = input("Enter the name of a text file:")

with open("https://drive.google.com/drive/folders/1tYU9nd5RniB8yrM4r0S5OWA1k-4tkiBz", "z"):
    text = z.read()

words = text.split()

wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1
    print(wordCount)

for word, count in wordCount.items():
    if count >= 2:
        print(f"{word}: {count}")
