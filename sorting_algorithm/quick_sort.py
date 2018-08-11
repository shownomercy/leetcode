class QuickSort:
    def __init__(self, list):
        self.list = list

    def partition(self, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            if (self.list[i] <= self.list[begin]):
                pivot += 1
                self.list[pivot], self.list[i] = self.list[i], self.list[pivot]

        self.list[begin], self.list[pivot] = self.list[pivot], self.list[begin]
        return pivot

    def quick_sort(self, begin=0, end=None):
        if end is None:
            end = len(self.list) - 1

        def _quick_sort(begin, end):
            if begin >= end:
                return
            pivot = self.partition(begin, end)
            _quick_sort(begin, pivot - 1)
            _quick_sort(pivot + 1, end)

        _quick_sort(begin, end)
