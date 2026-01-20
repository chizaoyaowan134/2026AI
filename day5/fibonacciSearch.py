# # --- 1. 辅助函数：生成斐波那契数据 ---
# def get_fib_k(n):
#     """
#     根据数组长度 n，生成足够长的斐波那契数列 F，
#     并找到最小的 k，使得 F[k]-1 >= n
#     :param n: 待查找数组的长度
#     :return: (F数列, k值)
#     """
#     # 初始化斐波那契数列 [0, 1, 1, 2, 3...]
#     F = [0, 1]
#     k = 0
#
#     # 循环生成，直到 F[k]-1 大于等于 n
#     # 比如 n=10，我们需要找到 F[k]=13 (此时k=7)，因为 13-1 >= 10
#     while F[k] - 1 < n:
#         k += 1
#         # 如果数列长度不够，就动态追加下一个斐波那契数
#         if k >= len(F):
#             F.append(F[-1] + F[-2])
#
#     return F, k
#
#
# # --- 2. 主函数：斐波那契查找 ---
# def fibonacci_search(nums, target):
#     """
#     核心查找逻辑
#     """
#     n = len(nums)
#     if n == 0:
#         return -1
#
#     # 第一步：调用辅助函数，获取必要的 F 和 k
#     F, k = get_fib_k(n)
#
#     # 第二步：补齐数组
#     # 因为斐波那契查找要求长度必须为 F[k]-1，不足的部分用最后一个元素填充
#     # 例如：原数组 [1, 5, 9]，n=3。F[k]=5。
#     # 需要补齐到 4个元素 -> [1, 5, 9, 9]
#     temp_nums = nums[:] + [nums[-1]] * (F[k] - 1 - n)
#
#     low = 0
#     high = n - 1
#
#     # 第三步：循环查找
#     while low <= high:
#         # 黄金分割分割点公式
#         mid = low + F[k - 1] - 1
#
#         # 此时 mid 可能落在补齐的区域，所以比较时用 temp_nums
#         if temp_nums[mid] < target:
#             # 目标在右半区 (剩下长度 F[k-2]-1)
#             low = mid + 1
#             k -= 2
#         elif temp_nums[mid] > target:
#             # 目标在左半区 (剩下长度 F[k-1]-1)
#             high = mid - 1
#             k -= 1
#         else:
#             # 找到了！处理补齐的情况
#             # 如果 mid 越过了原数组边界，说明找到的是补齐的重复值，返回原数组最后一个索引
#             if mid < n:
#                 return mid
#             else:
#                 return n - 1
#
#     return -1
#
#
# # --- 测试代码 ---
# list_data = [1, 5, 15, 22, 25, 31, 39, 42, 47, 49, 59, 68, 88]
# target = 47
#
# # 调用主函数
# result = fibonacci_search(list_data, target)
# print(f"找到目标，索引为: {result}")

'''
生成一个最后一个数大于num的斐波那契数列
'''
def fib(num):
   list = [1,1,2]
   a,b,c = 1,1,2
   while c<num:
      a = b
      b = c
      c = a + b
      list.append(c)
   return list
'''
斐波那契查找
nums 目标序列
value 要查找的目标值
'''
def fibonacciSearch(nums,value):
   #初始化最低索引，最高索引
   low,high = 0,len(nums)-1
   #初始化
   f = fib(high)
   #初始区间为最后一个区间
   block = len(f)-1
   #计算中间索引
   mid = low + f[block-1] - 1
   #循环处理
   while low<high:
      #若相同，返回下标值
      if nums[mid]==value:
         return mid
      #中间元素大于目标值，序列为升序。
      elif nums[mid]>value:
         #将中间索引-1设置为最高索引，下次查找左边
         high = mid-1
         #减少一个区间
         block -= 1
      # 中间元素小于目标值，序列为升序。
      else:
         # 将中间索引+1设置为最低索引，下次查找右边
         low = mid+1
         #减少两个区间
         block -= 2
      #重新计算中间索引
      mid = low + f[block-1] - 1

# --- ❌ 漏找的测试用例 ---
miss_nums = [10, 20]
target = 20

result = fibonacciSearch(miss_nums, target)
print(f"查找结果: {result}")
# 预期输出: 1
# 实际输出: None (或者是 Python 默认的 None)


