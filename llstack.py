from node import Node


class LLStack:
    """
    A singly-linked-list based Stack.

    Attributes:
        __head(Node): Node representing the top of the stack.
        __size(int): integer representing the number of Nodes in the stack.
    """

    def __init__(self):
        """
        Constructor for LLStack.
        """

        self.__head: Node = None
        self.__size: int = 0

    # Properties
    @property
    def size(self):
        """
        Returns:
            int: integer representing the number of nodes in the LLStack.
        """

        return self.__size

    @property
    def head(self):
        """
        Returns:
            Node: returns the top node in the stack.
        """

        return self.__head

    def pop(self) -> tuple:
        """
        Method to remove the top Node from the LLStack.

        Returns:
            tuple: data from the removed Node.

        Raises:
            IndexError: if the LLStack is empty.
        """

        if self.__head is None:
            raise IndexError
        item = self.__head  # Store the popped Node to item variable
        self.__head = self.__head.next  # Change the head to the next Node
        self.__size -= 1  # Subtract the Node from the size
        return item.data

    def push(self, data: tuple):
        """
        Method to add a new Node to LLStack.

        Parameters:
            data(tuple): data contained in the Node.
        """

        new = Node(data)  # Initialize new Node
        new.next = self.__head  # Set the previous head to next
        self.__head = new  # Set the new node as the current head
        self.__size += 1  # Add the new node to the size of the stack.

    def copy(self):
        """
        Method to create a copy of the LLStack.

        Returns:
            LLStack: a copy of the current LLStack.
        """

        temp_stack = LLStack()  # Initialize temporary stack
        copied_stack = LLStack()  # Initialize the final copied stack

        # Iterate through the original stack adding every Node to the temp stack
        cur_node = self.__head
        while cur_node is not None:
            temp_stack.push(cur_node.data)
            cur_node = cur_node.next

        # Iterate through the temp stack adding every Node to the copied stack.
        cur_node = temp_stack.__head
        while cur_node is not None:
            copied_stack.push(cur_node.data)
            cur_node = cur_node.next
        return copied_stack

    def checked_node(self, other: tuple):
        """
        Method to check if data is in the current LLStack.

        Parameters:
            other(tuple): data to check if in current stack.

        Returns:
            bool: returns True if the data is in the stack, False if not.
        """

        #  Iterate through stack checking if each Nodes data is the same as param
        cur_node = self.__head
        while cur_node is not None:
            if other == cur_node.data:
                return True
            cur_node = cur_node.next
        return False

    def __lt__(self, other: 'LLStack'):
        """
        Method to compare sizes of LLStacks.

        Parameters:
            other(LLstack): the LLStack being compared.

        Returns:
            bool: returns True if the stack is smaller than the compared stack.
        """
        if self.size < other.size:
            return True
        else:
            return False

    def __str__(self):
        """
        Method returning a string representation of a LLStack.

        Returns:
            str: string representing the data of each Node in the LLStack.
        """

        end_str = ''  # Initialize string

        # Iterate through LLStack
        cur_node = self.__head
        while cur_node is not None:
            if cur_node.next is None:
                end_str += str(cur_node)  # Add data to the end string
                cur_node = cur_node.next
            else:
                end_str += str(cur_node)  # Add data to the end string
                end_str += ' -> '  # Add connector in between data
                cur_node = cur_node.next
        return end_str
