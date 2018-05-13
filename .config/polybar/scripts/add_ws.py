#!/usr/bin/python
import subprocess
import i3

max_ws = 4
ws_list = [[x,0] for x in range(10)]
# get a list of workspaces
for workspace in i3.get_workspaces():
    # get the workspace tree data
    workspace_tree = i3.filter(num=workspace.get('num'))
    ws_list[int(workspace.get('num'))][1] = 1
for i in ws_list:
    if i[0] > max_ws and not i[1]:
        subprocess.run(['i3-msg', 'workspace', str(i[0])])
        break
