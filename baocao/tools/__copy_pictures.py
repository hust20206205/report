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
# sao chép  

nguon = r"../pictures/_"
dich = os.path.join("../pictures", output)
shutil.copytree(nguon, dich)