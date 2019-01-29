f = open('sample.txt', 'r')
paragraph = f.read()
#print (paragraph.split())
words = paragraph.split()
# need buffer to store words
buffer = []
#looping through all words
for x in range(len(words)):
    word = words[x]
    # creating a condition for buffer
    if sum([len(i) for i in buffer]) + len(word) + len(buffer) <= 20:
        buffer.append(word)
        flag = False
