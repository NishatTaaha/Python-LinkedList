class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self._length = 0
    def display(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next

    def insertBegin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insertEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node

    def insertAfterGivenNode(self,data,givenPtr):
        n=self.head
        while n is not None:
            if givenPtr==n.data:
                break
            n=n.next
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node

    def insertBeforeGivenNode(self,data,givenPtr):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==givenPtr:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data==givenPtr:
                break
            n = n.next        
        if n.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node    

    def insertInempty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is empty!!") 

    def deleteBegin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next

    def deleteEnd(self):
        if self.head is None:
            print("The Linked List is already empty")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def deleteByValue(self,x):
        if self.head is None:
            print("Can't delete Linked List is empty")
            return
        if x==self.head.data:
            self.head=self.head.next
            return
        n=self.head
        while n.next is not None:
            if x==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Node is not present!!")
        else:
            n.next=n.next.next

    def reverseLinkedList(self):
        prevPtr = None
        currentPtr = self.head
        while(currentPtr is not None):
            next = currentPtr.next
            currentPtr.next = prevPtr
            prevPtr = currentPtr
            currentPtr = next
        self.head = prevPtr


    def findIndex(self,key):
        curr = self.head
        index = 0
        while curr:
            if curr.data == key:
                return index
            curr = curr.next
            index = index + 1
        return -1


    def sortingList(self):
        curr=self.head
        pos=None
        if(self.head==None):
            return
        else:
            while(curr!=None):
                pos=curr.next
                while(pos!=None):
                    if(curr.data>pos.data):
                        temp=curr.data
                        curr.data=pos.data
                        pos.data=temp
                    pos=pos.next
                curr=curr.next

  
    def lengthOfLL(self):
        temp=self.head 
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def maximumInLL(self):
        max=-100000
        head=self.head
        while(head!=None):
            if(max<head.data):
                max=head.data
            head=head.next
        return max

    def minimumInLL(self):
        min=100000
        head=self.head
        while(head!=None):
            if(min>head.data):
                min=head.data
            head=head.next
        return min

    def removeDuplicates(self):
        curr = self.head
        prev = None
        duplicateList = dict()
        while curr:
            if curr.data not in duplicateList:
                duplicateList[curr.data] = None
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next



# print("INSERTING VALUES: ")
# PyLL=LinkedList()
# PyLL.insertInempty(100)
# PyLL.insertBegin(30)
# PyLL.insertEnd(40)
# PyLL.insertBegin(30)
# PyLL.insertEnd(100)
# PyLL.insertAfterGivenNode(20,40)
# PyLL.insertBeforeGivenNode(10,30)
# PyLL.display()
# print("*****************")
# print("REVERSING VALUES: ")
# PyLL.reverseLinkedList()
# PyLL.display()
# print("*****************")
# print("SORTING: ")
# PyLL.sortingList()
# PyLL.display()
# print("*****************")
# print("OTHERS: ")
# index=PyLL.findIndex(30)
# print(index)
# print(len(PyLL))
# maxnum=PyLL.maximumInLL()
# print(maxnum)
# minnum=PyLL.minimumInLL()
# print(minnum)
# print("*****************")
# print("Remove Duplicates: ")
# PyLL.removeDuplicates()
# PyLL.display()
# print("*****************")
# print("DELETING VALUES: ")
# PyLL.deleteBegin()
# PyLL.deleteEnd()
# PyLL.deleteByValue(30)
# PyLL.display()
