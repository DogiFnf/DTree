

# DTree: Python Library for Building and Traversing Trees

DTree is a Python library for building and traversing trees. It provides a simple and efficient way to create and manipulate tree data structures.

## Features

* Create trees from dictionaries, lists, and tuples
* Traverse trees using generators
* Support for different tree themes (ASCII, Unicode)
* Customizable tree rendering

## Installation

To install DTree, run the following command:
```bash
pip install pydtree
```
## Usage

Here is an example of how to create and traverse a tree using DTree:
```python
import pydtree

# Create a tree from a dictionary
data = {
    'root': {
        'child1': 'value1',
        'child2': 'value2',
        'child3': {
            'grandchild1': 'value3',
            'grandchild2': 'value4'
        }
    }
}

# Traverse the tree using a generator
for line in pydtree.tree('my_tree', data):
    print(line)
```
This will output the following tree structure:
```
my_tree:
`-- root
    +-- child1: value1
    +-- child2: value2
    `-- child3
        +-- grandchild1: value3
        `-- grandchild2: value4
```
## Themes

DTree supports different tree themes, including ASCII and Unicode. You can customize the theme by passing a `theme` parameter to the `tree` function:
```python
for line in pydtree.tree(
        'my_tree',
        data,
        theme=dtree.themes.Unicode
):
    print(line)
```
This will output the following tree structure using Unicode characters:
```
my_tree:
└── root
    ├── child1: value1
    ├── child2: value2
    └── child3
        ├── grandchild1: value3
        └── grandchild2: value4
```
## Customization

You can customize the tree rendering by passing a `render` function to the `tree` function:
```python
def custom_render(key, value):
    return f"{key} ({value})"

for line in pydtree.tree(
        'my_tree',
        data,
        render=custom_render
):
    print(line)
```
This will output the following tree structure with custom rendering:
```
my_tree:
+-- child1 (value1)
+-- child2 (value2)
`-- child3 (value3)
```
## Contributing

If you'd like to contribute to DTree, please fork the repository and submit a pull request.

## License

DTree is licensed under the MIT License.