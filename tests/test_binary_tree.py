import pytest

from stepps.iterators.levelorder import LevelOrderIterator
from stepps.nodes import BinaryNode
from stepps.trees.binary_tree_impl import BinaryTreeImpl


class ConcreteBinaryTree(BinaryTreeImpl[int]):
    """
    Concrete binary tree used for testing ``BinaryTreeImpl``.
    """

    def insert(self, value: int) -> BinaryNode[int]:
        raise NotImplementedError

    def delete(self, value: int) -> bool:
        raise NotImplementedError

    def invert_tree(self) -> None:
        super().invert_tree()


@pytest.fixture
def tree():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    root = BinaryNode(50)
    root.left = BinaryNode(30)
    root.right = BinaryNode(70)
    root.left.left = BinaryNode(20)
    root.left.right = BinaryNode(40)
    root.right.left = BinaryNode(60)
    root.right.right = BinaryNode(80)

    tree.root = root
    tree._size = 7

    return tree


# =====================================================
# Basic Properties
# =====================================================


def test_new_tree_is_empty():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    assert tree.is_empty()
    assert len(tree) == 0
    assert tree.size() == 0
    assert not tree


def test_size(tree):
    assert tree.size() == 7
    assert len(tree) == 7
    assert tree


def test_clear(tree):
    tree.clear()

    assert tree.is_empty()
    assert tree.size() == 0
    assert len(tree) == 0


# =====================================================
# Search
# =====================================================


def test_find_existing(tree):
    node = tree.find(40)

    assert node is not None
    assert node.value == 40


def test_find_missing(tree):
    assert tree.find(999) is None


def test_contains(tree):
    assert 60 in tree


def test_not_contains(tree):
    assert 100 not in tree


# =====================================================
# Tree Statistics
# =====================================================


def test_height(tree):
    assert tree.height() == 2


def test_empty_tree_height():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    assert tree.height() == -1


def test_leaf_count(tree):
    assert tree.count_leaves() == 4


def test_empty_tree_leaf_count():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    assert tree.count_leaves() == 0


def test_internal_nodes(tree):
    assert tree.count_internal_nodes() == 3


def test_empty_tree_internal_nodes():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    assert tree.count_internal_nodes() == 0


# =====================================================
# Tree Inversion
# =====================================================


def test_invert_tree(tree):
    tree.invert_tree()

    assert tree.root is not None
    assert tree.root.value == 50

    assert tree.root.left is not None
    assert tree.root.left.value == 70

    assert tree.root.right is not None
    assert tree.root.right.value == 30

    assert tree.root.left.left is not None
    assert tree.root.left.left.value == 80

    assert tree.root.left.right is not None
    assert tree.root.left.right.value == 60

    assert tree.root.right.left is not None
    assert tree.root.right.left.value == 40

    assert tree.root.right.right is not None
    assert tree.root.right.right.value == 20


def test_invert_empty_tree():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    tree.invert_tree()

    assert tree.is_empty()


def test_invert_single_node_tree():
    tree = ConcreteBinaryTree(LevelOrderIterator)

    tree.root = BinaryNode(50)
    tree._size = 1

    tree.invert_tree()

    assert tree.root is not None
    assert tree.root.value == 50
    assert tree.root.left is None
    assert tree.root.right is None
