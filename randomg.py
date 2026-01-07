import random
count=0
A=0
B=0
while count!='1':
    al=random.randint(65,90)
    print(chr(al))
    print("Press 1 to halt")
    count=input("Do you want to quit?(A or B or 1): ").lower()
    if (count=='b'):
        B+=1
    elif(count=='a'):
        A+=1
    elif(count=='1'):
        break
    else:
        print("Invalid Input")
print("A's Score:",A)
print("B's Score:",B)
if(A<B):
    print("Winner is B!!")
elif(A>B):
    print("Winner is A!!")
else:
    print("BOTH WINS!!")
               
