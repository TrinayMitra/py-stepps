from collections import deque
from collections.abc import Sequence
from typing import override

from stepps.nodes import BinaryNode
from stepps.TreeBuilder.level_order_tree_builder import LevelOrderTreeBuilder


class LevelOrderTreeBuilderImpl[T](LevelOrderTreeBuilder[T]):
    """
    Provide the default implementation for building a binary tree
    from a level-order sequence.
    """

    @override
    def build(self, sequence: Sequence[T]) -> BinaryNode[T] | None:
        """
        Build a binary tree from a level-order sequence.

        The values are assigned to nodes level by level from left to right.

        :param sequence: The sequence of values used to build the tree.
        :return: The root node of the constructed tree, or ``None`` if the
            sequence is empty.
        """
        if not sequence:
            return None

        root = BinaryNode(sequence[0])
        queue: deque[BinaryNode[T]] = deque([root])

        index = 1

        while index < len(sequence):
            parent = queue.popleft()

            parent.left = BinaryNode(sequence[index])
            queue.append(parent.left)
            index += 1

            if index < len(sequence):
                parent.right = BinaryNode(sequence[index])
                queue.append(parent.right)
                index += 1

        return root
