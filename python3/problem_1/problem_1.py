"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def find_sum_index_in_one_loop_by_dict(num_list, target_sum):
    been_through_element_dict = dict()
    for index, num in enumerate(num_list):
        if num > target_sum:
            continue
        else:
            if num in been_through_element_dict.keys():
                return [been_through_element_dict[num], index]
            else:
                been_through_element_dict[target_sum - num] = index
    return [-1, -1]


def find_sum_index_in_one_loop_by_list(num_list, target_sum):
    been_through_element_list = []
    for index, num in enumerate(num_list):
        if num in been_through_element_list:
            return [been_through_element_list.index(num), index]
        else:
            been_through_element_list.append(target_sum-num)
    return [-1, -1]


if __name__ == '__main__':
    print(find_sum_index_in_one_loop_by_list([-3, 4, 3, 90], 0))
