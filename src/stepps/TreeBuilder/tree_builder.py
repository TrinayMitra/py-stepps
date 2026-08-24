from abc import ABC, abstractmethod
from collections.abc import Sequence

from stepps.nodes import BinaryNode


class TreeBuilder[T](ABC):
    """
    Define the interface for building a binary tree from a sequence.
    """

    @abstractmethod
    def build(self, sequence: Sequence[T]) -> BinaryNode[T] | None:
        """
        Build a binary tree from a sequence.

        :param sequence: The sequence of values used to build the tree.
        :return: The root node of the constructed tree, or ``None`` if the
            sequence is empty.
        """
        ...
