"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


class XOR_Node():
    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_idx):
        return self.both ^ prev_idx

    def prev_node(self, next_idx):
        return self.both ^ next_idx


class XOR_List():
    def __init__(self):
        self.mem = [XOR_Node(None, -1, -1)]

    # Returns head node idx, prev node idx, and head node
    def head(self):
        return 0, -1, self.mem[0]

    def add(self, val):
        cur_node_idx, prev_node_idx, cur_node = self.head()
        next_node_idx = cur_node.next_node(prev_node_idx)
        # Go until we reach the end
        while next_node_idx != -1:
            prev_node_idx, cur_node_idx = cur_node_idx, next_node_idx
            cur_node = self.mem[next_node_idx]

        # Add the node to our memory
        new_node_idx = len(self.mem)
        cur_node.both = prev_node_idx ^ new_node_idx
        self.mem.append(XOR_Node(val, cur_node_idx, -1))

    def get(self, index):
        cur_idx, prev_idx, cur_node = self.head()
        for cnt in range(index + 2):
            prev_idx = cur_idx
            cur_idx = cur_node.next_node(prev_idx)
            cur_node = self.memory[cur_idx]
        return cur_node.val


