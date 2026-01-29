def kmp(src, dst):
    # 防御性编程，如果目标串是空的，没法找，直接返回0
    if not dst:
        return 0

    steps = getSteps(dst)

    n = len(src)
    m = len(dst)

    # i：文章读到第几个字了
    # j：搜索词匹配到第几个字了
    i, j = 0, 0

    while (i < n) and (j < m):
        # 情况A：匹配成功
        if (src[i] == dst[j]):
            i += 1      # 文章看下一个字
            j += 1      # 搜索词进度条 +1

        # 情况B：中途匹配失败
        # 字不一样了，而且j不是0
        elif (j != 0):
            j = steps[j - 1]

        else:
            i += 1

    if (j == m):
        return i - j

    else:
        return -1


def getSteps(dst):

    m = len(dst)
    index = 0
    steps = [0] * m


    #i 是探索者，从第2个字符（下标1）开始往后跑
    # 为什么要从1开始？因为第0个字符没有前缀，肯定是0
    for i in range(1, m):

        # 如果index > 0 (说明前面有匹配好的前缀)
        # 并且dst[i]（探索者的新字符）!= dst[index]（前缀期待的字符）

        while(index > 0) and (dst[i] != dst[index]):

            index = steps[index - 1]


        if(dst[i] == dst[index]):
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
# 测试 3: 正常案例
print("测试3:", kmp('hello world', 'world'))
# 测试 4: 重复字符
print("测试4:", kmp('aaaaaa', 'aaa'))
# 测试 5: 找不到
print("测试5:", kmp('abcdefg', 'hij'))