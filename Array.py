class Array:
    def __init__(self):
        self.ls = []
        
    def insertToList(self,index,value):
        self.ls.insert(index, value)

    def printList(self):
        print(self.ls)

    def removeFromList(self, value):
        self.ls.remove(value)
    
    def appendToList(self,value):
        return self.ls.append(value)

    def sortList(self):
        return self.ls.sort()

    def popItem(self):
        return self.ls.pop()

    def reverseList(self):
        return self.ls.reverse()

if __name__ == '__main__':
    ls = List()
    ls.appendToList(1)
    ls.appendToList(6)
    ls.appendToList(10)
    ls.appendToList(8)
    ls.appendToList(9)
    ls.appendToList(2)
    ls.appendToList(12)
    ls.appendToList(7)
    ls.appendToList(3)
    ls.appendToList(5)
    ls.insertToList(8, 66)
    ls.insertToList(1, 30)
    ls.insertToList(6, 75)
    ls.insertToList(4, 44)
    ls.insertToList(9, 67)
    ls.insertToList(2, 44)
    ls.insertToList(9, 21)
    ls.insertToList(8, 87)
    ls.insertToList(1, 75)
    ls.insertToList(1, 48)
    ls.printList()
    ls.reverseList()
    ls.printList()
    ls.sortList()
    ls.printList()
    ls.appendToList(2)
    ls.appendToList(5)
    ls.removeFromList(2)
    ls.printList()'
    
    
    ls.insertToList(0, 5)
    ls.insertToList(1, 10)
    ls.insertToList(0, 6)
    ls.printList()
    ls.removeFromList(6)
    ls.appendToList(9)
    ls.appendToList(1)
    ls.sortList()
    ls.printList()
    ls.popItem()
    ls.reverseList()
    ls.printList()
'