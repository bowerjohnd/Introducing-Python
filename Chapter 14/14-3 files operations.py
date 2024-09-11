import os

print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))

print('')

name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))

print('')

print(os.path.isabs(name))
print(os.path.isabs('/big/fake/name'))
print(os.path.isabs('big/fake/name/without/a/leading/slash'))

print('')

import shutil
print(os.path.exists('oops.txt'))
print(os.path.exists('ohno.txt'))

#shutil.copy('oops.txt', 'ohno.txt')

print(os.path.exists('oops.txt'))
print(os.path.exists('ohno.txt'))

print('')

print(os.path.exists('ohno.txt'))
print(os.path.exists('ohwell.txt'))

#os.rename('ohno.txt', 'ohwell.txt')

print(os.path.exists('ohno.txt'))
print(os.path.exists('ohwell.txt'))

print('')

#os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

#os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))

print('')

os.chmod('oops.txt', 0o400)

import stat
os.chmod('oops.txt', stat.S_IRUSR)

uid = 5
gid = 22
#os.chown('oops', uid, gid)

print('')

#os.remove('oops.txt')
print(os.path.exists('oops.txt'))

#os.mkdir('poems')
print(os.path.exists('poems'))

#os.rmdir('poems')
print(os.path.exists('poems'))

print('')

#os.mkdir('poems')
print(os.listdir('poems'))
#os.mkdir('poems/mcintyre')
print(os.listdir('poems'))

fout = open('poems/mcintyre/the_good_man', 'wt')
print(
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
)
fout.close()

print(os.listdir('poems/mcintyre'))

print('')

#import os
os.chdir('poems')
print(os.listdir('.'))

print('')

import glob
print(glob.glob('m*'))
print(glob.glob('??'))
print(glob.glob('m??????e'))
print(glob.glob('[klm]*e'))

