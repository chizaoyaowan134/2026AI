'''
调整某一棵子树的最大顶堆
parent需要调整为大顶堆的父节点索引
'''

def maxHeap(nums, size, parent):
    # 获取parent节点的左子节点
    leftChild = 2 * parent + 1
    # 获取parent节点的右子节点
    rightChild = 2 * parent + 2
    # 先假设parent节点是最大的节点
    largest = parent
    # 如果左子节点存在，且左子节点的值大于parent节点的值
    if leftChild < size and nums[leftChild] > nums[largest]:
        largest = leftChild
    # 如果右子节点存在，且右子节点的值大于目前最大的节点
    if rightChild < size and nums[rightChild] > nums[largest]:
        largest = rightChild
    # 如果最大的节点不是parent节点，则交换，并递归调整
    if largest != parent:
        temp = nums[parent]
        nums[parent] = nums[largest]
        nums[largest] = temp
        maxHeap(nums, size, largest)


'''
堆排序算法
'''
def heapSort(nums):
    last = len(nums) - 1
    # 获取最后一个非叶子节点
    parent = last // 2 - 1 if last % 2 == 0 else last // 2
    # 从最后一个父节点向前依次调整
    while parent >= 0:
        maxHeap(nums, len(nums), parent)
        parent -= 1
    # 遍历区间，i是最后一个节点的索引，每次将堆顶元素与最后一个元素交换，然后调整堆
    i = last
    while i > 0:
        # 交换堆顶元素和最后一个元素
        temp = nums[0]
        nums[0] = nums[i]
        nums[i] = temp
        # 调整堆
        maxHeap(nums, i, 0)
        i -= 1


# 待排序列表
nums = [7, 6, 3, 9, 1, 8]
print("排序前：", nums)
heapSort(nums)
print("排序后：", nums)