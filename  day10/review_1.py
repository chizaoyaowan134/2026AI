def search(head, target):
    # 1. 边界条件防御：如果是空链表，直接返回
    if not head:
        return None

    current = head

    while current:
        if current.val == target:
            return current
        current = current.next

    return None


# --- 测试代码 ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 创建链表: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
target = 3
result_node = search(head, target)
if result_node:
    print(f"找到了节点，值为: {result_node.val}")  # 预期输出: 3
else:
    print("未找到目标节点")
