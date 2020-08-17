from os import mkdir
from pathlib import Path

# absolute path
# C:\Program Files\...
#relative path
# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)