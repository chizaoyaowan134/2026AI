def maxHeap(nums, size, parent):

    leftChild = 2 * parent + 1
    rightChild = 2 * parent + 2

    largest = parent

    if leftChild < size and nums[leftChild] > nums[largest]:
        largest = leftChild

    if rightChild < size and nums[rightChild] > nums[largest]:
        largest = rightChild

    if largest != parent:
        temp = nums[parent]
        nums[parent] = nums[largest]
        nums[largest] = temp
        maxHeap(nums, size, largest)


def heapSort(nums):
    last = len(nums) - 1

    parent = last // 2 - 1 if last % 2 == 0 else last // 2

    while parent >= 0:
        maxHeap(nums, len(nums), parent)

        parent -= 1

    #遍历区间：i是最后一个节点的索引，每次将堆顶元素与最后一个元素交换
    i = last
    while i > 0:
        temp = nums[0]
        nums[0] = nums[i]
        nums[i] = temp
        maxHeap(nums, i, 0)
        i -= 1


# --- 测试代码 ---
import random
# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
heapSort(data)
print(f"排序结果: {data}")


