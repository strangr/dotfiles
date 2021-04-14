from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keys import keys, mod

left_groups = ["1", "2", "3", "4", "5"]
right_groups = ["F1", "F2", "F3", "F4", "F5"]
all_groups = left_groups + right_groups

groups = []
for i in range(len(all_groups)):
    groups.append(
        Group(
            name=all_groups[i],
            #matches=group_matches[i],
            #exclusive=group_exclusives[i],
            #layout=group_layouts[i].lower(),
            init=True,
            persist=True,
            label="●",
        ))


for i in left_groups:
    keys.extend([
        Key([mod], i, lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Switch to group {}".format(str(i))),
        Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Shift to group {}".format(str(i))),
    ])

for i in right_groups:
    keys.extend([
        Key([mod], i, lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Switch to group {}".format(str(i))),
        Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Shift to group {}".format(str(i))),
    ])