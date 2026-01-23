# def index(src, dst):
#     # 获取源字符串和目标字符串的长度
#
#     src_len = len(src)
#     dst_len = len(dst)
#
#     for i in range(src_len - dst_len + 1):
#
#         if src[i:i + dst_len] == dst:
#             return i
#
#     return -1
#
# # 测试代码
# source_string = "ababcabcacbab"
# target_string = "abcac"
# result = index(source_string, target_string)
# print(f"目标字符串在源字符串中的索引位置为: {result}")


def kmp(src, dst):

    if not dst: return 0

    steps = getSteps(dst)

    n = len(src)
    m = len(dst)

    i, j = 0, 0

    while (i < n) and (j < m):

        if src[i] == dst[j]:
            i += 1
            j += 1

        elif j != 0:
            j = steps[j - 1]

        else:
            i += 1


    if j == m:
        return  i - j

    else:
        return -1

def getSteps(dst):
    m = len(dst)
    index = 0
    steps = [0] * m

    for i in range(1, m):

        while (index > 0) and (dst[i] != dst[index]):
            index = steps[index - 1]

        if (dst[i] == dst[index]):
            index += 1

        steps[i] = index

    return steps

# --- 测试环节 ---

# 测试 1: 应该找不到
# 你的逻辑跑出来也是 -1，正确。
print("测试1:", kmp('byte bye-by bye-bye', 'bye-byt'))

# 测试 2: 之前会让程序变傻的“必死案例”
# 'abaabc' 的 steps 表应该是 [0, 0, 1, 1, 2, 0]
# 你的新代码现在能正确处理连续回退，能算出 2 (在索引2的位置找到)
print("测试2:", kmp('ababaabc', 'abaabc'))
