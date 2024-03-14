# [4,0,1,1,3]
nums = [8, 1, 2, 2, 3]

# [2,1,0,3]
# nums = [6, 5, 4, 8]

# [0,0,0,0]
# nums = [7, 7, 7, 7]

smaller_numbers = []
for num in nums:
    cont = 0
    for n in nums:
        if n < num:
            cont += 1
    smaller_numbers.append(cont)

smaller_numbers = [sum([1 for n in nums if n < num]) for num in nums]

print(smaller_numbers)
