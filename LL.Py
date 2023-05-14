class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def insert_after(self,value, after):
        new_node = Node(value)
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        # case 1:- break agar item milgya -> curr -> Not none

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1

        # case 2:- if item did not found
        else:
            return "item not found "

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):

        if self.head == None:
            return "empty linked list"
        else:
            self.head = self.head.next
            self.n -= 1

    def pop(self):

        if self.head == None:
            return print("Empty linked list! first insert node then delete\n")

        curr = self.head
        # agar linked list me sirf ek hi element ho?
        if curr.next == None:
            return self.delete_head()
        else:
            while curr.next.next != None:
                curr = curr.next

            # curr -> 2nd last node

            curr.next = None
            self.n -= 1

    def remove(self, value):
        if self.head == None:
            return print("empty linked list")


        if self.head.data == value:
            return self.delete_head()

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            # ab yha do cases honge agar
            # 1. agar item/node nahi mila
            return print("Item/Node not found")
        else:
            # 2. agar item/node milgya
            curr.next = curr.next.next
            self.n -= 1

    def search(self, item):

        curr = self.head
        pos = 0

        while curr != None:
            # after traverse we check if current data is similar to given data
            if curr.data == item:
                return print(f'position of given element is {pos}')
            curr = curr.next
            pos = pos + 1

        return print('Not found \n')

    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return print(f'Element in the given index is {curr.data}')
            curr = curr.next
            pos = pos + 1

            return print('indexError')



'''
All operations begins here
'''

ll = LinkedList()
ll.insert_head(1)
ll.insert_head(3)
ll.insert_head(10)
ll.insert_head(6)
ll.append(9)
ll.insert_after(3, 6)
ll.insert_after(11, 1)
# ll.clear()

# for i in range(0, 3):
#     ll.delete_head()

# for i in range(0, 8):
#     ll.pop()
# ll.remove(6)

# ll.search(11)
ll.__getitem__(1)

# Print the data in the linked list

curr = ll.head
while curr != None:
    print(curr.data)
    curr = curr.next

print(f'length of the linked list is {len(ll)}')

