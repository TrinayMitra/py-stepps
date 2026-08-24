import pytest

from stepps.iterators import (
    InOrderIterator,
    LevelOrderIterator,
    PostOrderIterator,
    PreOrderIterator,
)
from stepps.trees.bst_impl import BSTImpl


@pytest.fixture
def bst():
    tree = BSTImpl()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    return tree


# =====================================================
# Basic Properties
# =====================================================


def test_new_tree_is_empty():
    tree = BSTImpl()

    assert tree.is_empty()
    assert len(tree) == 0


def test_size(bst):
    assert len(bst) == 7


# =====================================================
# Search
# =====================================================


def test_find_existing(bst):
    node = bst.find(40)

    assert node is not None
    assert node.value == 40


def test_find_missing(bst):
    assert bst.find(999) is None


def test_contains(bst):
    assert 60 in bst


def test_not_contains(bst):
    assert 100 not in bst


# =====================================================
# Min / Max
# =====================================================


def test_minimum(bst):
    node = bst.minimum()

    assert node is not None
    assert node.value == 20


def test_maximum(bst):
    node = bst.maximum()

    assert node is not None
    assert node.value == 80


# =====================================================
# Tree Statistics
# =====================================================


def test_height(bst):
    assert bst.height() == 2


def test_leaf_count(bst):
    assert bst.count_leaves() == 4


def test_internal_nodes(bst):
    assert bst.count_internal_nodes() == 3


# =====================================================
# Traversals
# =====================================================


def test_inorder(bst):
    values = [node.value for node in InOrderIterator(bst.root)]

    assert values == [20, 30, 40, 50, 60, 70, 80]


def test_preorder(bst):
    values = [node.value for node in PreOrderIterator(bst.root)]

    assert values == [50, 30, 20, 40, 70, 60, 80]


def test_postorder(bst):
    values = [node.value for node in PostOrderIterator(bst.root)]

    assert values == [20, 40, 30, 60, 80, 70, 50]


def test_levelorder(bst):
    values = [node.value for node in LevelOrderIterator(bst.root)]

    assert values == [50, 30, 70, 20, 40, 60, 80]


# =====================================================
# Delete
# =====================================================


def test_delete_leaf(bst):
    assert bst.delete(20)

    values = [node.value for node in InOrderIterator(bst.root)]

    assert values == [30, 40, 50, 60, 70, 80]


def test_delete_node_with_one_child(bst):
    bst.delete(20)

    assert bst.delete(30)

    values = [node.value for node in InOrderIterator(bst.root)]

    assert values == [40, 50, 60, 70, 80]


def test_delete_node_with_two_children(bst):
    assert bst.delete(50)

    values = [node.value for node in InOrderIterator(bst.root)]

    assert values == [20, 30, 40, 60, 70, 80]


def test_delete_missing_node(bst):
    assert not bst.delete(999)

    assert len(bst) == 7
