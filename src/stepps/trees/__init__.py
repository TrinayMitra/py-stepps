from collections.abc import Callable
from typing import Literal, overload

from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.iterators.levelorder import LevelOrderIterator as _LOI
from stepps.nodes import BinaryNode
from stepps.trees.binary_tree import BinaryTree
from stepps.trees.binary_tree_impl import BinaryTreeImpl
from stepps.trees.bst import BST, Comparable
from stepps.trees.bst_impl import BSTImpl
from stepps.trees.tree import Tree

__all__ = [
    "BST",
    "BinaryTree",
    "Tree",
    "get_binary_tree",
]


@overload
def get_binary_tree[T: Comparable](
    *,
    search_tree: Literal[True] = True,
    find_search_iter: Callable[
        [BinaryNode[T] | None],
        BinaryTreeIterator[BinaryNode[T]],
    ]
    | None = None,
) -> BST[T]: ...


@overload
def get_binary_tree[T: Comparable](
    *,
    search_tree: Literal[False] = False,
    find_search_iter: Callable[
        [BinaryNode[T] | None],
        BinaryTreeIterator[BinaryNode[T]],
    ]
    | None = None,
) -> BinaryTree[T]: ...


def get_binary_tree[T: Comparable](
    *,
    search_tree: Literal[True, False] = False,
    find_search_iter: Callable[
        [BinaryNode[T] | None],
        BinaryTreeIterator[BinaryNode[T]],
    ]
    | None = None,
) -> BinaryTree[T] | BST[T]:
    """
    Create a binary tree implementation.

    :param search_tree: Whether to create a binary search tree.
    :param find_search_iter: Iterator to use for find operations.
        Level-order traversal is used by default.
    :return: A binary tree implementation.
    """
    if search_tree:
        return BSTImpl()

    if find_search_iter is None:
        find_search_iter = _LOI

    return BinaryTreeImpl(find_search_iter)
