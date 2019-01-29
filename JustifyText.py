f = open('sample.txt', 'r')
paragraph = f.read()
#print (paragraph.split())

print(paragraph.split())

for i in paragraph.split():
    print(i)

