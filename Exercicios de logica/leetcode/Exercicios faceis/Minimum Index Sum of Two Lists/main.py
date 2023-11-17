class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = {}
        for index, word in enumerate(list1):
            list1_dict[index] = word

        list2_dict = {}
        for index, word in enumerate(list2):
            list2_dict[index] = word

        lower_sum_indexs = []
        for key, value_list1 in list1_dict.items():
            if value_list1 in list2:
                index_list2 = [key for key, value in list2_dict.items() if value == value_list1][0]
                lower_sum_indexs.append([int(key) + int(index_list2), value_list1])

        for key, value_list2 in list2_dict.items():
            if value_list2 in list1:
                index_list1 = [key for key, value in list1_dict.items() if value == value_list2][0]
                lower_sum_indexs.append([int(key) + int(index_list1), value_list2])

        keys = [key[0] for key in lower_sum_indexs]
        value1 = [value for key, value in lower_sum_indexs if key == min(keys)]

        return list(set(value1))