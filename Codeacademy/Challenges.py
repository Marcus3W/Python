# 1. Divisible by Ten

def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count += 1
    return count

#print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings

def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list

#print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers

def delete_starting_evens(my_list):
    while (len(my_list) > 0 and my_list[0] % 2 == 0):
        my_list = my_list[1:]
    return my_list

#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

# 4. Odd Indices
def odd_indices(my_list):
    new_list = []
    for i in range(1, len(my_list), 2):
        new_list.append(my_list[i])
    return new_list
#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents

def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list
#print(exponents([2, 3, 4], [1, 2, 3]))


# Advanced

# 1. Larger Sum
def larger_sum(lst1, lst2):
    x = 0
    y = 0
    for item in lst1:
        x += item
    for item in lst2:
        y += item
    return lst1 if x > y else lst2

#print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Over 9000
def over_nine_thousand(lst):
    sum = 0

    for item in lst:
        sum += item
        if sum > 9000:
            break
    return sum

#print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num
def max_num(nums):
    max = nums[0]
    for item in nums:
        if item > max:
            max = item
    return max

#print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values
def same_values(lst1, lst2):
    new_list = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
                new_list.append(index)
    return new_list

#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5. Reversed List
def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
            if lst1[i] != lst2[len(lst2) - 1 - i]:
                return False
    return True

#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))

