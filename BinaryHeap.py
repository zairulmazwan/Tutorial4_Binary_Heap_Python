class Heap:

    def __init__(self,n):
        self.MAX_SIZE = n
        self.heap = [0]*self.MAX_SIZE
        self.size = 0


    def get_index_of(self,value):
        return self.heap.index(value)

    # return the index of the node.
    def get_parent(self, index):
        res = (index-1)//2
        return res

    def get_left_child(self, index):
        res = (2*index) + 1
        return res

    def get_right_child(self, index):
        res = (2*index) + 2
        return res

    def insert(self, value):
        if self.size >= self.MAX_SIZE:
            print(f"The binary heap tree is full!, {value} cannot be inserted.")
            return

        self.heap[self.size] = value
        self.size += 1

        index = self.size-1
        while index != 0 and self.heap[index] > self.heap[self.get_parent(index)]:
            temp = self.heap[index]
            self.heap[index] = self.heap[self.get_parent(index)]
            self.heap[self.get_parent(index)] = temp
            index = self.get_parent(index)


    def insert_min(self, value):
        if self.size >= self.MAX_SIZE:
            print(f"The binary heap tree is full!, {value} cannot be inserted.")
            return

        self.heap[self.size] = value
        self.size += 1

        index = self.size-1
        while index != 0 and self.heap[index] < self.heap[self.get_parent(index)]:
            temp = self.heap[index]
            self.heap[index] = self.heap[self.get_parent(index)]
            self.heap[self.get_parent(index)] = temp
            index = self.get_parent(index)


    def max_heapify(self, index):

        left_index = self.get_left_child(index)
        right_index = self.get_right_child(index)

        largest_index = index

        if (left_index <= self.size and self.heap[left_index] > self.heap[largest_index]):
            largest_index = left_index

        if (right_index <= self.size and self.heap[right_index] > self.heap[largest_index]):
            largest_index = right_index

        if largest_index != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest_index]
            self.heap[largest_index] = temp
            self.max_heapify(largest_index)


    def min_heapify(self, index):

        left_index = self.get_left_child(index)
        right_index = self.get_right_child(index)

        min_index = index

        if (left_index <= self.size and self.heap[left_index] < self.heap[min_index]):
            min_index = left_index

        if (right_index <= self.size and self.heap[right_index] < self.heap[min_index]):
            min_index = right_index

        if min_index != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[min_index]
            self.heap[min_index] = temp
            self.min_heapify(min_index)


    def delete_node(self, index):

        self.heap[index] = self.heap[self.size-1]
        self.size -= 1
        self.max_heapify(index)


    def delete_node_min(self, index):

        self.heap[index] = self.heap[self.size-1]
        self.size -= 1
        self.min_heapify(index)


    def descending_order(self):
        heap_data = self.copy_heap()
        res = [0]*self.size

        resize = len(res)
        index = 0
        while index<resize:
            res[index] = self.heap[0]
            self.delete_node(0)
            index+=1

        return res


    def ascending_order(self):

        res = [0] * self.size

        resize = len(res)
        index = 0
        while index < resize:
            res[index] = self.heap[0]
            self.delete_node_min(0)
            index += 1

        return res

    def create_heap_tree(self, data):
        for i in data:
            self.insert(i)


    def create_min_heap(self,data):
        for i in data:
            self.insert_min(i)

    # This function is not used in this program
    def copy_heap(self):
        res = [self.heap[:]]
        return res

    def print_heap(self):
        for i in self.heap:
            print(i, end=" ")


    def print_list(self, data):
        for i in data:
            print(i, end=" ")


data = [47,57,23,43,31,29,17]

heap_tree = Heap(len(data))
heap_tree.create_heap_tree(data)
heap_tree.print_heap()
sorted  = heap_tree.descending_order()
print("\nDescending order")
heap_tree.print_list(sorted)

print("\n\nMinimum Heap Tree")
min_heap = Heap(len(data))
min_heap.create_min_heap(data)
print("\nBinary Heap Min is: ")
min_heap.print_heap()

print("\nAscending order")
asc = min_heap.ascending_order()
min_heap.print_list(asc)
min_heap.delete_node_min(2)



