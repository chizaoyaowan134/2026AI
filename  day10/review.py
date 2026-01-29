'''
写出循环单列表中查找出最大值（或最小值）的算法
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def find_max_in_circular_list(head):

        if head is None:
            return None


        # 假设第一个节点时最大的
        max_val = head.value
        current = head.next

        # 终止条件：当current再次指向Head时，说明绕了一圈
        while current != head:
            if current.value > max_val:
                max_val = current.value
            current = current.next

        return max_val


# --- 测试代码 ---
# 创建循环单列表: 3 -> 5 -> 2 -> 8 -> 1 -> back to head (3)
head = Node(3)
node2 = Node(5)
node3 = Node(2)
node4 = Node(8)
node5 = Node(1)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = head  # 形成循环
max_value = Node.find_max_in_circular_list(head)
print(f"循环单列表中的最大值是: {max_value}")  # 预
# 期输出: 8