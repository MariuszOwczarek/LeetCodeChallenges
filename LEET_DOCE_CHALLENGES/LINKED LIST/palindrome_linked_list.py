"""
Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Linkedpalindrome:
    @staticmethod
    def result(head):
        data = []
        current = head
        while current is not None:
            data.append(current.value)
            current = current.next

        if data == data[::-1]:
            return True
        return False


head = ListNode(1)
second = ListNode(2)
head.next = second
third = ListNode(2)
second.next = third
fourth = ListNode(1)
third.next = fourth

linked_list_palindrome = Linkedpalindrome.result(head)
print(linked_list_palindrome)
