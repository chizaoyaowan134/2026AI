def shell_sort(nums):

    # 初始步长
    step = len(nums) // 2

    while step > 0:

        for i in range(step, len(nums)):

            #记录当前元素
            current = nums[i]

            # 从本组中的前一个位置开始比较，下表为i - step
            j = i - step
            # 遍历本组中前面的所有元素，若本组中前面的元素大于current，则将其后移
            while j >= 0 and nums[j] > current:
                nums[j + step] = nums[j]
                j -= step

            nums[j + step] = current

        step //= 2



# --- 测试代码 ---
import random
# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
shell_sort(data)
print(f"排序结果: {data}")


