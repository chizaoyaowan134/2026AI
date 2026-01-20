# '''
# 基数排序
# '''
#
# def radix_sort(nums):
#     # 获取最大长度
#     max_len = len(str(max(nums)))
#     # 创建嵌套列表作为队列
#     queues = [[] for _ in range(10)]
#     # 根据最大长度遍历轮数
#     for x in range(1, max_len + 1):
#         for num in nums:
#         # 获取每个数字的对应位数，并放入对应队列
#         #str(num)将数字转换为字符串，zfill(max_len)在左侧填充0以确保长度一致
#         #str(num)[-i]获取从右往左第i位的字符，int(...)将其转换为整数索引
#             try:
#                 queueIndex = int(str(num)[-x])
#             # 若抛出异常，说明该位数不存在，放入0号队列
#             except IndexError:
#                 queueIndex = 0
#             #将数字放入对应队列
#             queues[queueIndex].append(num)
#         # 重置nums列表
#         nums.clear()
#         # 遍历队列，依次取出数字放入nums列表
#         for queue in queues:
#             nums.extend(queue)
#             # 清空队列，准备下一轮使用
#             queue.clear()
#
#
# # 待排序列表
# nums = [170, 45, 75, 90, 802, 242, 66]
# # 调用基数排序函数
# radix_sort(nums)
# # 输出排序结果
# print(nums)

#
# def radix_sort(nums):
#     # 1. 找到最大值，确定需要排序的轮数
#     max_num = max(nums)
#
#     # 2. 初始位置：从个位开始（it=1表示个位，10表示十位，100表示百位...）
#     it = 1
#
#     # 当最大值除以当前位依然大于0，说明还没处理完所有位数
#     while it <= max_num:
#         # 3. 创建 10 个桶（队列）
#         queues = [[] for _ in range(10)]
#
#         # 4. 遍历数字，计算当前位的数字（核心数学逻辑）
#         for num in nums:
#             # 公式：(num // it) % 10
#             # 举例：num=802, it=10(十位) -> (802 // 10) % 10 = 80 % 10 = 0
#             digit = (num // it) % 10
#             queues[digit].append(num)
#
#         # 5. 回收数据：将桶里的数字放回原列表
#         nums.clear()
#         for queue in queues:
#             nums.extend(queue)
#
#         # 6. 进位：准备处理下一位（个位变十位，十位变百位...）
#         it *= 10
#
#
# # 测试代码
# nums = [170, 45, 75, 90, 802, 242, 66]
# radix_sort(nums)
# print(f"排序结果：{nums}")


import time
import random

# --- 方法 1：字符串转换法 ---
def radix_sort_str(nums_orig):
    nums = nums_orig.copy() # 为了公平，复制一份避免修改原数据
    max_len = len(str(max(nums)))
    for x in range(1, max_len + 1):
        queues = [[] for _ in range(10)]
        for num in nums:
            try:
                queueIndex = int(str(num)[-x])
            except IndexError:
                queueIndex = 0
            queues[queueIndex].append(num)
        nums.clear()
        for queue in queues:
            nums.extend(queue)
    return nums

# --- 方法 2：数学取模法 ---
def radix_sort_math(nums_orig):
    nums = nums_orig.copy()
    max_num = max(nums)
    it = 1
    while it <= max_num:
        queues = [[] for _ in range(10)]
        for num in nums:
            digit = (num // it) % 10
            queues[digit].append(num)
        nums.clear()
        for queue in queues:
            nums.extend(queue)
        it *= 10
    return nums

# --- 测试准备 ---
# 生成 100,000 个 0 到 1,000,000 之间的随机整数
test_data = [random.randint(0, 1000000) for _ in range(100000)]

print(f"数据量: {len(test_data)} 条\n" + "-"*30)

# 测试字符串法速度
start = time.time()
radix_sort_str(test_data)
end = time.time()
print(f"字符串法用时: {end - start:.4f} 秒")

# 测试数学法速度
start = time.time()
radix_sort_math(test_data)
end = time.time()
print(f"数学取模法用时: {end - start:.4f} 秒")