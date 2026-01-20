# '''
# 快速排序
# nums: 待排序的列表
# start - end: 排序的范围
# '''
#
# def quick_sort(nums, start, end):
#     # 如果开始的索引小于结束的索引，说明范围内有两个或以上的元素需要排序
#     if start < end:
#         # 选择第一个元素作为基准值
#         pivot = nums[start]
#         low = start  # 从左边开始的指针
#         high = end   # 从右边开始的指针
#
#         # 两下标未相遇时继续循环
#         while low < high:
#             # 从右向左移动high指针，找到第一个小于基准值的元素
#             while low < high and nums[high] >= pivot:
#                 high -= 1
#             nums[low] = nums[high]  # 将找到的元素放到low位置
#
#             # 从左向右移动low指针，找到第一个大于基准值的元素
#             while low < high and nums[low] <= pivot:
#                 low += 1
#             nums[high] = nums[low]  # 将找到的元素放到high位置
#
#         nums[low] = pivot  # 将基准值放到最终位置
#
#         # 递归排序基准值左侧和右侧的子列表
#         quick_sort(nums, start, low - 1)
#         quick_sort(nums, low + 1, end)
#
# # 排序前的列表
# nums = [7, 6, 3, 9, 1, 8]
# print("排序前：", nums)
# quick_sort(nums, 0, len(nums) - 1)
# print("排序后：", nums)



# 这是会出问题的快速排序
'''
快速排序
nums:待排序列表
start-end:待排序区间
'''
# def quickSort(nums,start,end):
#    #如果开始位置和结束位置相同，说明只有一个数，不需要排序
#    if start < end:
#       #取出标准数
#       standard = nums[start]
#       #记录下左右下标
#       low = start
#       high = end
#       #两下标未重合，就循环
#       while low<high:
#          #右下标向左寻找小于标准数的数,使用大于判断，循环结束，表示找到了小于标准数的数
#          while low<high and nums[high]>=standard:
#             high-=1
#          #将寻找到的数存入左下标所在位置
#          nums[low]=nums[high]
#          #左下标向右寻找大于标准数的数
#          while low<high and nums[low]<standard:
#             low+=1
#          #将寻找到的数存入右下标所在位置
#          nums[high]=nums[low]
#       #将标准数存入两下标重合处
#       nums[low]=standard
#       #递归处理小于等于标准数部分
#       quickSort(nums,start,low)
#       #递归处理大于标准数部分
#       quickSort(nums,low+1,end)
# #待排序列表
# list = [2, 1]
# #快速排序
# quickSort(list,0,len(list)-1)
# #输出结果
# print(list)


'''
结论： 它是靠多跑了一轮递归，把基准数（Pivot）作为下一次排序的最大值，
再次筛选了一遍，最终让 low 减小，从而终止了递归。
'''

import time
import sys
import random
import copy

# 修改递归深度限制，否则代码2在处理倒序长列表时会直接报错崩溃
sys.setrecursionlimit(10000)

# ===========================
# 1. 你的代码 (Code 2) - 有隐患
# ===========================
calls_code_2 = 0  # 计数器


def quickSort_User(nums, start, end):
   global calls_code_2
   calls_code_2 += 1

   if start < end:
      standard = nums[start]
      low = start
      high = end
      while low < high:
         while low < high and nums[high] >= standard:
            high -= 1
         nums[low] = nums[high]
         while low < high and nums[low] < standard:  # 注意这里是你原来的 <
            low += 1
         nums[high] = nums[low]
      nums[low] = standard

      # 你的写法：包含 low
      quickSort_User(nums, start, low)
      quickSort_User(nums, low + 1, end)


# ===========================
# 2. 标准代码 (Code 1) - 正确
# ===========================
calls_code_1 = 0  # 计数器


def quickSort_Standard(nums, start, end):
   global calls_code_1
   calls_code_1 += 1

   if start < end:
      pivot = nums[start]
      low = start
      high = end
      while low < high:
         while low < high and nums[high] >= pivot:
            high -= 1
         nums[low] = nums[high]
         while low < high and nums[low] <= pivot:  # 标准写法 <=
            low += 1
         nums[high] = nums[low]
      nums[low] = pivot

      # 标准写法：排除 low
      quickSort_Standard(nums, start, low - 1)
      quickSort_Standard(nums, low + 1, end)


# ===========================
# 测试部分
# ===========================
def run_test(test_name, data_list):
   print(f"--- 测试场景: {test_name} (数据量: {len(data_list)}) ---")

   # 准备两份一样的数据
   data1 = copy.deepcopy(data_list)
   data2 = copy.deepcopy(data_list)

   # 测试标准代码
   global calls_code_1
   calls_code_1 = 0
   start_time = time.perf_counter()
   quickSort_Standard(data1, 0, len(data1) - 1)
   end_time = time.perf_counter()
   print(f"【标准版】 耗时: {end_time - start_time:.6f} 秒 | 递归调用次数: {calls_code_1}")

   # 测试你的代码
   global calls_code_2
   calls_code_2 = 0
   start_time = time.perf_counter()
   try:
      quickSort_User(data2, 0, len(data2) - 1)
      end_time = time.perf_counter()
      print(f"【你的版】 耗时: {end_time - start_time:.6f} 秒 | 递归调用次数: {calls_code_2}")
   except RecursionError:
      print(f"【你的版】 报错: 递归深度溢出！无法完成排序。")

   print("-" * 30)


# 生成测试数据
# 1. 随机数据 (差异不大)
random_list = [random.randint(0, 10000) for _ in range(2000)]

# 2. 倒序数据 (差异巨大 - 这是快排的噩梦场景)
# 注意：数据量如果太大，你的代码会直接爆栈，所以我们只用 1500 个数
reverse_list = list(range(1500, 0, -1))

if __name__ == "__main__":
   run_test("随机乱序列表", random_list)
   run_test("完全倒序列表", reverse_list)