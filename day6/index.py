'''
朴素算法
'''

def index(src, dst):
    # 获取源字符串和目标字符串的长度
    src_len = len(src)
    dst_len = len(dst)
    # 遍历下标到m - n + 1, m - n + 1是为了防止越界
    for i in range(src_len - dst_len + 1):
        # 若相同
        if src[i:i + dst_len] == dst:
            return i
    return -1

# 测试代码
source_string = "ababcabcacbab"
target_string = "abcac"
result = index(source_string, target_string)
print(f"目标字符串在源字符串中的索引位置为: {result}")