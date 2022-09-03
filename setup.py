from site import getsitepackages
from sys import executable
from os.path import normpath, dirname, isdir, join
from os import system
from shutil import copytree, rmtree

system('')

module_dirs = getsitepackages()
python_path = dirname(executable)
module_dir = next(dir for dir in module_dirs if python_path in dir and 'site-packages' in dir)

ansi_esc = u'\u001b'
rgb = lambda r, g, b: f'{ansi_esc}[38;2;%s;%s;%sm' % (r, g, b)
reset = f'{ansi_esc}[0m'

red = rgb(255, 75, 75)

cryptMyReplPath = join(module_dir, 'CryptMyRepl')

try:
    copytree('./CryptMyRepl', cryptMyReplPath)
except PermissionError:
    print(f'{red}cannot create the folder in Python module dir. Try to launch this file in administrator{reset}')
    raise SystemExit(1)

except FileExistsError:
    try:
        rmtree(cryptMyReplPath)
    except PermissionError:
        print(f'{red}cannot create the folder in Python module dir. Try to launch this file in administrator{reset}')
        raise SystemExit(1)

    copytree('./CryptMyRepl', cryptMyReplPath)

if isdir(cryptMyReplPath):
    print(f'Success! Stored in {cryptMyReplPath}')