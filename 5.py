def find(word,sentence):
    if word in sentence:
        print(word," appears at index ",sentence.index(word))
    else:
        print(word," is not present in the given sentence")
sentence=input("Enter a sentence : ")
word=input("Enter a word to search : ")
find(word,sentence)
