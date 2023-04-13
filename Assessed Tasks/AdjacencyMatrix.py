class Graph(object):
    '''
    adjacency matrix
    Inputs: Takes edges we are either to add to the matrix or remove from the matrix
    Output: adjacency matrix once we have added or removed
    '''



    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(*self.adjMatrix, sep='\n')
        self.size = size

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here
    
    def addVertex(self,amount):
        size=self.size #will set a variable which contains the size of the entire matrix
        print("Current size of matrix is: " + str(size) ) # will print what the size of the graph is
        size= size+amount # will set the size to increase by adding the the amount that is being added to the matrix
        self.adjMatrix=[] will set the matrix as a list
        for i in range(size): #will create a loop to iterate through the size of the matrix
            self.adjMatrix.append([0 for i in range(size)]) #will append the list for each vertex for the size of the graph
        self.size=size# will set the size to the adjacency matrix to the self variable which is used to call size throughout all the code
        print("New size of the matrix is: " + str(self.size))# will print what the new size of the matrix is
  
    def addEdge(self,vertexI,vertexII):
        vertexI=vertexI-1 # will subtract from the variable set for the 1st vertex since lists in python start at 0 and the user will not assume that with inputs
        vertexII=vertexII-1 # will subtract from the variable set for the 2nd vertex since lists in python start at 0 and the user will not assume that with inputs
       # print(vertexI) #used to check if the vertex is correct
       # print(vertexII) #used to check if the vertex is correct
        if vertexI<0 or vertexII<0: # will check if either vertex is less than 0
            print("No because it is negative")# will tell us the vertexes are negative
            exit() # will exit the code because we cannot work with negative vertexes
        else:
            if vertexI==vertexII: #will check if either vertex is equal
                print("Same vertex %d and %d" % (vertexI,vertexII)) #will tell us the vertexes are equal

            elif vertexI!=vertexII:
                self.adjMatrix[vertexI][vertexII]=1 # will set the graph so it sets the edge to 1 showing there is weight on the edge
                self.adjMatrix[vertexII][vertexI]=1 # will set the graph so it sets the edge to 1 showing there is weight on the edge

    def removeEdge(self,vertexI,vertexII):
        vertexI=vertexI-1 # will subtract from the variable set for the 1st vertex since lists in python start at 0 and the user will not assume that with inputs
        vertexII=vertexII-1 # will subtract from the variable set for the 1st vertex since lists in python start at 0 and the user will not assume that with inputs

        self.adjMatrix[vertexI][vertexII]=0 # will set the edge to 0 to show there is no weight on the graph
        self.adjMatrix[vertexII][vertexI]=0 # will set the edge to 0 to show there is no weight on the graph

    def __len__(self):
        return self.size # will return the size of the matrix

    def printMatrix(self):
        print(*self.adjMatrix, sep='\n') #will print the matrix to show our results after we have removed or added edges
    


#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
        g = Graph(6)
        print("\n")
        g.addEdge(1,2)
        g.printMatrix()
        g.addEdge(3,4)
        print("\n")
        g.printMatrix()
        print("\n")
        g.removeEdge(3,4)
        g.printMatrix()

if __name__ == '__main__':
   main()
