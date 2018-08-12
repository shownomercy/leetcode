def heapify(a_list):
    """
    a_list is an array, and will be treated as a complete binary tree

    for a complete binary tree, each node at index i, will have its 

    left child index as 2 * i + 1, and right child index as 2 * i + 2
    (that's index starts from 0)

    heapify will be a bottom up behavior
    Arguments:
        list {[type]} -- [description]
    """

    def heapify_helper(the_list, index):
        if 2 * index + 1 >= len(the_list):
            return
        elif 2 * index + 2 >= len(the_list):
            if the_list[2 * index + 1] > the_list[index]:
                the_list[2 * index + 1], the_list[index] = the_list[
                    index], the_list[2 * index + 1]
        else:
            heapify_helper(the_list, 2 * index + 1)
            heapify_helper(the_list, 2 * index + 2)
            if the_list[index] >= max(the_list[2 * index + 1],
                                      the_list[2 * index + 2]):
                return
            if the_list[2 * index + 1] >= the_list[2 * index + 2]:
                the_list[index], the_list[2 * index + 1] = the_list[
                    2 * index + 1], the_list[index]
                heapify_helper(the_list, 2 * index + 1)
            else:
                the_list[2 * index + 2], the_list[index] = the_list[
                    index], the_list[2 * index + 2]
                heapify_helper(the_list, 2 * index + 2)

    heapify_helper(a_list, 0)


def heap_sort(a_list):
    heapify(a_list)
    ret = []
    while a_list:
        ret.append(a_list[0])
        a_list[0], a_list[len(a_list) - 1] = a_list[len(a_list) - 1], a_list[0]
        del a_list[len(a_list) - 1]
        heapify(a_list)
    return ret


ll = [2, 5, 1, 3, 6, 8, 9, 232]
#heapify(ll)
#for i in ll:
#    print(i)
#print("")
lll = heap_sort(ll)
#for i in lll:
#    print(i)
#for i in lll: print(i)
#print(*lll, sep='\n')
for i in lll:
    print(i)