while True:
    n = int(input("\nEnter the Number (Enter 0 or a negative number to exit): "))
    if n <= 0:
        break
    if n%3==0:
        print("jugs",end=" ")
    if n%6==0:
        print("mugs",end=" ")
    if n%9==0:
        print("pugs",end=" ")
    if n%3 !=0 and n%6 !=0 and n%9 !=0:
        print("None")
print("\nThanks for trying!")