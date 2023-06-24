class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new,data):
        new_node=node(new,data)
        new_node.next=self.head
        self.head=new_node
    def detectandremoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                print('meeting point:',slow_p.data)
                slow_p=self.head
                while(slow_p.next != fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                print('start of loop:',fast_p.next.data)
                fast_p.next=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
llist=linkedlist()
llist.head=node(50)
llist.head.next=node(20)
llist.head.next.next=node(15)
llist.head.next.next.next=node(4)
llist.head.next.next.next.next=node(10)
#create of loop
extra=node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist printlist()
llist.detectandremoveloop()
print('linked list after removing loop')
llist.printlist()