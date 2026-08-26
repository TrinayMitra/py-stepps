from stepps.iterators.inorder import InOrderIterator
from stepps.TreeBuilder.inorder_tree_builder_impl import InOrderTreeBuilderImpl


def test_build_empty_sequence():
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build([])

    assert root is None


def test_build_single_element():
    sequence = [50]
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None
    assert root.value == 50

    result = [node.value for node in InOrderIterator(root)]

    assert result == sequence


def test_build_odd_length_sequence():
    sequence = [1, 2, 3, 4, 5, 6, 7]
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None
    assert root.value == 4

    result = [node.value for node in InOrderIterator(root)]

    assert result == sequence


def test_build_even_length_sequence():
    sequence = [1, 2, 3, 4, 5, 6]
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None
    assert root.value == 4

    result = [node.value for node in InOrderIterator(root)]

    assert result == sequence


def test_build_long_sequence():
    sequence = list(range(1, 16))
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None

    result = [node.value for node in InOrderIterator(root)]

    assert result == sequence


def test_build_tree_structure():
    sequence = [1, 2, 3, 4, 5, 6, 7]
    builder = InOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None
    assert root.value == 4

    assert root.left is not None
    assert root.left.value == 2

    assert root.right is not None
    assert root.right.value == 6

    assert root.left.left is not None
    assert root.left.left.value == 1

    assert root.left.right is not None
    assert root.left.right.value == 3

    assert root.right.left is not None
    assert root.right.left.value == 5

    assert root.right.right is not None
    assert root.right.right.value == 7
