from collections.abc import Sequence
from typing import override

from stepps.nodes import BinaryNode
from stepps.TreeBuilder.inorder_tree_builder import InOrderTreeBuilder


class InOrderTreeBuilderImpl[T](InOrderTreeBuilder[T]):
    """
    Provide the default implementation for building a binary tree
    from an inorder sequence.
    """

    @override
    def build(self, sequence: Sequence[T]) -> BinaryNode[T] | None:
        """
        Build a binary tree from an inorder sequence.

        :param sequence: The sequence of values used to build the tree.
        :return: The root node of the constructed tree, or ``None`` if the
            sequence is empty.
        """
        return self._build(sequence, 0, len(sequence) - 1)

    def _build(
        self,
        sequence: Sequence[T],
        left: int,
        right: int,
    ) -> BinaryNode[T] | None:
        """
        Recursively construct the tree from the given sequence range.

        :param sequence: The sequence of values used to build the tree.
        :param left: The start index of the current range.
        :param right: The end index of the current range.
        :return: The root node of the constructed subtree.
        :complexity: O(n) space complexity, including the constructed tree.
        """
        if left > right:
            return None
        if (len(sequence)) % 2 == 0:
            mid = (left + right + 1) // 2
        else:
            mid = (left + right) // 2

        node = BinaryNode(sequence[mid])

        node.left = self._build(sequence, left, mid - 1)
        node.right = self._build(sequence, mid + 1, right)

        return node
