from typing import Any

from pydtree import tree
from pydtree.types import RenderData


def custom_render(
        key: str,
        value: Any,
        render_data: RenderData
) -> str:
    if render_data.is_endpoint:  # If the node is an endpoint
        if isinstance(value, str):
            return f'{key}: \"{value}\"'
        elif isinstance(value, int):
            return f'{key}: {value}'
        elif isinstance(value, float):
            return f'{key}: {value}'
        elif isinstance(value, bool):
            return f'{key}: {value}'
        else:
            return f'{key}: {repr(value)} ({type(value).__name__})'

    else:  # If the node is not an endpoint
        if isinstance(value, dict):
            return f'{key}: (dict with {len(value)} keys)'
        elif isinstance(value, list):
            return f'{key}: (list with {len(value)} items)'
        elif isinstance(value, tuple):
            return f'{key}: (tuple with {len(value)} items)'
        elif isinstance(value, set):
            return f'{key}: (set with {len(value)} items)'
        elif isinstance(value, frozenset):
            return f'{key}: (frozenset with {len(value)} items)'
        else:
            return f'{key}:'


data = {
    'root': {
        'child1': 'value1',
        'child2': ['a', 'b', 'c'],
        'child3': {'nested': 42}
    }
}

for line in tree('My Tree', data, render=custom_render):
    print(line)
