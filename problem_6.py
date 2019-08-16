class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    dictionary = {}
    unionList = LinkedList()
    tempNode1 = llist_1.head
    tempNode2 = llist_2.head

    if tempNode1 is None and tempNode2 is None:
        return llist_1  # here we can return llist 2 as well

    if tempNode1 is None:
        return llist_2

    if tempNode2 is None:
        return llist_1

    while tempNode1 is not None:
        if tempNode1.value not in dictionary:
            dictionary[tempNode1.value] = tempNode1
        tempNode1 = tempNode1.next
    while tempNode2 is not None:
        if tempNode2.value not in dictionary:
            dictionary[tempNode2.value] = tempNode2
        tempNode2 = tempNode2.next
    for element in dictionary:
        unionList.append(element)
    return unionList


def intersection(llist_1, llist_2):
    dictionary = {}
    common_elements = {}
    intersection_list = LinkedList()
    temp_node1 = llist_1.head
    temp_node2 = llist_2.head

    if temp_node1 is None:
        return llist_1
    if temp_node2 is None:
        return llist_2

    while temp_node1 is not None:
        if temp_node1.value not in dictionary:
            dictionary[temp_node1.value] = temp_node1
        temp_node1 = temp_node1.next

    while temp_node2 is not None:
        if temp_node2.value in dictionary and temp_node2.value not in common_elements:
            common_elements[temp_node2.value] = temp_node2
        temp_node2 = temp_node2.next

    for element in common_elements:
        intersection_list.append(element)
    return intersection_list


if __name__ == "__main__":
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union of ", element_1, "&", element_2)
    print(union(linked_list_1, linked_list_2))
    print("Intersection", element_1, "&", element_2)
    print(intersection(linked_list_1, linked_list_2))

    # Results of Test case 1

    # Union
    # of[3, 2, 4, 35, 6, 65, 6, 4, 3, 21] & [6, 32, 4, 9, 6, 1, 11, 21, 1]
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    # Intersection[3, 2, 4, 35, 6, 65, 6, 4, 3, 21] & [6, 32, 4, 9, 6, 1, 11, 21, 1]
    # 6 -> 4 -> 21 ->

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Union", element_1, "&", element_2)
    print(union(linked_list_3, linked_list_4))
    print("Intersection", element_1, "&", element_2)
    print(intersection(linked_list_3, linked_list_4))

    # Result of Test case 2
    # Union[3, 2, 4, 35, 6, 65, 6, 4, 3, 23] & [1, 7, 8, 9, 11, 21, 1]
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    # Intersection[3, 2, 4, 35, 6, 65, 6, 4, 3, 23] & [1, 7, 8, 9, 11, 21, 1]

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 3, 23]
    element_2 = [1, 3, 2]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print("Union", element_1, "&", element_2)
    print(union(linked_list_5, linked_list_6))
    print("Intersection", element_1, "&", element_2)
    print(intersection(linked_list_5, linked_list_6))

    # Result of Test case 3
    # Union[3, 2, 4, 3, 23] & [1, 3, 2]
    # 3 -> 2 -> 4 -> 23 -> 1 ->
    # Intersection[3, 2, 4, 3, 23] & [1, 3, 2]
    # 3 -> 2 ->

    # Test case 4

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()
    element_1 = []
    element_2 = [1, 3, 2]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print("Union", element_1, "&", element_2)
    print(union(linked_list_7, linked_list_8))
    print("Intersection", element_1, "&", element_2)
    print(intersection(linked_list_7, linked_list_8))

    # Result of Test case 4
    # Union [] & [1, 3, 2]
    # 1 -> 3 -> 2 ->
    # Intersection [] & [1, 3, 2]

    # Test case 5

    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()
    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_9.append(i)

    for i in element_2:
        linked_list_10.append(i)

    print("Union", element_1, "&", element_2)
    print(union(linked_list_9, linked_list_10))
    print("Intersection", element_1, "&", element_2)
    print(intersection(linked_list_9, linked_list_10))

    # Result of Test case 5
    # Union[] & []
    #
    # Intersection[] & []

