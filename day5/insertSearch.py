def interpolation_search(nums, target):
    low = 0
    high = len(nums) - 1

    # ⚠️ 关键区别 1: 循环条件必须加上数值范围判断
    # 为什么？因为如果 target 很大（比如 10000），套用公式算出来的 mid 会直接越界
    # 同时这也避免了 nums[high] == nums[low] 导致的除以零错误
    while low <= high and nums[low] <= target <= nums[high]:

        # 优化：如果只剩一个数，或者头尾相等，直接判断
        if low == high:
            if nums[low] == target:
                return low
            return -1

        # ⚠️ 关键区别 2: 使用插值公式计算 mid
        # 注意要用 int() 取整
        pos = low + int((high - low) * (target - nums[low]) / (nums[high] - nums[low]))

        # 下面的逻辑和二分查找一模一样
        if nums[pos] == target:
            return pos
        elif nums[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# --- 测试代码 ---
# 插值查找最适合这种“均匀分布”的数组
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 30

index = interpolation_search(my_list, target)
print(f"找到目标，索引为: {index}")