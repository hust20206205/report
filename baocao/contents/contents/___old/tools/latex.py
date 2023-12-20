from modules.Convert import Convert
import os
import shutil
import pyperclip
import re
# nhận văn bản
input = pyperclip.paste()
match = re.search(r'\{([^}]+)\}', input)
if match:
    input = match.group(1)
    print(input)
else:
    print("No match found.")
    exit()
input = input.replace("(", "")
input = input.replace(")", "")
input = input.replace("/", "")
input = input.replace("-", "")
while "  " in input:
    input = input.replace("  ", " ")
output = Convert.VarSnakeCase(input)
# sao chép file
ten_file_nguon = r"../contents/_a.tex"
ten_file_dich = os.path.join("../contents", f"{output}"+".tex")
shutil.copy(ten_file_nguon, ten_file_dich)
# xóa file
with open(ten_file_nguon, 'w') as file:
    file.write('')
# return văn bản
output = "\n\\input{contents/" + output + "}\n\n\n" 
# output += "\\section{xxxxxxx}\n" 
# output += "\\subsection{xxxxxxx}\n" 
output += "\\subsubsection{xxxxxxx}\n" 
output += "\\input{contents/_a.tex}\n" 
pyperclip.copy(output)
