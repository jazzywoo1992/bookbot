def main():
    bookPath = "books/frankinstein.txt"  # Corrected spelling
    text = getBookText(bookPath)
    numWords = wordcount(text)
    characterCount = charCount(text)

    # Sort the list of dictionaries by frequency in descending order
    sortedListDict = sorted(characterCount, key=getCharacterFrequency, reverse=True)

    print(f"--- Begin report of {bookPath} ---")
    print(f"{numWords} words found in the document")
    # Printing character frequencies from the sorted list
    for char_dict in sortedListDict:
        char, freq = list(char_dict.items())[0]
        print(f"The '{char}' character was found {freq} times")
    print("--- End report ---")


def wordcount(text): 
    words = text.split()
    return len(words)

def getBookText(bookPath):
    with open(bookPath) as f:
        return f.read()

def charCount(text):
    text = ''.join([i for i in text if i.isalpha()])
    dict = {}

    for i in text:
        lowered = i.lower()
        if lowered not in dict:
            dict[lowered] = 1
        else:
            dict[lowered] += 1
    
    listDict = [ {key:value} for key,value in dict.items()]
    return listDict

# Corrected version
def getCharacterFrequency(dict_item):
    return next(iter(dict_item.values()))

main()