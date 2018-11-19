#!/usr/bin/python
import i3ipc

i3 = i3ipc.Connection()
w_dict = sorted(i3.get_workspaces(), key=lambda x: x['num'])
i = 1
for w in w_dict:
    if i != w['num']:
        i3.command(f'workspace {i}')
        break
    i += 1
else:
    i3.command(f'workspace {i}')
