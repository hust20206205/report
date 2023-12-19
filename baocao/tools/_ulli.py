import pyperclip

# Nhận văn bản từ clipboard
input_text = pyperclip.paste()

# Tách các dòng trong văn bản
lines = input_text.split('\n')

# Kiểm tra từng dòng và thêm '\item' nếu dòng không trống
output_lines = []
for line in lines:
    if line.strip() != "":
        output_lines.append("\\item " + line)
    else:
        output_lines.append(line)

# Ghép các dòng thành văn bản mới
output_text = '\n'.join(output_lines)
output_text ="\n\n \\begin{itemize} \n\n"+output_text
output_text =output_text+"\n\n \\end{itemize} \n\n"

# In kết quả
print(output_text)

pyperclip.copy(output_text)
import pyautogui 
pyautogui.hotkey('ctrl', 'j')
pyautogui.hotkey('ctrl', 'shift', 'g') 