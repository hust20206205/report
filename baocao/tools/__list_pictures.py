import os
import glob


def TimKiem(root_dir, ext):
    return glob.glob(os.path.join(
        root_dir, f'**/*{ext}'), recursive=True)


base_folder = os.path.join(os.getcwd(), "..")
folder = os.path.join(base_folder, "pictures")

files = TimKiem(folder, '.png')
files += TimKiem(folder, '.jpg')

with open(os.path.join(folder,"_pictures.md"), 'w') as markdown:
    for file in files:
        markdown.write(f"========================================\n")
        # markdown.write(f"![]({os.path.relpath(file, folder)})\n")
        markdown.write(f"\n")
        markdown.write(f"\\begin{{figure}}[H]\n")
        markdown.write(f"\\centering\n")
        markdown.write("\\includegraphics[scale = 0.5]{"+f"{os.path.relpath(file, base_folder).replace('\\', '/')}"+"}\n")
        markdown.write("\\caption{vvn20206205}\n")
        # markdown.write("\\label{pictures:"+ f"{os.path.relpath(file, folder)}"+"}\n")
        markdown.write(f"\\end{{figure}}\n")
        markdown.write(f"========================================\n")
        
 

files = glob.glob(os.path.join(folder, f'**/*.md'), recursive=True)
for file_markdown in files:
    with open(file_markdown, 'r', encoding="utf-8") as file:
        contents = file.read()

    if contents == '':
        continue

    contents = contents.replace('\n', '\n\n\n')

    while '  ' in contents:
        contents = contents.replace('  ', ' ')
    contents = '\n'.join(line.strip() for line in contents.split('\n'))
    while "\n\n\n" in contents:
        contents = contents.replace("\n\n\n", "\n\n")
    contents = contents.lstrip('\n')
    with open(file_markdown, 'w', encoding="utf-8") as file:
        file.write(contents)