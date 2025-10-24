from pydtree import tree, themes
from pydtree.types import Theme

# Using ASCII theme
data = {
    'root': {
        'child1': 'value1',
        'child2': 'value2'
    }
}

for line in tree('ASCII Theme', data, theme=themes.Ascii):
    print(line)


print("\n" + "="*50 + "\n")

# Using Unicode theme
for line in tree('Unicode Theme', data, theme=themes.Unicode):
    print(line)


print("\n" + "="*50 + "\n")

# Custom theme
MyTheme = Theme(
    vertical='|  ',
    branch='|- ',
    corner='=- ',
    tab='   '
)

for line in tree('Custom Theme', data, theme=MyTheme):
    print(line)
