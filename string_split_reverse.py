sen=input("Type the sentence:")
words=sen.split()
for word in words:
    print(word[::-1],end=" ")
    
