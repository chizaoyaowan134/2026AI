import time
import sys


# 1. 线性查找
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. 二分查找
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- 测试准备 ---
# 创建一个有序的大数组（1000万个数据）
data_size = 10_000_000
sorted_list = list(range(data_size))

print(f"数据量: {data_size}")
print("-" * 30)

# ==========================================
# 测试场景 1：目标在索引 0 (最前面)
# ==========================================
target_first = 0
print(f"场景 1：查找目标 {target_first} (位于最前面)")

# 测试线性查找
start = time.perf_counter()
linear_search(sorted_list, target_first)
end = time.perf_counter()
print(f"  > 线性查找耗时: {end - start:.9f} 秒 ✅ 胜出")

# 测试二分查找
start = time.perf_counter()
binary_search(sorted_list, target_first)
end = time.perf_counter()
print(f"  > 二分查找耗时: {end - start:.9f} 秒")

print("-" * 30)

# ==========================================
# 测试场景 2：目标在索引 9999999 (最后面)
# ==========================================
target_last = data_size - 1
print(f"场景 2：查找目标 {target_last} (位于最后面)")

# 测试线性查找
start = time.perf_counter()
linear_search(sorted_list, target_last)
end = time.perf_counter()
print(f"  > 线性查找耗时: {end - start:.9f} 秒")

# 测试二分查找
start = time.perf_counter()
binary_search(sorted_list, target_last)
end = time.perf_counter()
print(f"  > 二分查找耗时: {end - start:.9f} 秒 ✅ 胜出")