# ICT 201 - Data Structures and Algorithms
# 🐍 Python Linear Data Structures

A practical guide to implementing and understanding **linear data structures** using Python.

Linear data structures organize elements sequentially — each item is attached to its neighbor.
They form the foundation of most algorithms and problem-solving techniques.

---

## 📌 What’s Inside

This repository covers the following **linear data structures**:

* **Lists**
* **Stacks (LIFO)**
* **Queues (FIFO)**
* **Linked Lists**
* **Doubly Linked Lists** *(optional)*
* **Array-based and List-based implementations**

Each module contains:
✔ Overview and use cases
✔ Common operations
✔ Working Python examples
✔ Time complexity notes

---

## 📁 Project Structure

```
python-linear-data-structures/
│
├── lists/
│   └── list_examples.py
│
├── stacks/
│   └── stack.py
│
├── queues/
│   └── queue.py
│
├── linked_list/
│   └── singly_linked_list.py
│
├── doubly_linked_list/
│   └── doubly_linked_list.py   (optional)
│
└── README.md
```

---

## 🚀 Running the Code

### 🔧 Requirements

* Python **3.8+**
* No third-party libraries required

### ▶ Execute any file

```bash
git clone https://github.com/yourusername/python-linear-data-structures.git
cd python-linear-data-structures

python stacks/stack.py
```

---

## 📚 Data Structures Overview

### 📌 List (Built-in Dynamic Array)

* Stores ordered values, supports duplicates
* Indexable and sliceable

```python
nums = [1, 2, 3]
nums.append(4)
```

---

### 📌 Stack (Last-In, First-Out)

Used in:

* Undo/redo
* Syntax parsing
* Function call stacks

```python
from collections import deque
stack = deque()
stack.append("A")  # push
stack.pop()        # pop
```

---

### 📌 Queue (First-In, First-Out)

Used in:

* Task scheduling
* Customer service systems
* Breadth-first search

```python
from collections import deque
queue = deque()
queue.append("Task")
queue.popleft()
```

---

### 📌 Singly Linked List

Node-based dynamic structure
Efficient for insertions/removals compared to lists

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### 📌 Doubly Linked List *(Optional)*

Nodes have **prev** and **next** pointers
Great when you need fast backward traversal

---

## ⏱ Time Complexity Snapshot

| Structure   | Access | Search | Insert | Delete |
| ----------- | ------ | ------ | ------ | ------ |
| List        | O(1)   | O(n)   | O(n)   | O(n)   |
| Stack       | O(n)*  | O(n)*  | O(1)   | O(1)   |
| Queue       | O(n)*  | O(n)*  | O(1)   | O(1)   |
| Linked List | O(n)   | O(n)   | O(1)*  | O(1)*  |

**when operating at the ends (head/tail)*

---

## 🎯 Why Focus on Linear Structures?

Mastering linear data structures helps you:

* Think algorithmically
* Build scalable programs
* Understand memory and runtime trade-offs
* Prepare for technical interviews

---

## 🤝 Contributing

Contributions welcome!
Add:

* More structure variants
* Exercises or challenges
* Visualizers or test cases

---

## 📄 License

MIT — free to use and expand.

---

## ⭐ Support

If this repo helped you, **give it a star** ⭐
Happy coding and keep learning! 🧠🛠


## References 📚

1. Baka, B. (2017). Python data structures and algorithms: Improve application performance with graphs, stacks, and queues. Packt Publishing. ISBN 978-1-78646-735-5.
2. GeeksforGeeks. (2025, July 26). Complete A2Z Reference for DSA Concepts. Retrieved from https://www.geeksforgeeks.org/dsa/
3. krahets. (2025). Before starting – Hello Algo. Hello Algo. https://www.hello-algo.com/en/chapter_hello_algo/
4. Pregueiro, P. (n.d.). Linked Lists in Python: An Introduction. Real Python. Retrieved from https://realpython.com/linked-lists-python/
5. Python Software Foundation. (2025, September 14). Data Structures — Python 3.13.7 documentation. https://docs.python.org/3/tutorial/datastructures.html
6. WeeTech Solution. (2024, June 20). What is the difference between linear data structure and non linear data structure? https://www.weetechsolution.com/blog/difference-between-linear-and-non-linear-data-structure
