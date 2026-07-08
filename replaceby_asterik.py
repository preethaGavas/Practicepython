word=input("Enter the Word:")
Final=""
print(len(word))
for ch in range(len(word)):
    if ch%2==0:
        Final=Final+"*"
    else:
        Final=Final+word[ch]
print(Final)
        