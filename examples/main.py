from pydtree import tree

# Example with dictionary
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

for line in tree('Dictionary tree', data):
    print(line)

print('\n' + '=' * 50 + '\n')

# Example with list
data_list = {
    'root': [
        'item1',
        'item2',
        {'nested': 'value'}
    ]
}

for line in tree('List tree', data_list):
    print(line)

print('\n' + '=' * 50 + '\n')

# Example with set
data_set = {
    'root': {'a', 'b', 'c'}
}

for line in tree('Set tree', data_set):
    print(line)


print("\n" + '=' * 50 + "\n")

# Depth limitation
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

for line in tree('Depth-limited tree', data, max_depth=3):
    print(line)
