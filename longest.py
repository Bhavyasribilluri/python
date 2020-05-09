# to find the longest word in a given sentence
def longest_string(sentence):
    a=sentence.split(" ")
    max=0
    for i in a:
        print(i, len(i))
        l=len(i)
        if l>max:
            max=l
    print("longest word is of length", max)        
    for i in a:
        if len(i)==max:
          print(i) 
    
       
                  
       
longest_string("Life is full of surprises and miracles.")    