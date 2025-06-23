# Exercises: Data Structures and Algorithms in Python

This file contains a series of exercises to practice the concepts covered in the lecture. The problems start simple and build up to a final project that integrates multiple skills.

## Topic-by-Topic Exercises

_These are focused exercises designed to test your understanding of a single topic at a time._

---

### Exercise 1: Arrays (Python Lists)
*   **Scenario:** You are building a custom data analytics library and need a foundational dynamic array structure to build upon, without relying on Python's built-in list methods directly for resizing.
*   **Task:** Implement a `DynamicArray` class that internally uses a fixed-size list (or a similar static structure) and handles resizing automatically when it becomes full.
*   **Requirements:**
    *   The class should have `append(value)` and `get(index)` methods.
    *   When an `append` call would exceed the internal array's capacity, the array should be resized (e.g., doubled in size).
*   **Test Case:**
    *   **Input:**
        1. Create a `DynamicArray` with an initial capacity of 2.
        2. `append(10)`
        3. `append(20)`
        4. `append(30)`
        5. `get(2)`
    *   **Expected Output:** The `get(2)` call should return `30`. The internal capacity should now be 4.

### Exercise 2: Arrays (Python Lists)
*   **Scenario:** You are a junior financial analyst, and your first task is to analyze historical stock price data to find the best single-day trading opportunity.
*   **Task:** Write a function `max_profit(prices)` that takes a list of stock prices for consecutive days and returns the maximum profit that could have been made by buying on one day and selling on a later day.
*   **Requirements:**
    *   The function must take a list of integers (`prices`).
    *   You must complete the task in a single pass (O(n) time complexity).
    *   If no profit can be made, the function should return 0.
*   **Test Case:**
    *   **Input:** `max_profit([7, 1, 5, 3, 6, 4])`
    *   **Expected Output:** `5` (Buy at 1, sell at 6)

### Exercise 3: Arrays (Python Lists)
*   **Scenario:** You are working on an image processing application. One of the required features is the ability to rotate an image represented as a 2D matrix by 90 degrees clockwise.
*   **Task:** Write a function `rotate_matrix(matrix)` that rotates an N x N 2D matrix (represented as a list of lists) by 90 degrees clockwise. The rotation must be done in-place.
*   **Requirements:**
    *   The function must modify the matrix directly without creating a new one.
    *   The matrix will always be square (N x N).
*   **Test Case:**
    *   **Input:** `rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`
    *   **Expected Output:** The input matrix is modified to become `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`.

---

### Exercise 4: Stack
*   **Scenario:** You need to implement a basic stack data structure from scratch to understand its LIFO (Last-In, First-Out) behavior.
*   **Task:** Create a `Stack` class using a Python list as the underlying storage.
*   **Requirements:**
    *   Implement the following methods:
        *   `push(item)`: Adds an item to the top of the stack.
        *   `pop()`: Removes and returns the top item. Raises an error if the stack is empty.
        *   `peek()`: Returns the top item without removing it.
        *   `is_empty()`: Returns `True` if the stack is empty, `False` otherwise.
*   **Test Case:**
    *   **Input:**
        1. `s = Stack()`
        2. `s.push(1)`
        3. `s.push(2)`
        4. `s.peek()` returns `2`
        5. `s.pop()` returns `2`
        6. `s.pop()` returns `1`
        7. `s.is_empty()` returns `True`
    *   **Expected Output:** The sequence of operations should yield the specified return values.

### Exercise 5: Stack
*   **Scenario:** You are writing a utility for a command-line interface that needs to handle file paths. You need to simplify a given absolute path by resolving `.` (current directory) and `..` (parent directory).
*   **Task:** Write a function `simplify_path(path)` that takes a Unix-style absolute path string and returns the simplified canonical path.
*   **Requirements:**
    *   Use a stack to keep track of the directory names.
    *   `/../` should resolve to `/`.
    *   Multiple slashes `//` should be treated as a single slash.
