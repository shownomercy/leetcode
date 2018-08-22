def merge_sort(a_list, start, end):
    if start >= end:
        return
    mid = (start + end) // 2

    merge_sort(a_list, start, mid)
    merge_sort(a_list, mid + 1, end)

    def merge(a_list, start, mid, end):
        a_list_tmp = [0] * (end - start + 1)

        i = start
        j = mid + 1

        k = 0
        while i <= mid and j <= end:
            if a_list[i] > a_list[j]:
                a_list_tmp[k] = a_list[j]
                j += 1
            else:
                a_list_tmp[k] = a_list[i]
                i += 1
            k += 1

        while i <= mid:
            a_list_tmp[k] = a_list[i]
            i += 1
            k += 1
        while j <= end:
            a_list_tmp[k] = a_list[j]
            j += 1
            k += 1

        for i in range(k):
            a_list[start + i] = a_list_tmp[i]

    merge(a_list, start, mid, end)


a_list = [4, 5, 7, 3, 5, 78, 1, 11, 44]
a_list = [2, 1]
a_list = [10, 20]

merge_sort(a_list, 0, len(a_list) - 1)
for num in a_list:
    print(num)