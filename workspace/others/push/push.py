import os
from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
from modules.MyView import MyView

message = "VuVanNghia20206205"

git_path =  os.path.join(os.getcwd(), '../../../')
init_path =  os.path.join(os.getcwd(), '../../../baocao/contents/start/init.sty')
workspace_path = os.path.join(os.getcwd(), '../../vvn20206205.code-workspace')
gitignore_path = os.path.join(git_path, ".gitignore") 

MyGit.chdir(git_path)
MyGit.add()
MyGit.commit(message)

MyFormat.latex(git_path)
MyFormat.markdown(git_path)
MyFormat.basic(gitignore_path)
MyFormat.basic(init_path)
MyFormat.workspace(workspace_path)

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
# MyView.CollapseFolders()
# MyView.OpenGit()
MyView.OpenLatex()
