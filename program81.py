# Compute the frequency of the words from the input. The output should also sort the keys alphanumerically.

sentence = str(input("Enter the input sentence: "))

# Parse the input
sentenceList = sentence.split(' ')

newList = []
for word in sentenceList:
    word = word.strip('.,? ')
    word = word.lower()
    newList.append(word)

print(newList)
# create set
sentenceSet = set(newList)

dictList = []
# for each word in set, count the number of times word appears in sentenceList.
for word1 in sentenceSet:
    count = 0
    for word2 in newList:
        if word1 == word2:
            count = count + 1
            print(word1)
            print(count)
    # insert key and value pair into list element as tuple. e.g. [(word, number), (word2, number2), (word3, number3)]
    dictList.append((word1, count))
    
# convert list to dict
sentenceDict = dict(sorted(dict(dictList).items()))

print(sentenceDict)