from abc import abstractmethod

from stepps.nodes import BinaryNode
from stepps.visualizer.tree_visualizer import TreeVisualizer


class CliTreeVisualizer[T](TreeVisualizer[BinaryNode[T] | None]):
    """
    Define the interface for CLI-based binary tree visualization.
    """

    @abstractmethod
    def treevisualizer(self, tree: BinaryNode[T] | None) -> None:
        """
        Visualize a binary tree in the CLI.

        :param tree: The root node of the binary tree.
        """
        ...
