def longest_word(sentence):
    a=sentence.split(" ")
    max=0
    for i in a:
        print(i, len(i))
        l=len(i)
        if l>max:
            max=l

    print("the longest word is of the length", max)  

longest_word("stay single forever")