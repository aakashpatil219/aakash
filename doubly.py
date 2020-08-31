class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class DoublyLinkedList:    
    def __init__(self):    
        self.head = None
        self.tail = None
    def addNode(self, data):
        self.newNode = Node(data)
        if(self.head == None):
            self.head = self.tail = self.newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = self.newNode
            self.newNode.previous = self.tail
            self.tail = self.newNode
            self.tail.next = None
    def removeNode(self):
        self.head = self.head.next
        return self.head
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
    
    def add_tail(self,data):
        new_value = Node(data)
        self.get_tail().next = new_value
        
    def remove_tail(self):
         self.tail = self.tail.previous
         return self.tail
             
    def display(self):
        current = self.head;    
        if(self.head == None):    
            print("List is empty")
            return;    
        print('List')
        while(current != None):    
            print(current.data)
            current = current.next
                
dL = DoublyLinkedList() 
dL.addNode(1)
dL.addNode(2)
dL.addNode(3)
dL.addNode(4)
dL.addNode(5)
dL.display()
dL.removeNode()
dL.display()
dL.add_tail(6)
dL.display()
#dList.remove_tail()
dL.display()
#print(dList.get_tail())