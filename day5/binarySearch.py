'''
二分查找
'''


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    # ✅ 修正点1：使用 <=，防止漏掉由于 low==high 导致的最后一个元素
    while low <= high:
        # ✅ 修正点2：mid 在循环内部计算即可，不需要初始化在外面
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # ✅ 修正点3：如果循环结束还没找到，通常返回 -1 表示不存在
    return -1


# # 测试数据
# my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # 别用 list 做变量名，它是Python关键字
# target = 3
#
# result = binary_search(my_list, target)
# print(f"目标值索引为: {result}")
#
# list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target = 3
# result = binarySearch(list, target)
# print(result)


