class Nodes:
    def __init__(self,val):
        self.val=val
        self.next=None

class Singly_Linked_List:
    def __init__(self):
        self.head=None

    def append(self,val):

        new_node=Nodes(val)
        if self.head==None:
            self.head=new_node

        else:
            current=self.head

            while current.next is not None:
                current=current.next

            current.next=new_node
    def traversal(self):
        if self.head is None:
            print("SSL is empty")

        else:
            current=self.head
            while current is not None: 
                print(current.val,end=" ")
                current=current.next
            print()

    def insertion(self,val,position):
        new_node=Nodes(val)

        if count==0:
            new_node.next=self.head
            self.head=new_node

        else: 
            current=self.head
            previous=None
            count=0
            while current is not None and count < position :
                previous=current
                current=current.next
                count+=1
            previous=new_node
            new_node.next=current

    def deletion(self,val):

        temp=self.head
        if temp.val==val:
            self.head=self.head.next
            temp.next=None
            del temp
            return
        
        else:
            previous=None
            current=self.head
            count=0
            while current is not None and current.val!=val :
                previous=current
                current=current.next
                count+=1
                
            previous.next=current.next
            del current

sll = Singly_Linked_List()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(1)
sll.traversal()