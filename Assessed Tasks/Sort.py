'''Selection Sort
   Input: Unsorted list
   output sorted list
   Uses selection sort with swap
'''
def select_sort(A):
    for i in range(len(A)-1):  #Outer loop iterates through the list to find the smallest values
        minn=i #declare minn variable to be equivalent to i
        for j in range(i+1, len(A)): #inner loop iterates through the list to check for smaller values
            if (A[j]<A[minn]): #checks if value in the listv is smaller than another value
                minn=j#sets the minn variable
        swap(A,i,minn)#calls swap function

    return A

def swap(A,i,minn):
    B = A[i]#creates buffer variable which is set to the element from the list
    A[i] = A[minn]#sets the i variable in the list to be equal to the minn variable in the list
    A[minn] = B# uses the stored buffer variable to set minn to what i was
    print(A)#prints to show the swap has been done
    return(A)#returns the list


select_sort([10,4,1,2,11,6,5])#sets the unsorted list we are to be using