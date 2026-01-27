def radix_sort(nums):

    # 获取最大长度
    max_len = len(str(max(nums)))
    # 创建嵌套列表作为队列
    queues = [[] for _ in range(10)]

    # 根据最大长度遍历轮数
    for x in range(1, max_len + 1):

        for num in nums:

            try:
                queueIndex = int(str(num)[-x])
            except IndexError:
                queueIndex = 0

            queues[queueIndex].append(num)

        nums.clear()

        for queue in queues:
            nums.extend(queue)
            queue.clear()



# --- 测试代码 ---
import random
# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
radix_sort(data)
print(f"排序结果: {data}")