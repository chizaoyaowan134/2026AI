def merge(left, right):

    r, l = 0, 0
    temp = []

    # 当左右列表都有元素时，比较后放入新列表
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:

            temp.append(left[l])
            l += 1

        else:
            temp.append(right[r])
            r += 1

    # 将左列表剩余原酸放入新列表
    temp += left[l:]
    # 将右列表剩余元素放入新列表
    temp += right[r:]
    return temp


def merge_sort(nums):
    # 如果列表长度小于等于1，说明已经有序，直接返回
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


# --- 测试代码 ---
import random
# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
sorted_data = merge_sort(data)
print(f"排序结果: {sorted_data}")






