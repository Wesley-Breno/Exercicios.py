class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        heights_ordered = {}
        for index, number in enumerate(heights):
            heights_ordered[index] = number

        indexs = list(dict(sorted(heights_ordered.items(), key=lambda item: item[1], reverse=True)).keys())

        names_ordered = [names[index] for index in indexs]
        return names_ordered
