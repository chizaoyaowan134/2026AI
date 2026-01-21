class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_max_in_circular_list(head):
    """
    在循环单链表中查找最大值
    """
    # 1. 处理空链表
    if head is None:
        return None

    # 2. 初始化
    # 假设第一个节点是最大的
    max_val = head.value
    # 从第二个节点开始遍历
    current = head.next

    # 3. 循环遍历
    # 终止条件：当 current 再次指向 head 时，说明绕了一圈
    while current != head:
        if current.value > max_val:
            max_val = current.value
        # 指针后移
        current = current.next

    return max_val


# --- 测试代码 ---
if __name__ == "__main__":
    # 1. 创建节点
    n1 = Node(10)
    n2 = Node(50)
    n3 = Node(20)
    n4 = Node(99)
    n5 = Node(5)

    # 2. 构建引用关系
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1  # 【关键】尾节点指向头节点，形成闭环

    # 3. 调用算法
    # 传入任意一个节点作为入口（通常是头节点）
    max_value = find_max_in_circular_list(n1)

    print(f"链表中的最大值是: {max_value}")

    # 如果要找最小值，逻辑完全一样，把 > 改成 < 即可