#!/usr/bin/python
import i3ipc

i3 = i3ipc.Connection()
i = 1
for w in i3.get_workspaces():
    if i != w['num']:
        i3.command(f'workspace {i}')
        break
    i += 1
else:
    i3.command(f'workspace {i}')
