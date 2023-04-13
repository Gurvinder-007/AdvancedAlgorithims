class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def Insert(self,val_before,newdata):
        if val_before is None:
            print("no node to insert after")
            return
        else:

            NewNode= Node(newdata) #creates a NewNode variable which has the data of the new node that is being inserted

            check= self.headval# sets the variable check to the starting value in the list which we will use for checks

            while(check.nextval): #loop will iterate so long as the graph has values

                check=check.nextval#will have the code keep looping through the days
                if check.dataval==val_before: #once has found the value the day needs to be inserted after will stop the loop
                    print(check.dataval) #prints value to ensure we are using the correct variable for the day
                    break #breaks the loop to move onto the swap


            B=check.nextval#creates a buffer variable which is set to what the next value in the list  before the swap was
            check.nextval=NewNode#will swap that value with the new value we are inserting
            NewNode.nextval=B # will re insert the value befpreinto the list using the buffer variable to ensure the list is correct


list = SLinkedList()
list.headval = Node("Mon")



e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun")
list.Insert("Tue","Weds")
list.listprint()
