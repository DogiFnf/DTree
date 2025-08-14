import pytest

from dtree import themes, tree
from dtree.types import Theme

# Data from the README.md example
TEST_DATA = {
    "root": {
        "child1": "value1",
        "child2": "value2",
        "child3": {"grandchild1": "value3", "grandchild2": "value4"},
    }
}


def test_tree_with_default_ascii_theme():
    """Tests the default ASCII theme output against the expected structure."""
    expected_output = [
        "my_tree:",
        "`-- root",
        "    +-- child1: value1",
        "    +-- child2: value2",
        "    `-- child3",
        "        +-- grandchild1: value3",
        "        `-- grandchild2: value4",
    ]

    # The generator returns lines, so we collect them into a list
    actual_output = list(tree("my_tree", TEST_DATA))

    assert actual_output == expected_output


def test_tree_with_unicode_theme():
    """Tests the Unicode theme output against the expected structure."""
    expected_output = [
        "my_tree:",
        "└── root",
        "    ├── child1: value1",
        "    ├── child2: value2",
        "    └── child3",
        "        ├── grandchild1: value3",
        "        └── grandchild2: value4",
    ]

    actual_output = list(tree("my_tree", TEST_DATA, theme=themes.Unicode))

    assert actual_output == expected_output


def test_invalid_data_type_raises_error():
    """Tests that a TypeError is raised for unsupported data types."""
    with pytest.raises(TypeError, match="Data must be a dict, list, or tuple"):
        # We need to consume the generator to trigger the error
        list(tree("my_tree", "just a string"))


def test_empty_data():
    """Tests that the tree function handles empty data gracefully."""
    expected_output = ["my_tree:", "`-- root"]
    actual_output = list(tree("my_tree", {}))
    assert actual_output == expected_output


def test_magic_number_bug_with_custom_theme():
    """
    This test is EXPECTED TO FAIL.
    It checks for the 'magic number' bug where the prefix is hardcoded.
    A custom theme with a wider indent will expose this bug.
    """
    MyTheme = Theme(
        vertical="|    ", branch="+--- ", corner="`--- ", tab="     "  # 5 spaces, not 4
    )
    expected_output = [
        "my_tree:",
        "`--- root",
        "     +--- child1: value1",
        "     `--- child2: value2",
    ]
    data = {"root": {"child1": "value1", "child2": "value2"}}
    actual_output = list(tree("my_tree", data, theme=MyTheme))
    assert actual_output == expected_output


def test_cyclical_dependency_handling():
    """
    Tests that the tree function can handle data with circular references
    without crashing.
    """
    data = {"name": "node1"}
    data["cycle"] = data  # Create a cycle

    expected_output = [
        "cyclic_tree:",
        "`-- root",
        "    +-- name: node1",
        "    `-- cycle: [Circular Reference]",
    ]

    actual_output = list(tree("cyclic_tree", {"root": data}))
    assert actual_output == expected_output
