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
else:
    print("No match found.")
print(input)
input = input.replace("(", "")
input = input.replace(")", "")
input = input.replace("/", "")
input = input.replace("-", "")
input = input.replace("%", "")
while "  " in input:
    input = input.replace("  ", " ")
print(input)
output = Convert.VarSnakeCase(input)
# sao chép file
ten_file_nguon = r"../contents/_a.tex"
ten_file_dich = os.path.join("../contents", f"{output}"+".tex")
shutil.copy(ten_file_nguon, ten_file_dich)
# xóa file
with open(ten_file_nguon, 'w') as file:
    file.write('')
# return văn bản
output = "\n\n\n\n\\input{contents/" + output + "}\n\n\n\n\n\n\n\n\n\n\n\n" 



# output += "% \\section{xxxxxxx}\n\n\n\n" 
# output += "% \\subsection{xxxxxxx}\n\n\n\n" 
output += "% \\subsubsection{xxxxxxx}\n\n\n\n" 
# output += "% \\paragraph{xxxxxxx}\n\n\n\n" 
# output += "% \\subparagraph{xxxxxxx}\n\n\n\n" 



output += "% \\input{contents/_a.tex}\n\n\n\n" 
pyperclip.copy(output)
import pyautogui


pyautogui.hotkey('alt', '2')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'j')