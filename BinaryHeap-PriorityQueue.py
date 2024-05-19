import matplotlib.pyplot as plt
import random 
import tqdm
import math



class PriorityQueue:
    def __init__(self):
        self.heap = []  # Initialize an empty heap
        self.counter = 0 # Initialize a counter to count operations

    def insert(self, item, priority):
        """
        Insert an item with its priority into the heap and maintain the heap property.
        """
        self.counter = 0
        self.heap.append((priority, item))
        self._sift_up(len(self.heap)-1)
        return self.counter

    def delete(self):
        """
        Remove and return the item with the highest priority from the heap, maintaining the heap property.
        """
        self.counter = 0
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sift_down(0)
        return item, self.counter

    def peek(self):
        """
        Return the item with the highest priority from the heap without removing it.
        """
        return self.heap[0] [1]

    def is_empty(self):
        """
        Check if the heap is empty and return True if it is, False otherwise.
        """
        return not self.heap
        
               
    def size(self):
        """
        Return the current number of items in the heap.
        """
        return len(self.heap)

    def change_priority(self, item, new_priority):
        """
        Change the priority of a specific item in the heap and adjust its position accordingly.
        """
        for i in range(len(self.heap)): 
            if item == self.heap[i] [0]:
                old_priority = self.heap[i] [1]
                self.heap[i] = (item, new_priority)
                if old_priority > new_priority:
                    self._sift_down(i)
                else:
                    self._sift_up(i)
                return 'Done'     
        return "not found"

    def _sift_up(self, i):
        """
        Move the element at index i upwards in the heap until it reaches its proper position.
        """
        self.counter += 1
        parent_index = (i - 1) //2
        while i > 0 and self.heap[parent_index] < self.heap[i]:
            self.heap[parent_index], self.heap[i] = self.heap[i], self.heap[parent_index]
            i = parent_index
            parent_index = (i-1)//2
            self.counter += 1


    def _sift_down(self, i):
        """
        Move the element at index i downwards in the heap until it reaches its proper position.
        """
        child_index = 2 * i + 1
        while child_index < len(self.heap):
            right_child = child_index + 1
            if right_child < len(self.heap):
                self.counter += 1
                if self.heap[right_child][0] > self.heap[child_index][0]:
                    child_index = right_child
            
            self.counter += 1
            if self.heap[i][0] >= self.heap[child_index][0]:
                break

            self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]
            i = child_index
            child_index = 2 * i + 1
        return self.counter
        
        
def test_priority_queue(debug=False):
    # Create an instance of the PriorityQueue class
    pq = PriorityQueue()

    # Generate random items with priorities and insert them into the priority queue
    items_priority = []
    for _ in range(10):
        item = chr(random.randint(65, 90))
        priority = random.randint(1, 100)
        items_priority.append(priority)
        pq.insert(item, priority)

    # Sort the items in descending order based on priority
    items_priority.sort(reverse=True)
    if debug:
        print(items_priority)

    # Check if the item received by delete is indeed the highest priority item in the queue
    for priority in items_priority:
        highest_priority = pq.delete()[0][0]
        if debug:
            print(highest_priority)
        else:
            assert highest_priority == priority, "Incorrect item received by delete."
    if not debug:
        print("All tests passed successfully!")


# Function to measure the time complexity for insertion and deletion operations
def time_complexity(pq, num_elements):
    insertion_times = {}
    deletion_times = {}

    # Measure insertion complexity
    
    for i in tqdm.trange(num_elements):
        size = pq.size()
        priority = random.randint(0,size)
        count = pq.insert(i, priority) 
        insertion_times[size] = count

    # Measure deletion complexity
    for i in tqdm.trange(num_elements):
        size = pq.size()
        _, count = pq.delete() 
        deletion_times[size] = count

    return insertion_times, deletion_times


def plot_performance(num_elements=1_000_000):
    # Testing the Priority Queue implementation
    pq = PriorityQueue()

    insertion_times, deletion_times = time_complexity(pq, num_elements)

    # Plotting the time for insertion and deletion
    x = list(range(1, num_elements + 1))
    y = [math.log2(i) for i in x]

    plt.plot(insertion_times.keys(), insertion_times.values(), label='Insertion')
    plt.plot(deletion_times.keys(), deletion_times.values(), label='Deletion')
    plt.plot(x, y, label='LOG(x)')
    plt.xlabel('Number of Elements')
    plt.ylabel('Running Time')
    plt.title('Priority Queue Insertion and Deletion Complexity')
    plt.legend()
    plt.show()

# test_priority_queue()
# plot_performance()

a = PriorityQueue()
a.insert(1, "hi")
print(a.change_priority("hi", 2))
print(a.heap)


