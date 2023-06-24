stack=[]
def push():
    
    element=int(input("enter the element"))
    stack.append(element)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element is",e)
        print (stack)
def display():
    print(stack)
while True:
    print("enter the option 1.push 2.pop 3.display 4.break")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice ==3:
        display()
    elif choice==4:
        break
    else:
        print("enter correct operation")
        