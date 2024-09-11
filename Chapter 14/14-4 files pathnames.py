win_file = 'eek\\urk\\snort.txt'
win_file2 = r'eek\urk\snort.txt'
print(win_file)
print(win_file2)

print('')

import os
print(os.path.abspath('oops.txt'))

#for unix/linux
print(os.path.realpath('jeepers.txt'))

print('')

win_file = os.path.join("eek", "urk")
win_file = os.path.join(win_file, "snort.txt")

print(win_file)

print('')

from pathlib import Path
file_path = Path('eek') / 'urk' / 'snort.txt'
print(file_path)
print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

print('')

from pathlib import PureWindowsPath
print(PureWindowsPath('eek/urk/snort.txt'))
print(PureWindowsPath(file_path))

