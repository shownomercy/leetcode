from quick_sort import QuickSort

my_list = [4, 6, 44, 57, 1, 77, 32, 11, 33, 3, 4]

qc = QuickSort(my_list)

print(qc.partition())

qc.quick_sort()

print(my_list)