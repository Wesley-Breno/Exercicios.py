"""
Basicamente...
Tire os valores duplicados de uma lista e os deixem em ordem.
Para os valores duplicados que foram retirados, coloque um '_' no lugar.

Exemplo 1;
    Input
        [0,0,1,1,1,2,2,3,3,4]
    Output
        [0,1,2,3,4,_,_,_,_,_]

Exemplo 2;
    Input
        [1,1,2]
    Output
        [1,2,_]

Restricoes;
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums é classificado em ordem não decrescente.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)

        nums.clear()
        for num in new_list:
            nums.append(num)

        return len(nums)


if __name__ == '__main__':
    list1 = [0,0,1,1,1,2,2,3,3,4]
    obj = Solution()
    response = obj.removeDuplicates(list1)
    print(response)


# [0,1,2,3,4,_,_,_,_,_]