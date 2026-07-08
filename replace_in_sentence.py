sentence=input("Enter the sentence")
replace={"cat":"dog","apple":"orange","red":"blue"}
word=sentence.split()
for i in range(len(word)):
    if word[i] in replace:
        word[i]=replace[word[i]]
print(" ".join(word))

