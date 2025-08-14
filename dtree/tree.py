from types import FunctionType
from typing import Any, Generator, Set

from . import themes
from .types import Theme, TreeNode


def _render(key: str, value: Any) -> str:
    """Default render function for a key-value pair."""
    return f"{key}: {value}"


def tree(
    name: str, data: Any, theme: Theme = themes.Ascii, render: FunctionType = None
) -> Generator[str, None, None]:
    """
    Generator for building and traversing a data tree.

    Args:
        name: The name of the tree.
        data: The input data to build the tree from (dict, list, or tuple).
        theme: The theme to use for rendering the tree.
        render: A custom function to render key-value pairs.

    Yields:
        str: A string representing the current node in the tree.
    """
    if not isinstance(data, (dict, list, tuple)):
        raise TypeError("Data must be a dict, list, or tuple")

    yield f"{name}:"

    # Handle empty data case as per test_empty_data
    if not data:
        yield theme.corner + "root"
        return

    render_func = render or _render
    visited: Set[int] = set()

    def _build_tree(data: Any, parent_key: str = "") -> TreeNode:
        """Recursively builds a TreeNode structure from nested data."""
        if id(data) in visited:
            return TreeNode(value=f"{parent_key}: [Circular Reference]")
        if isinstance(data, (dict, list, tuple)):
            visited.add(id(data))

        node = TreeNode(value=parent_key or "root")

        if isinstance(data, dict):
            for key, value in data.items():
                child = _build_tree(value, str(key))
                node.children.append(child)
        elif isinstance(data, (list, tuple)):
            for idx, item in enumerate(data):
                child = _build_tree(item, f"[{idx}]")
                node.children.append(child)
        else:
            node.value = render_func(parent_key, data)

        return node

    root = _build_tree(data)

    def _traverse(
        node: TreeNode, prefix: str = "", is_last: bool = True
    ) -> Generator[str, None, None]:
        """Recursively traverses the TreeNode and yields formatted strings."""
        if prefix:
            connector = theme.corner if is_last else theme.branch
            line = prefix + connector + node.value
        else:
            line = node.value

        if line != "root":
            # Fix for "magic number" bug: use theme's tab length
            yield line[len(theme.tab) :]

        new_prefix = prefix + (theme.tab if is_last else theme.vertical)
        for i, child in enumerate(node.children):
            yield from _traverse(child, new_prefix, i == len(node.children) - 1)

    yield from _traverse(root)
