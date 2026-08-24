from stepps.iterators.levelorder import LevelOrderIterator
from stepps.TreeBuilder.level_order_tree_builder_impl import LevelOrderTreeBuilderImpl


def test_build_empty_sequence():
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build([])

    assert root is None


def test_build_single_element():
    sequence = [50]
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None
    assert root.value == 50

    result = [node.value for node in LevelOrderIterator(root)]

    assert result == sequence


def test_build_complete_tree():
    sequence = [50, 30, 70, 20, 40, 60, 80]
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None

    result = [node.value for node in LevelOrderIterator(root)]

    assert result == sequence


def test_build_incomplete_last_level():
    sequence = [50, 30, 70, 20, 40, 60]
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None

    result = [node.value for node in LevelOrderIterator(root)]

    assert result == sequence


def test_build_left_incomplete_tree():
    sequence = [50, 30, 70, 20]
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None

    result = [node.value for node in LevelOrderIterator(root)]

    assert result == sequence


def test_build_long_sequence():
    sequence = list(range(1, 16))
    builder = LevelOrderTreeBuilderImpl[int]()

    root = builder.build(sequence)

    assert root is not None

    result = [node.value for node in LevelOrderIterator(root)]

    assert result == sequence