*   **Test Case:**
    *   **Input:** `simplify_path("/a/./b/../../c/")`
    *   **Expected Output:** `"/c"`

### Exercise 6: Stack
*   **Scenario:** You are building a specialized data analysis tool that needs to quickly retrieve the minimum value in a collection, even as new values are added and removed.
*   **Task:** Design a `MinStack` class that supports `push`, `pop`, `peek`, and a new method `get_min` which returns the minimum element in the stack.
*   **Requirements:**
    *   All methods, including `get_min`, must operate in constant time, O(1).
    *   You will likely need to use an auxiliary stack to keep track of the minimums.
*   **Test Case:**
    *   **Input:**
        1. `ms = MinStack()`
        2. `ms.push(-2)`
        3. `ms.push(0)`
        4. `ms.push(-3)`
        5. `ms.get_min()` returns `-3`
        6. `ms.pop()`
        7. `ms.get_min()` returns `-2`
    *   **Expected Output:** The `get_min` calls should return the specified values.

---

### Exercise 7: Queue
*   **Scenario:** As a foundational exercise, you need to implement the Queue data structure to understand its FIFO (First-In, First-Out) properties.
*   **Task:** Create a `Queue` class. You can use `collections.deque` for an efficient implementation.
*   **Requirements:**
    *   Implement the following methods:
        *   `enqueue(item)`: Adds an item to the end of the queue.
        *   `dequeue()`: Removes and returns the item from the front of the queue. Raises an error if empty.
        *   `peek()`: Returns the front item without removing it.
        *   `is_empty()`: Returns `True` if the queue is empty.
*   **Test Case:**
    *   **Input:**
        1. `q = Queue()`
        2. `q.enqueue('A')`
        3. `q.enqueue('B')`
        4. `q.peek()` returns `'A'`
        5. `q.dequeue()` returns `'A'`
        6. `q.dequeue()` returns `'B'`
        7. `q.is_empty()` returns `True`
    *   **Expected Output:** The sequence of operations should yield the specified return values.

### Exercise 8: Queue
*   **Scenario:** You're tasked with building a system that simulates a print queue for an office. The system needs to process jobs in the order they were received.
*   **Task:** Write a function `process_print_jobs(jobs)` that takes a list of jobs and returns a list of the job IDs in the order they would be completed.
*   **Requirements:**
    *   Use the `Queue` class you implemented.
    *   The input `jobs` is a list of tuples, where each tuple is `(job_id, document_name)`.
    *   The function should simulate enqueuing all jobs and then dequeuing them one by one.
*   **Test Case:**
    *   **Input:** `process_print_jobs([(101, 'report.docx'), (102, 'photo.jpg'), (103, 'memo.txt')])`
    *   **Expected Output:** `[101, 102, 103]`

### Exercise 9: Queue
*   **Scenario:** You are analyzing a stream of real-time sensor data and need to find the maximum value within a moving window of a fixed size as it slides along the data array.
*   **Task:** Write a function `sliding_window_max(nums, k)` that takes an array of numbers `nums` and a window size `k`. It should return an array containing the maximum value for each window.
*   **Requirements:**
    *   This is a challenging problem. A naive solution is O(n*k). An optimal solution using a deque (a double-ended queue) can achieve O(n).
    *   The deque should be used to store indices of elements, keeping it in decreasing order of values.
*   **Test Case:**
    *   **Input:** `sliding_window_max(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)`
    *   **Expected Output:** `[3, 3, 5, 5, 6, 7]`

---

### Exercise 10: Linked List
*   **Scenario:** Linked lists are a fundamental data structure. Your goal is to implement one from the ground up to understand how nodes connect and store data.
*   **Task:** Implement a `SinglyLinkedList` class, along with a `Node` class.
*   **Requirements:**
    *   The `Node` class should have `data` and `next` attributes.
    *   The `SinglyLinkedList` class should have a `head` attribute and the following methods:
        *   `append(data)`: Adds a node to the end of the list.
        *   `prepend(data)`: Adds a node to the beginning.
        *   `delete(data)`: Deletes the first node containing the specified data.
