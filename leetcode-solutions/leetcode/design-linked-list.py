class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self): 
        self.head = node(-1)
        self.size = 0
            

    def get(self, index: int) -> int:
        dummy = self.head
        while dummy and index + 1 > 0:
            dummy = dummy.next
            # if dummy:
                # print(dummy.val)
            print(index)
            index -= 1
            

        return dummy.val if dummy else -1
        

    def addAtHead(self, val: int) -> None:
        dummy = self.head
        newNode = node(val)
        newNode.next = dummy.next
        self.head.next = newNode
        self.size += 1


        

    def addAtTail(self, val: int) -> None:
        newNode = node(val)

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = newNode
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        prev = node(-1)
        prev.next = curr
        found = True

        for _ in range(index + 1):

            prev = curr
            curr = curr.next

            if not curr:
                break


        if self.size < index:
            return 
            
        if index == 0:
            self.addAtHead(val)
        else:
            newnode = node(val)
            prev.next = newnode
            newnode.next = curr
            
        self.size += 1

        # print(self.head.val, self.head.next.val)


        

    def deleteAtIndex(self, index: int) -> None:
        prev = node(0)
        curr = self.head
        prev.next = curr

        for _ in range(index + 1):
            prev = curr
            curr = curr.next

            if not curr:
                break


        if curr:
            prev.next = curr.next
            curr.next = None
        else:
            prev.next = None
        if index == 0:
            self.head.next = prev.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)