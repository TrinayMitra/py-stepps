from typing import override

from stepps.nodes import BinaryNode
from stepps.visualizer.cli_visualizer import CliTreeVisualizer


class CliTreeVisualizerImpl[T](CliTreeVisualizer[T]):
    """
    Provide the default CLI implementation for binary tree visualization.
    """

    @override
    def treevisualizer(self, tree: BinaryNode[T] | None) -> None:
        """
        Visualize a binary tree in the terminal.

        :param tree: The root node of the binary tree.
        """
        if tree is None:
            print("<empty tree>")
            return

        self._display(tree)

    def _display(
        self,
        node: BinaryNode[T],
        prefix: str = "",
        is_left: bool = True,
    ) -> None:
        """
        Display a binary tree node and its children.

        :param node: The current node.
        :param prefix: The indentation prefix.
        :param is_left: Whether the node is a left child.
        """
        if node.right is not None:
            self._display(
                node.right,
                prefix + ("│   " if is_left else "    "),
                False,
            )

        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.value))

        if node.left is not None:
            self._display(
                node.left,
                prefix + ("    " if is_left else "│   "),
                True,
            )
