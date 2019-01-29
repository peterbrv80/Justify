#define function
def JustifyText(paragraph):
    #spliting sentence into separate strings
    words = paragraph.split(' ')
    # Flag for the both conditions to meet. Add to buffer and push
    flag = True
    # Final array
    save = []
    buffer = []
    # looping trough paragraph
    for x in range(len(words)):
        word = words[x]
        # len(buffer) is an estimate of the mininum number of spaces
        if sum([len(i) for i in buffer]) + len(word) + len(buffer) <= 20:
            #[len(i) for i in buffer]
            #y = 0
            #for i in buffer:
            #   y + = len(i)
            # adding words to buffer while less than 20
            buffer.append(word)
            flag = False
            # last step len(words) = last word index
        if flag or x + 1 == len(words):
            # set space count
            spaceOffset = 1
            # to add more if needed
            space = " "
            # checks if I need more spaces. Join converts array into strings
            while len((space * spaceOffset).join(buffer)) + len(space * spaceOffset) < 20:
                spaceOffset += 1
            # converts array to string and adds character (space) between words
            line = (space * spaceOffset).join(buffer)
            if len(line) != 20:
                extraOffset = 20 - len(line)
                # finding index from the right to put extra space
                target = line.rfind(' ')
                # constructing the line with extra space
                line = line[:target] + space * extraOffset + line[target:]
            # save = result
            save.append(line)
            # new and clean buffer with new word (from the loop)
            buffer = [word]
        flag = True

    return save

userInput = input("Enter input:")
result = JustifyText(userInput)

for i in range(len(result)):
    line = result[i]
    print('Array['+ str(i+1) + ']\t' + line)

