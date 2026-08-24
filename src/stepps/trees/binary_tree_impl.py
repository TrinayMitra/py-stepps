from collections import deque
from collections.abc import Callable
from typing import override

from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.nodes import BinaryNode
from stepps.trees.binary_tree import BinaryTree


class BinaryTreeImpl[T](BinaryTree[T]):
    """
    Provide the default implementation of a binary tree.
    """

    def __init__(
        self,
        find_search_iter: Callable[
            [BinaryNode[T] | None],
            BinaryTreeIterator[BinaryNode[T]],
        ]
        | None = None,
    ) -> None:
        self.root: BinaryNode[T] | None = None
        self._size = 0
        self._find_search_iter = find_search_iter

    def is_empty(self) -> bool:
        """
        Return whether the tree is empty.

        :return: ``True`` if the tree contains no nodes, otherwise ``False``.
        """
        return self.root is None

    def clear(self) -> None:
        """
        Remove all nodes from the tree.
        """
        self.root = None
        self._size = 0

    def size(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        return self._size

    @override
    def find(self, value: T) -> BinaryNode[T] | None:
        """
        Find the first node containing ``value``.

        :param value: The value to search for.
        :return: The matching node, or ``None`` if the value is not found.
        """
        if self._find_search_iter is None:
            return None

        iterator = self._find_search_iter(self.root)

        for node in iterator:
            if node.value == value:
                return node

        return None

    @override
    def contains(self, value: T) -> bool:
        """
        Return whether ``value`` exists in the tree.

        :param value: The value to search for.
        :return: ``True`` if the value exists, otherwise ``False``.
        """
        return self.find(value) is not None

    @override
    def __contains__(self, value: T) -> bool:
        """
        Return whether ``value`` exists in the tree.

        :param value: The value to search for.
        :return: ``True`` if the value exists, otherwise ``False``.
        """
        return self.contains(value)

    @override
    def height(self) -> int:
        """
        Return the height of the tree.

        :return: The height of the tree.
        """
        if self.root is None:
            return -1

        queue: deque[tuple[BinaryNode[T], int]] = deque([(self.root, 0)])
        max_height = 0

        while queue:
            node, level = queue.popleft()
            max_height = max(max_height, level)

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return max_height

    @override
    def count_leaves(self) -> int:
        """
        Return the number of leaf nodes in the tree.

        :return: The number of leaf nodes.
        """
        if self.root is None:
            return 0

        count = 0
        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.is_leaf():
                count += 1
                continue

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return count

    @override
    def count_internal_nodes(self) -> int:
        """
        Return the number of internal nodes in the tree.

        :return: The number of internal nodes.
        """
        if self.root is None:
            return 0

        count = 0
        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.has_children():
                count += 1

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return count

    @override
    def insert(self, value: T) -> BinaryNode[T]:
        """
        Insert a value into the tree.

        :param value: The value to insert.
        :raises NotImplementedError: Binary tree insertion is defined by
            concrete tree implementations.
        """
        raise NotImplementedError

    @override
    def delete(self, value: T) -> bool:
        """
        Delete a value from the tree.

        :param value: The value to delete.
        :raises NotImplementedError: Binary tree deletion is defined by
            concrete tree implementations.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        return self._size

    def __bool__(self) -> bool:
        """
        Return whether the tree contains at least one node.

        :return: ``True`` if the tree is not empty, otherwise ``False``.
        """
        return not self.is_empty()

    @override
    def invert_tree(self) -> None:
        """
        Invert the binary tree in place.

        The left and right children of every node are exchanged.
        """
        if self.root is None:
            return

        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
