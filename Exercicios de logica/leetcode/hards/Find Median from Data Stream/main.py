class MedianFinder:
    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums = sorted(self.nums)
        len_nums = len(self.nums)
        index = int(len_nums/2)
        if len_nums % 2 == 0:
            numbers = self.nums[index-1:index+1]
            return sum(numbers) / 2
        return self.nums[index]