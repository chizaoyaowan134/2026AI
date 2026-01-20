'''
归并操作
'''

def merge(left, right):
    # 记录下标
    r, l = 0, 0
    #新列表
    temp = []
    # 当左右列表都有元素时，比较后放入新列表
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            temp.append(left[l])
            l += 1
        else:
            temp.append(right[r])
            r += 1
    # 将左列表剩余元素放入新列表
    temp += left[l:]
    # 将右列表剩余元素放入新列表
    temp += right[r:]
    return temp

'''
归并排序
'''
def merge_sort(nums):
    # 如果列表长度小于等于1，说明已经有序，直接返回
    if len(nums) <= 1:
        return nums
    # 获取中间索引
    mid = len(nums) // 2
    # 递归排序左半部分和右半部分
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    # 合并两个有序部分
    return merge(left, right)


# 待排序列表
nums = [7, 6, 3, 9, 1, 8]
print("排序前：", nums)
sorted_nums = merge_sort(nums)
print("排序后：", sorted_nums)