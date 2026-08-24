from stepps.trees.bst_impl import BSTImpl
from stepps.visualizer.cli_visualizer_impl import CliTreeVisualizerImpl


def create_tree() -> BSTImpl:
    """
    Create a sample binary search tree for visualization tests.

    :return: A populated binary search tree.
    """
    tree: BSTImpl = BSTImpl()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    return tree


def test_visualize_tree(capsys):
    """
    Test visualization of a populated binary search tree.
    """
    tree = create_tree()
    visualizer = CliTreeVisualizerImpl()

    visualizer.treevisualizer(tree.root)

    captured = capsys.readouterr()

    print(captured.out)

    assert "50" in captured.out
    assert "30" in captured.out
    assert "70" in captured.out
    assert "20" in captured.out
    assert "40" in captured.out
    assert "60" in captured.out
    assert "80" in captured.out

    assert captured.out.count("50") == 1
    assert captured.out.count("30") == 1
    assert captured.out.count("70") == 1


def test_visualize_empty_tree(capsys):
    """
    Test visualization of an empty binary search tree.
    """
    tree: BSTImpl = BSTImpl()
    visualizer = CliTreeVisualizerImpl()

    visualizer.treevisualizer(tree.root)

    captured = capsys.readouterr()

    print(captured.out)

    assert captured.out == "<empty tree>\n"


def test_visualize_single_node_tree(capsys):
    """
    Test visualization of a binary search tree containing one node.
    """
    tree: BSTImpl = BSTImpl()
    tree.insert(50)

    visualizer = CliTreeVisualizerImpl()
    visualizer.treevisualizer(tree.root)

    captured = capsys.readouterr()

    print(captured.out)

    assert captured.out == "└── 50\n"


def test_visualize_left_skewed_tree(capsys):
    """
    Test visualization of a left-skewed binary search tree.
    """
    tree: BSTImpl = BSTImpl()

    for value in [50, 40, 30, 20]:
        tree.insert(value)

    visualizer = CliTreeVisualizerImpl()
    visualizer.treevisualizer(tree.root)

    captured = capsys.readouterr()

    print(captured.out)

    assert "50" in captured.out
    assert "40" in captured.out
    assert "30" in captured.out
    assert "20" in captured.out


def test_visualize_right_skewed_tree(capsys):
    """
    Test visualization of a right-skewed binary search tree.
    """
    tree: BSTImpl = BSTImpl()

    for value in [50, 60, 70, 80]:
        tree.insert(value)

    visualizer = CliTreeVisualizerImpl()
    visualizer.treevisualizer(tree.root)

    captured = capsys.readouterr()

    print(captured.out)

    assert "50" in captured.out
    assert "60" in captured.out
    assert "70" in captured.out
    assert "80" in captured.out
