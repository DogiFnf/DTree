import dtree

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


def custom_render(key, value):
    return f"{key} ({value})"


# Traverse the tree using a generator
for line in dtree.tree(
        'my_tree',
        data,
        dtree.themes.Unicode,
        custom_render
):
    print(line)
