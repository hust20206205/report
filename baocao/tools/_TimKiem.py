import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = os.path.join(os.getcwd(), "../../")
print( folder)
files = TimKiem(folder, '.srt')
files = TimKiem(folder, '.tex')
files = TimKiem(folder, '.md')
for f in files:
    print(f)


 