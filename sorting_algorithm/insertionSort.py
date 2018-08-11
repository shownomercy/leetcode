def insertionSort(list):
    """
    insertion sort on a array (not a linked list)
    
    Arguments:
        list {[type]} -- [description]
    """

    for sorted in range(len(list)):
        if sorted == len(list) - 1:
            return
        else:
            unsorted = sorted + 1
            for i in range(unsorted):
                if list[i] > list[unsorted] and i == unsorted - 1:
                    list[i], list[unsorted] = list[unsorted], list[i]
                elif list[i] > list[unsorted]:
                    value = list[unsorted]
                    for j in reversed(range(i, unsorted)):
                        list[j + 1] = list[j]
                    list[i] = value
            sorted += 1


list = [2, 4, 6, 2, 76, 7]
#list = [4, 3]
insertionSort(list)
for i in list:
    print(i)