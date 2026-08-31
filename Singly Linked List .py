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
    def transversal(self):
        if self.head is None:
            print("SSL is empty")

        else:
            current=self.head
            while current.next is not None:
                print(current.val)
                current=current.next
