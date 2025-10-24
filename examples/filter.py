from typing import Any, Tuple

from pydtree import tree


def filter_func(key: str, value: Any) -> Tuple[str, Any]:
    if key.startswith("_"):
        return None, None
    if key in {"password", "secret", "token"}:
        return key, "******"
    return key, value


data = {
    'root': {
        '_root_child1': 'value1',
        '_root_child2': 'value2',
        'child1': 'value1',
        'child2': 'value2',
        'child3': {
            'grandchild1': 'value3',
            'grandchild2': 'value4'
        },
        'password': 'password'
    }
}

for line in tree('Dictionary tree', data, filter=filter_func):
    print(line)