*   **Test Case:**
    *   **Input:**
        1. `ll = SinglyLinkedList()`
        2. `ll.append(10)`
        3. `ll.append(20)`
        4. `ll.prepend(5)`
        5. `ll.delete(10)`
    *   **Expected Output:** The final list should contain the nodes `5 -> 20`.

### Exercise 11: Linked List
*   **Scenario:** In database management, you often need to merge sorted result sets. This task simulates that process using linked lists.
*   **Task:** Write a function `merge_sorted_lists(l1, l2)` that takes the heads of two sorted linked lists and merges them into a single, sorted linked list.
*   **Requirements:**
    *   The function should return the head of the new merged list.
    *   Do not create new nodes. The merging should be done by rearranging the pointers of the existing nodes.
*   **Test Case:**
    *   **Input:** `l1` representing `1 -> 2 -> 4`, `l2` representing `1 -> 3 -> 4`
    *   **Expected Output:** The head of a new list representing `1 -> 1 -> 2 -> 3 -> 4 -> 4`

### Exercise 12: Linked List
*   **Scenario:** You need to implement a feature that detects if a linked list has been corrupted in a way that creates a cycle (i.e., a node's `next` pointer points back to a previous node in the list).
*   **Task:** Write a function `has_cycle(head)` that determines if a linked list has a cycle in it.
*   **Requirements:**
    *   Use Floyd's Tortoise and Hare algorithm, which involves two pointers moving at different speeds.
    *   The function should return `True` if a cycle is present, and `False` otherwise.
    *   The solution should use O(1) (constant) memory.
*   **Test Case:**
    *   **Input:** A linked list where the last node points back to the second node. `1 -> 2 -> 3 -> 4 -> 2`
    *   **Expected Output:** `True`

---

### Exercise 13: Trees (Binary Tree & BST)
*   **Scenario:** Binary Search Trees (BSTs) are crucial for applications requiring efficient searching, insertion, and deletion. You need to implement the core structure.
*   **Task:** Implement a `BinarySearchTree` class with a `Node` inner class.
*   **Requirements:**
    *   The `Node` class should have `value`, `left`, and `right` attributes.
    *   The `BinarySearchTree` class should have a `root` attribute and the following methods:
        *   `insert(value)`: Inserts a value into the correct position in the BST.
        *   `search(value)`: Returns `True` if the value exists in the tree, `False` otherwise.
*   **Test Case:**
    *   **Input:**
        1. `bst = BinarySearchTree()`
        2. `bst.insert(10)`
        3. `bst.insert(5)`
        4. `bst.insert(15)`
        5. `bst.insert(7)`
    *   **Expected Output:** `bst.search(7)` should return `True`, and `bst.search(12)` should return `False`.

### Exercise 14: Trees (Binary Tree & BST)
*   **Scenario:** You've received a binary tree from a data source that is supposed to be a Binary Search Tree, but you need to validate this property before processing it further.
*   **Task:** Write a function `is_valid_bst(root)` that determines if a given binary tree is a valid BST.
*   **Requirements:**
    *   A valid BST has the property that for any given node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater.
    *   You'll need to pass down min/max constraints as you traverse the tree.
*   **Test Case:**
    *   **Input:** A tree with root node `5`, left child `1`, and right child `7`. The right child `7` has a left child `4`.
    *   **Expected Output:** `False` (because `4` is in the right subtree of `5` but is not greater than `5`).

### Exercise 15: Trees (Binary Tree & BST)
*   **Scenario:** You are working on a data transmission protocol that sends data in a binary tree format. To optimize the protocol, you need to convert the tree structure into a compact string representation that can be sent over the network and then perfectly reconstructed on the other side.
*   **Task:** Implement two functions: `serialize(root)` which converts a binary tree to a string, and `deserialize(string)` which reconstructs the tree from the string.
*   **Requirements:**
    *   The serialization format is up to you, but a common approach is pre-order traversal, using a special character (like '#') for null nodes.
    *   The two functions should be inverses of each other.
*   **Test Case:**
    *   **Input:**
        1. A tree with root `1`, left child `2`, right child `3`. `3` has a left child `4` and right child `5`.
        2. `data = serialize(root)`
        3. `new_root = deserialize(data)`
    *   **Expected Output:** `serialize(new_root)` should produce the exact same string as the original `serialize(root)` call. For a pre-order traversal with '#', the string might look like `"1,2,#,#,3,4,#,#,5,#,#"`

---

### Exercise 16: Heap
*   **Scenario:** Heaps are the ideal data structure for implementing priority queues. Implement a Min Heap to understand how it maintains the heap property.
*   **Task:** Create a `MinHeap` class.
*   **Requirements:**
    *   Use a list to store the heap elements.
    *   Implement the following methods:
        *   `insert(value)`: Adds a value to the heap and maintains the heap property.
        *   `extract_min()`: Removes and returns the smallest value from the heap.
        *   Helper methods like `_heapify_up` and `_heapify_down` are recommended.
*   **Test Case:**
    *   **Input:**
        1. `h = MinHeap()`
        2. `h.insert(3)`
        3. `h.insert(1)`
        4. `h.insert(6)`
        5. `h.insert(5)`
    *   **Expected Output:** Calling `h.extract_min()` three times should return `1`, then `3`, then `5`.

### Exercise 17: Heap
*   **Scenario:** You are working for a social media analytics company and need to find the most popular hashtags from a massive stream of posts.
*   **Task:** Write a function `top_k_frequent(nums, k)` that takes a list of numbers (or words) and an integer `k`, and returns the `k` most frequent elements.
*   **Requirements:**
    *   First, count the frequency of each element (a dictionary is good for this).
    *   Then, use a min-heap of size `k` to keep track of the `k` most frequent elements encountered so far.
*   **Test Case:**
    *   **Input:** `top_k_frequent(nums = [1,1,1,2,2,3], k = 2)`
    *   **Expected Output:** `[1, 2]` (order does not matter).

### Exercise 18: Heap
*   **Scenario:** You need to design a system that can efficiently find the median of a dataset that is constantly growing as new numbers arrive in a stream.
*   **Task:** Implement a `MedianFinder` class that can process a stream of numbers.
*   **Requirements:**
    *   The class should have two methods:
        *   `add_num(num)`: Adds a number from the data stream.
        *   `find_median()`: Returns the median of all elements added so far.
    *   This is a classic problem solved by using two heaps: a max-heap for the smaller half of the numbers and a min-heap for the larger half. The heaps should be kept balanced in size.
*   **Test Case:**
    *   **Input:**
        1. `mf = MedianFinder()`
        2. `mf.add_num(1)`
        3. `mf.add_num(2)`
        4. `mf.find_median()` returns `1.5`
        5. `mf.add_num(3)`
        6. `mf.find_median()` returns `2.0`
    *   **Expected Output:** The `find_median` calls should return the specified values.

---

### Exercise 19: Trie
*   **Scenario:** The Trie (or prefix tree) is a highly efficient data structure for storing and searching a dynamic set of strings. You will implement a basic version.
*   **Task:** Implement a `Trie` class.
*   **Requirements:**
    *   It should have a `TrieNode` inner class that contains a dictionary for children and a boolean flag `is_end_of_word`.
    *   Implement the following methods on the `Trie` class:
        *   `insert(word)`: Inserts a word into the trie.
        *   `search(word)`: Returns `True` if the exact word exists in the trie.
*   **Test Case:**
    *   **Input:**
        1. `t = Trie()`
        2. `t.insert("apple")`
        3. `t.search("apple")` returns `True`
        4. `t.search("app")` returns `False`
    *   **Expected Output:** The `search` calls should return the specified boolean values.

### Exercise 20: Trie
*   **Scenario:** You are building an autocompletion feature for a search bar. The system needs to know if any existing words start with the user's current input.
*   **Task:** Extend your `Trie` class by adding a `starts_with(prefix)` method.
*   **Requirements:**
    *   The `starts_with(prefix)` method should return `True` if there is any word in the trie that starts with the given prefix, `False` otherwise.
*   **Test Case:**
    *   **Input:**
        1. `t = Trie()`
        2. `t.insert("application")`
        3. `t.insert("apple")`
        4. `t.starts_with("app")`
    *   **Expected Output:** `True`

### Exercise 21: Trie
*   **Scenario:** To complete the autocompletion feature, you now need to suggest a list of possible words based on the user's typed prefix.
*   **Task:** Implement an `autocomplete(prefix)` method in your `Trie` class.
*   **Requirements:**
    *   The method should take a prefix string as input.
    *   It should return a list of all words stored in the trie that start with that prefix.
    *   This will require a traversal (like DFS) from the node corresponding to the end of the prefix.
*   **Test Case:**
    *   **Input:**
        1. `t = Trie()`
        2. `t.insert("cat")`, `t.insert("catalog")`, `t.insert("car")`, `t.insert("dog")`
        3. `t.autocomplete("cat")`
    *   **Expected Output:** `['cat', 'catalog']` (or in a different order).

---

### Exercise 22: Graphs (DFS & BFS)
*   **Scenario:** You need to implement a graph data structure and the two most fundamental traversal algorithms: Depth-First Search (DFS) and Breadth-First Search (BFS).
*   **Task:** Implement a `Graph` class using an adjacency list representation.
*   **Requirements:**
    *   The class should have methods: `add_vertex(vertex)` and `add_edge(v1, v2)`.
    *   Implement `bfs(start_vertex)` and `dfs(start_vertex)` methods. Both should return a list of visited nodes in the order of traversal.
*   **Test Case:**
    *   **Input:**
        1. Create a graph: 0-1, 0-2, 1-2, 2-3
        2. Call `g.bfs(0)`
        3. Call `g.dfs(0)`
    *   **Expected Output:**
        *   `bfs(0)`: `[0, 1, 2, 3]` (or `[0, 2, 1, 3]`)
        *   `dfs(0)`: `[0, 1, 2, 3]` (or `[0, 2, 3, 1]`, etc., depending on implementation)

### Exercise 23: Graphs (DFS & BFS)
*   **Scenario:** A university needs a system to check if a student's desired course plan is possible. Some courses have prerequisites, meaning you must complete one course before another.
*   **Task:** Write a function `can_finish(num_courses, prerequisites)` that returns `True` if all courses can be finished, and `False` if there is a circular dependency (e.g., Course A requires B, and B requires A).
*   **Requirements:**
    *   Model the problem as a directed graph where courses are nodes and prerequisites are edges.
    *   The problem is equivalent to detecting a cycle in the graph. DFS is a great tool for this.
*   **Test Case:**
    *   **Input:** `can_finish(num_courses=2, prerequisites=[[1, 0]])`
    *   **Expected Output:** `True` (You must take course 0 before course 1)
    *   **Input:** `can_finish(num_courses=2, prerequisites=[[1, 0], [0, 1]])`
    *   **Expected Output:** `False` (Circular dependency)

### Exercise 24: Graphs (DFS & BFS)
*   **Scenario:** You're playing a word game. The goal is to get from a `start_word` to an `end_word` by changing only one letter at a time, with each intermediate word being a valid word from a given dictionary.
*   **Task:** Write a function `word_ladder_length(start_word, end_word, word_list)` that finds the length of the shortest transformation sequence.
*   **Requirements:**
    *   This is a shortest path problem on an unweighted graph, which is a perfect use case for BFS.
    *   The "nodes" of the graph are the words. An "edge" exists between two words if they are one letter apart.
    *   The function should return the number of words in the shortest path (e.g., start -> ... -> end), or 0 if no path exists.
*   **Test Case:**
    *   **Input:** `word_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])`
    *   **Expected Output:** `5` (The path is "hit" -> "hot" -> "dot" -> "dog" -> "cog")

---

### Exercise 25: Searching (Binary Search)
*   **Scenario:** Binary search is a highly efficient algorithm for finding an item in a sorted collection. You must implement it to understand its core logic.
*   **Task:** Write a function `binary_search(arr, target)` that implements the binary search algorithm.
*   **Requirements:**
    *   The input array `arr` is guaranteed to be sorted.
    *   The function should return the index of the `target` if found.
    *   If the `target` is not in the array, it should return `-1`.
*   **Test Case:**
    *   **Input:** `binary_search([-1, 0, 3, 5, 9, 12], 9)`
    *   **Expected Output:** `4`

### Exercise 26: Searching (Binary Search)
*   **Scenario:** An online bookstore's database returns a list of books sorted by publication year. You need to find the first book published in a specific year, but there could be many books from that year.
*   **Task:** Write a function `find_first_occurrence(arr, target)` that finds the index of the first occurrence of `target` in a sorted array that may contain duplicates.
*   **Requirements:**
    *   The solution must be more efficient than a linear scan (i.e., it should be based on binary search).
    *   When an instance of `target` is found, you must continue searching in the left half of the array to see if an earlier one exists.
*   **Test Case:**
    *   **Input:** `find_first_occurrence([1, 2, 3, 5, 5, 5, 8], 5)`
    *   **Expected Output:** `3`

### Exercise 27: Searching (Binary Search)
*   **Scenario:** A sorted array of unique numbers was rotated at an unknown pivot point (e.g., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`). You need to find an element in this rotated array efficiently.
*   **Task:** Write a function `search_rotated_array(nums, target)` that searches for a `target` in a rotated sorted array.
*   **Requirements:**
    *   Your algorithm's time complexity must be O(log n).
    *   This requires a modified binary search that first determines which half of the current search space is sorted.
*   **Test Case:**
    *   **Input:** `search_rotated_array(nums = [4,5,6,7,0,1,2], target = 0)`
    *   **Expected Output:** `4`

---

### Exercise 28: Sorting (Quicksort & Mergesort)
*   **Scenario:** Quicksort is a highly efficient, divide-and-conquer sorting algorithm. Your task is to implement it to understand its partitioning logic.
*   **Task:** Write a function `quicksort(arr)` that sorts a list of numbers.
*   **Requirements:**
    *   Implement the algorithm using recursion.
    *   You will need a helper function, `partition`, which takes a subarray and a pivot, and rearranges the subarray so that all elements less than the pivot come before it, and all elements greater come after.
    *   The sort can be done in-place.
*   **Test Case:**
    *   **Input:** An unsorted array `[10, 7, 8, 9, 1, 5]`. The `quicksort` function is called on it.
    *   **Expected Output:** The array is modified to `[1, 5, 7, 8, 9, 10]`.

### Exercise 29: Sorting (Quicksort & Mergesort)
*   **Scenario:** Mergesort is another powerful divide-and-conquer sorting algorithm known for its stability. You'll implement it to sort a list of custom objects.
*   **Task:** Write a function `mergesort_students(students)` that sorts a list of `Student` objects by their `grade` attribute.
*   **Requirements:**
    *   Assume a `Student` class exists with `name` and `grade` attributes.
    *   Implement the recursive `mergesort` logic that splits the list and a `merge` helper function that combines two sorted lists.
    *   Unlike quicksort, mergesort is not typically done in-place and will require extra space.
*   **Test Case:**
    *   **Input:** A list of student objects: `[Student('Alice', 88), Student('Bob', 95), Student('Charlie', 72)]`
    *   **Expected Output:** A new list of student objects sorted by grade: `[Student('Charlie', 72), Student('Alice', 88), Student('Bob', 95)]`

### Exercise 30: Sorting (Quicksort & Mergesort)
*   **Scenario:** You're given an array containing only three distinct values (e.g., 0, 1, and 2, representing colors). You need to sort this array in a single pass with constant space.
*   **Task:** Implement the "Dutch National Flag" algorithm to sort an array of 0s, 1s, and 2s.
*   **Requirements:**
    *   The function `sort_colors(nums)` should sort the array in-place.
    *   The solution must be achieved in a single pass (O(n) time complexity) and use constant extra space (O(1)).
    *   Use three pointers: one for the next position of a 0 (`low`), one for the current element being considered (`mid`), and one for the next position of a 2 (`high`).
*   **Test Case:**
    *   **Input:** `nums = [2, 0, 2, 1, 1, 0]`. The `sort_colors` function is called on it.
    *   **Expected Output:** The `nums` array is modified to `[0, 0, 1, 1, 2, 2]`.

---

### Exercise 31: Backtracking
*   **Scenario:** Backtracking is a powerful technique for exploring all possible solutions to a problem. A fundamental backtracking problem is generating all permutations of a set of elements.
*   **Task:** Write a function `permute(nums)` that takes a list of distinct integers and returns all possible permutations.
*   **Requirements:**
    *   Use a recursive helper function that builds a permutation step by step.
    *   Keep track of which elements have been used in the current permutation to avoid duplicates.
*   **Test Case:**
    *   **Input:** `permute([1, 2, 3])`
    *   **Expected Output:** `[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]` (order of permutations does not matter).

### Exercise 32: Backtracking
*   **Scenario:** You are designing a feature for an e-commerce site to show all possible combinations of items a user could put in a "build your own" gift basket from a specific list of products.
*   **Task:** Write a function `subsets(nums)` that, given a set of distinct integers, returns all possible subsets (the power set).
*   **Requirements:**
    *   The solution set must not contain duplicate subsets.
    *   This can be solved using a recursive/backtracking approach where at each step, you decide whether to include the current number in the subset or not.
*   **Test Case:**
    *   **Input:** `subsets([1, 2, 3])`
    *   **Expected Output:** `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]` (order of subsets does not matter).

### Exercise 33: Backtracking
*   **Scenario:** You are developing a puzzle-solving application. One of the classic puzzles to include is Sudoku. You need to write the core engine that can solve any valid Sudoku puzzle.
*   **Task:** Write a function `solve_sudoku(board)` that solves a Sudoku puzzle.
*   **Requirements:**
    *   The input `board` is a 9x9 list of lists, where empty cells are represented by a specific character (e.g., `"."`).
    *   The function should modify the board in-place to fill in the solution.
    *   Use backtracking: Find an empty cell. Try placing a number from 1 to 9. Check if it's valid. If yes, recurse. If the recursion doesn't lead to a solution, backtrack by un-placing the number and trying the next one.
*   **Test Case:**
    *   **Input:** A 9x9 list representing a valid, partially filled Sudoku board.
    *   **Expected Output:** The input board is modified to its solved state.

---

### Exercise 34: Dynamic Programming
*   **Scenario:** Dynamic Programming (DP) often starts with understanding memoization. A classic example is optimizing the computation of Fibonacci numbers, which involves many overlapping subproblems.
*   **Task:** Write a function `fib(n)` that calculates the nth Fibonacci number using top-down dynamic programming (memoization).
*   **Requirements:**
    *   Use a dictionary or array to store the results of `fib(k)` once they are computed.
    *   Before computing `fib(k)`, check if the result is already in your memoization cache.
*   **Test Case:**
    *   **Input:** `fib(10)`
    *   **Expected Output:** `55`

### Exercise 35: Dynamic Programming
*   **Scenario:** You are designing a cash register system that needs to give customers change using the fewest possible coins.
*   **Task:** Write a function `coin_change(coins, amount)` that calculates the minimum number of coins required to make up a given amount.
*   **Requirements:**
    *   `coins` is a list of coin denominations available.
    *   `amount` is the total amount to make.
    *   Use bottom-up dynamic programming. Create a DP array where `dp[i]` stores the minimum coins needed for amount `i`.
    *   If the amount cannot be made up by any combination of the coins, return -1.
*   **Test Case:**
    *   **Input:** `coin_change(coins = [1, 2, 5], amount = 11)`
    *   **Expected Output:** `3` (because 11 = 5 + 5 + 1)

### Exercise 36: Dynamic Programming
*   **Scenario:** You're working on a "diff" utility that compares two text files. The core of this utility is calculating the "edit distance" between two strings: the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.
*   **Task:** Write a function `edit_distance(word1, word2)` that computes the Levenshtein distance between two strings.
*   **Requirements:**
    *   Use a 2D DP table, where `dp[i][j]` represents the edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`.
    *   The state transition will depend on whether `word1[i]` equals `word2[j]`.
*   **Test Case:**
    *   **Input:** `edit_distance(word1 = "horse", word2 = "ros")`
    *   **Expected Output:** `3` (1. h->r, 2. remove e, 3. remove s)

## Final Project

_This is a larger capstone project that requires combining multiple concepts from the topics above into a single, cohesive solution._

---

### Final Project: Code Dependency Analyzer
*   **Objective:** To build a tool that analyzes a directory of simple Python files to build a function call graph. The tool will then use this graph to identify potential circular dependencies and find unused functions, helping developers clean up and understand their codebase.
*   **Background Scenario:** You are a senior developer on a team that has inherited a large, legacy codebase. To make refactoring safer and more manageable, your manager has asked you to create a static analysis tool that can provide insights into the code's structure without running it. The first step is to map out which functions call which other functions.
*   **Core Tasks:**
    1.  **File Parsing and Call Extraction:** Create a function that takes a directory path. It should iterate through all `.py` files in that directory. For each file, parse the content (using basic string methods is sufficient) to create a mapping: for each function defined in the file, list all other functions that are called from within it. You can use a dictionary to store this information, e.g., `{'my_func': ['helper1', 'helper2']}`. (Concepts: Dictionaries, Lists/Arrays, String Manipulation).
    2.  **Graph Construction:** Using the data from the parsing step, construct a directed graph. Create a `Graph` class (or use a library). Each function name should be a vertex in the graph. For every function call from `func_A` to `func_B`, add a directed edge from the `A` vertex to the `B` vertex. (Concepts: Graph data structure).
    3.  **Analysis and Reporting:** Implement two analysis methods on your graph:
        *   **Circular Dependency Detection:** Use a Depth-First Search (DFS) traversal to detect cycles in the graph. Your DFS will need to keep track of the nodes currently in the recursion stack. If you encounter a node that's already in the stack, you've found a cycle. Report any cycles found. (Concepts: DFS, Recursion).
        *   **Unused Function Identification:** Traverse the graph to find all functions (nodes) that have an in-degree of 0. These are functions that are never called by any other function in the analyzed set and are candidates for being "dead code". Report these functions. (Concepts: Graph traversal).
*   **Deliverable:** A single Python script that can be run from the command line, taking a directory path as an argument. The script should print a clear report to the console, with separate sections for "Circular Dependencies Found" and "Potentially Unused Functions".
*   **Verification / Success Criteria:**
    *   **Check 1:** Given a directory with `a.py` (containing `def func_a(): func_b()`) and `b.py` (containing `def func_b(): func_a()`), the script must report a circular dependency between `func_a` and `func_b`.
    *   **Check 2:** Given a file `c.py` with `def used_func(): pass` and `def unused_func(): pass`, and another file `d.py` with `import c; c.used_func()`, the script must identify `unused_func` in its report.
    *   **Check 3:** The script must successfully run without errors on a directory containing multiple valid (but simple) Python files and correctly identify all function definitions and calls based on simple `def` and `()` patterns.