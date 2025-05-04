class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1, l2):
        # Initialize a dummy node to simplify the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0 


        # Pointers for l1 and l2
        p1 = l1
        p2 = l2

        while p1 is not None or p2 is not None:
            # Get the values from the nodes or 0 if we've reached the end
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit

            # Move to the next nodes
            current = current.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next

        # If there's any carry left, add a new node
        if carry > 0:
            current.next = ListNode(carry)

        # The result is in the next of the dummy head
        return dummy_head.next
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    print(addTwoNumbers)




