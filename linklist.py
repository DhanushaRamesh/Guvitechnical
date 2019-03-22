class Node:

   def __init__(self,data):
       self.data = data
       self.next = None
class LinkedList:

    def __init__(self):
       self.head = None
       self.last_node = None
    def addNode(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def remove(self,position):
        if self.head == None:
            return
        temp=self.head
        if position == 0:
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        next=temp.next.next
        temp.next=None
        temp.next=next
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
    def disp(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end='')
            cur=cur.next
a=LinkedList()
n=int(input("enter n no of elements:"))
print("\nenter data")
for i in range(n):
      data=int(input())
      a.addNode(data)
print("\n link list:")
a.disp()
value=int(input("\n enter data position to be deleted:"))
a.remove(value)
a.disp()
print("\n element deleted")
print("\n Reverse link list:")
a.reverse()
a.disp()
