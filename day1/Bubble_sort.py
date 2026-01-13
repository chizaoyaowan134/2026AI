'''
这是最开始的版本
'''
# def bubble_sort(nums):
#     for i in range(0, len(nums) - 1):
#         for j in range(0, len(nums) - 1 - i):
#             if nums[j] > nums[j + 1]:
#                 temp = nums[j]
#                 nums[j] = nums[j + 1]
#                 nums[j + 1] = temp
#
#
# 排序前的列表
# nums = [7, 6, 3, 9, 1, 8]
# print("排序前：", nums)
# # bubble_sort(nums)
# print("排序后：", nums)

# def bubble_sort(nums):
#     for i in range(0, len(nums) - 1):
#         for j in range(0, len(nums) - 1 - i):
#             print("第%d轮第%d次"%(i + 1, j + 1), end="\t")
#             if nums[j] > nums[j + 1]:
#                 print("%d和%d交换位置"%(nums[j], nums[j + 1]), end="")
#                 temp = nums[j]
#                 nums[j] = nums[j + 1]
#                 nums[j + 1] = temp
#             else:
#                 print("%d比%d小,不交换位置"%(nums[j], nums[j + 1]), end="")
#             print(nums)
#         print("第%d轮排序结果："%(i + 1), nums)

# # 排序前的列表
# nums = [7, 6, 3, 9, 1, 8]
# print("排序前：", nums)
# bubble_sort(nums)
# print("排序后：", nums)


'''
冒泡排序算法优化_1
'''


# def bubble_sort(nums):
#     for i in range(0, len(nums) - 1):
#         sortes = True
#         for j in range(0, len(nums) - 1 - i):
#             print("第%d轮第%d次"%(i + 1, j + 1), end="\t")
#             if nums[j] > nums[j + 1]:
#                 print("%d和%d交换位置"%(nums[j], nums[j + 1]), end="")
#                 temp = nums[j]
#                 nums[j] = nums[j + 1]
#                 nums[j + 1] = temp
#                 sortes = False
#             else:
#                 print("%d比%d小,不交换位置"%(nums[j], nums[j + 1]), end="")
#             print(nums)
#         print("第%d轮排序结果："%(i + 1), nums)
#         if sortes:
#             return

# 排序前的列表
nums = [6, 1, 2, 3, 4, 5]
print("排序前：", nums)
# bubble_sort(nums)
print("排序后：", nums)




def bubble_sort(nums):
    r = range(0, len(nums) - 1)
    for i in range(0, len(nums) - 1):
        sortes = True
        for j in r:
            print("第%d轮第%d次"%(i + 1, j + 1), end="\t")
            if nums[j] > nums[j + 1]:
                print("%d和%d交换位置"%(nums[j], nums[j + 1]), end="")
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                sortes = False
                #记录下最后一次交换的位置
                lastChange = j
            else:
                print("%d比%d小,不交换位置"%(nums[j], nums[j + 1]), end="")
            print(nums)
        print("第%d轮排序结果："%(i + 1), nums)
        if sortes:
            return
        print("最后是交换位置是：", lastChange)
        #改变下一轮比较的范围
        r = range(0, lastChange)

nums = [6, 1, 2, 3, 4, 5]
print("排序前：", nums)
bubble_sort(nums)
print("排序后：", nums)



