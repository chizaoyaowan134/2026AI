def kmp(src, dst):
    # 如果目标串为空，返回0
    if not dst: return 0
    
    steps = getSteps(dst)
    n = len(src)
    m = len(dst)
    i, j = 0, 0
    
    while (i < n) and (j < m):
        if (src[i] == dst[j]):
            i += 1
            j += 1
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
    
    # 从第1个字符开始向后遍历
    for i in range(1, m):
        # 【核心修改】使用 while 处理连续回退
        # 只要不匹配且 index > 0，就一直往前回溯
        while (index > 0) and (dst[i] != dst[index]):
            index = steps[index - 1]
            
        # 回退完了，再看现在匹配不匹配
        if (dst[i] == dst[index]):
            index += 1
            
        steps[i] = index
        
    return steps

# 测试
print(kmp('byte bye-by bye-bye', 'bye-byt')) # 正确输出 -1
print(kmp('ababaabc', 'abaabc'))             # 之前会出错的例子，现在正确输出 2