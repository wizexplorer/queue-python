L=[]
def enqueue():
    addMore="y"
    while(addMore.lower()!="n"):
        name=input("\t     Enter the name of the customer to add : ")
        print("\t     The customer",name,"has been added")
        L.append(name)
        addMore=input("\t     Add more(y/n) ? ")
        if addMore.lower() !="y" and addMore.lower() !="n":
            print("\t\t     Wrong input")
            addMore=input("\t     Add more(y/n) ? ")
    print("\t     Current customer list : ",L)

def isEmpty():
    if L==[]:
        return True
    else:
        return False

def peek():
    if isEmpty()==True:
        print("\t    The queue is empty")
    else:
        print("\t    The first customer is  :",L[0])

def dequeue():
    delMore="y"
    while(delMore.lower()!="n"):
        if isEmpty()==True:
            print("\t    The queue is empty, enter a name to remove first")
            add_or_not=input("\t     Insert book(y/n) ? ")
            if add_or_not.lower()=="y":
                enqueue()
            elif add_or_not.lower()=="n":
                break
            else:
                print("\t\t     Wrong input")
                add_or_not=input("\t     Insert name(y/n) ? ")
        else:
            x=L.pop(0)
            print("\t     The customer",x,"has been removed")
            delMore=input("\t     Remove more(y/n) ? ")
            if delMore.lower() !="y" and delMore.lower() !="n":
                print("\t\t     Wrong input")
                delMore=input("\t     Remove more(y/n) ? ")
    print("\t     Current customer list : ",L)
    
def traversal():
    n=len(L)
    if isEmpty()==True:
        print("\t     Queue is empty nothing to print")
        add_or_not="y"
        while(add_or_not!="n"):
            add_or_not=input("\t     Insert some names(y/n) ? ")
            if add_or_not.lower()=="y":
                enqueue()
            elif add_or_not.lower()=="n":
                traversal()
            else:
                print("\t\t     Wrong input")
                add_or_not=input("\t     Insert more(y/n) ? ")
    else:
        print("*"*65)
        print("\t\t  Current list : ",end='')
        for i in range(len(L)):
            if i==len(L)-1:
                print(L[i])
            else:
                print(L[i],end='-')
        print("*"*65)
choice=0
print("|----------------------EXPERIMENT NO.02-------------------------|")
print("|                     QUEUE OF CUSTOMERS                        |")

while(choice!='5'):
    print("-"*65)
    print("\t\t 1: Insert a customer's name")
    print("\t\t 2: Remove a customer's name")
    print("\t\t 3: Who's my first customer?")
    print("\t\t 4: Print current customers' list")
    print("\t\t 5: EXIT")
    choice=input("\t\t Enter your choice : ")
    if choice=='1':
        enqueue()
    elif choice=='2':
        dequeue()
    elif choice=='3':
        peek()
    elif choice=='4':
        traversal()
    elif choice!='1' and choice!='2' and choice!='3' and choice!='4' and choice!='5':
        print("Wrong input; input numbers from 1 to 5")
    
else :
    print("\t\t-->Exiting loop")
