def Cycle(self, head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
print(Cycle(list(map(int, input().split()))))

#OR print(Cycle([3,2,1,-4]))