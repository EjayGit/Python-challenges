# Find words which are greater than given length k.

# Example usage
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k = int(input("Enter the maximum length of the words to wish to keep: "))

def removeWords(word_list, k):
    newList = []
    # for each word in words:
    for word in word_list:
        # if word is greater than k chars long.
        if len(word) > k:
            continue
        else:
            newList.append(word)
    return newList

print(f'The new list is: {removeWords(word_list, k)}')