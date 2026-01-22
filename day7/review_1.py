# def quick_sort(nums, start, end):
#     # 如果开始的索引小于结束的索引，说明至少有两个元素需要排序
#     if start < end:
#         # 选择第一个元素作为基准值
#         pivot = nums[start]
#         low = start
#         high = end
#
#         # 两下标为相遇时
#         while low < high:
#             # 从右向左移动high指针，找到第一个小于基准值的元素
#             while low < high and nums[high] >= pivot:
#                 high -= 1
#             nums[low] = nums[high]
#
#             while low < high and nums[low] <= pivot:
#                 low += 1
#             nums[high] = nums[low]
#
#         nums[low] = pivot
#
#         quick_sort(nums, start, low - 1)
#         quick_sort(nums, low + 1, end)
#
#
# #  --- 测试代码 ---
#
# import random
# # 生成随机数据
# data = [random.randint(1, 100) for _ in range(15)]
# print(f"原始列表: {data}")
# quick_sort(data, 0, len(data) - 1)
# print(f"排序结果: {data}")
from requests.packages import target


# def shell_sort(nums):
#     step = len(nums) // 2
#     #当步长大于0时，继续排序
#     while step > 0:
#
#         for i in range(step, len(nums)):
#             # 记录当前元素
#             current = nums[i]
#             # 从本组中得前一个位置开始比较，下表为i - step
#             j = i - step
#             # 遍历本组中前面得所有元素，若本组中前面的元素大于current，则将其后移
#             while j >= 0 and nums[j] > current:
#                 nums[j + step] = nums[j]
#                 j -= step
#
#             nums[j + step] = current
#
#         step //= 2
#
#
# # --- 测试代码 ---
# import random
# # 生成随机数据
# data = [random.randint(1, 100) for _ in range(15)]
# print(f"原始列表: {data}")
# shell_sort(data)
# print(f"排序结果: {data}")



# # 调整某一颗子树的最大顶堆
# def maxHeap(nums, size, parent):
#
#     left_child = 2 * parent + 1
#     right_child = 2 * parent + 2
#
#     largest = parent
#
#     if left_child < size and nums[left_child] > nums[parent]:
#         largest = left_child
#     if right_child < size and nums[right_child] > nums[largest]:
#         largest = right_child
#
#     if largest != parent:
#         temp = nums[parent]
#         nums[parent] = nums[largest]
#         nums[largest] = temp
#         maxHeap(nums, size, largest)
#
#
# def heap_sort(nums):
#     last = len(nums) - 1
#     parent = last // 2 - 1 if last % 2 == 0 else last // 2
#     while parent >= 0:
#         maxHeap(nums, len(nums), parent)
#         parent -= 1
#
#     i = last
#
#     while i > 0:
#         temp = nums[0]
#         nums[0] = nums[i]
#         nums[i] = temp
#
#         maxHeap(nums, i, 0)
#         i -= 1
#
#
#
# # --- 测试代码 ---
# import random
# # 生成随机数据
# data = [random.randint(1, 100) for _ in range(15)]
# print(f"原始列表: {data}")
# heap_sort(data)
# print(f"排序结果: {data}")

# def merge(left, right):
#     r, l = 0, 0
#     temp = []
#
#     # 当左右列表都有元素时，比较后放入新列表
#     while l  < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             temp.append(left[l])
#             l += 1
#         else:
#             temp.append(right[r])
#             r += 1
#
#     temp += left[l:]
#     temp += right[r:]
#
#     return temp
#
#
# def merge_sort(nums):
#
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#
#     return merge(left, right)
#
#
# # --- 测试代码 ---
# import random
# # 生成随机数据
# data = [random.randint(1, 100) for _ in range(15)]
# print(f"原始列表: {data}")
# sorted_data = merge_sort(data)
# print(f"排序结果: {sorted_data}")


# def radix_sort(nums):
#     # 获取最大长度
#     max_len = len(str(max(nums)))
#     # 创建嵌套列表作为队列
#     queues = [[] for _ in range(10)]
#
#     for x in range(1, max_len + 1):
#
#         for num in nums:
#         # 获取每个数字的对应位数，并放入对应队列
#             try:
#                 queueIndex = int(str(num)[-x])
#             except IndexError:
#                 queueIndex = 0
#
#             queues[queueIndex].append(num)
#
#         nums.clear()
#
#         for queue in queues:
#             nums.extend(queue)
#             queue.clear()
#
#
# # --- 测试代码 ---
# import random
# # 生成随机数据
# data = [random.randint(1, 100) for _ in range(15)]
# print(f"原始列表: {data}")
# radix_sort(data)
# print(f"排序结果: {data}")


# def binary_search(nums, target):
#     low = 0
#     high = len(nums) - 1
#
#     while low <= high:
#
#         mid = (low + high) // 2
#
#         if nums[mid] == target:
#             return mid
#
#         elif nums[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
#
#
#
# # --- 测试代码 ---
# # 有序列表
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# target = 30
# index = binary_search(my_list, target)
# print(f"找到目标，索引为: {index}")


# def interpolation_search(nums, target):
#     low = 0
#     high = len(nums) - 1
#
#     while low <= high and nums[low] <= target <= nums[high]:
#
#
#         #优化：如果只剩一个数，或者头尾相等，直接判断
#         if low == high:
#             if nums[low] == target:
#                 return low
#             return -1
#
#
#         pos = low + int(((high - low) * (target - nums[low]) / (nums[high] - nums[low])))
#
#         if nums[pos] == target:
#             return pos
#
#         elif nums[pos] < target:
#             low = pos + 1
#         else:
#             high = pos - 1
#
#     return -1
#
# # --- 测试代码 ---
# # 插值查找最适合这种“均匀分布”的数组
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# target = 30
# index = interpolation_search(my_list, target)
# print(f"找到目标，索引为: {index}")


def get_fib_k(n):

    F = [0, 1]
    k = 0

    # 找到足够覆盖数组长度的斐波那契数
    # 要求F[k] - 1 >= n
    while F[k] - 1 < n:
        k += 1
        if k >= len(F):
            F.append(F[-1] + F[-2])

    return F, k


def fibonaci_search(nums, target):
    n = len(nums)

    if n == 0: return -1

    F, k = get_fib_k(n)

    temp_nums = nums[:] + [nums[-1]] * (F[k] - 1 - n)

    low = 0
    high = n - 1

    while low <= high:

        mid = low + F[k - 1] - 1

        if target < temp_nums[mid]:
            high = mid - 1
            k -= 1
        elif target > temp_nums[mid]:
            low = mid - 2
            k -= 2
        else:

            if mid < n:
                return mid
            else:
                return n - 1

    return -1


# --- 测试代码 ---
# 斐波那契查找最适合这种“均匀分布
# 的数组
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 30
index = fibonaci_search(my_list, target)
print(f"找到目标，索引为: {index}")








