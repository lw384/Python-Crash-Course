# 10.1
from pathlib import Path

base_path = Path(__file__).parent
path = base_path / 'learning_python.txt'

content = path.read_text()

print(f'Reading the entire file : {content}')

str = ''
for line in content.splitlines():
    if 'python' in line:
        line = line.replace('python','C++')
    str += line.lstrip()

print(f'Reading by lines : {str}')

path.write_text('I love programming')

name = input('What is your name')

path2 = Path('guest.txt')
path2.write_text(name)