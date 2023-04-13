def MergeSort(UnsortedArray):
    if len(UnsortedArray) > 1:


        MiddleOfArray = len(UnsortedArray)//2

        FirstHalf = UnsortedArray[:MiddleOfArray]
        SecondHalf = UnsortedArray[MiddleOfArray:]


        MergeSort(FirstHalf)
        MergeSort(SecondHalf)

        i=j=k=0

        while i < len(FirstHalf) and j < len(SecondHalf):
            if FirstHalf[i] < SecondHalf[j]:
                UnsortedArray[k] = FirstHalf[i]
                i += 1
            else:
                UnsortedArray[k] = SecondHalf[j]
                j += 1
            k += 1

        while i < len(FirstHalf):
            UnsortedArray[k] = FirstHalf[i]
            i += 1
            k += 1

        while j < len(SecondHalf):
            UnsortedArray[k] = SecondHalf[j]
            j += 1
            k += 1


def printList(UnsortedArray):
    for i in range(len(UnsortedArray)):
        print(UnsortedArray[i], end=" ")
    print()


if __name__ == '__main__':
    UnsortedArray = [6, 4, 9, 10, 2, 8, 1, 3, 7]

    MergeSort(UnsortedArray)

    print("Sorted array is: ")
    printList(UnsortedArray)
