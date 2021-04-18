from libqtile.config import Group, Key, ScratchPad, DropDown
from libqtile.lazy import lazy

from keys import keys, mod

rect_small = dict(
    opacity=0.9,
    height=0.5,
    width=0.5,
    x=0.25,
    y=0.25
)

rect_large = dict(
    opacity=0.9,
    height=0.8,
    width=0.8,
    x=0.1,
    y=0.1
)

left_groups = ["1", "2", "3", "4", "grave"]
right_groups = ["q", "w", "e", "r", "t"]
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

groups.append(
    ScratchPad("scratchpad", [
        DropDown("terminal-scratch", "urxvt -name term-scratch", **rect_small, on_focus_lost_hide=False),
        DropDown("ranger-scratch", "urxvt -name ranger-scratch -e ranger", **rect_large, on_focus_lost_hide=False),
        DropDown("pavucontrol-scratch", "pavucontrol", **rect_small, on_focus_lost_hide=True),
    ]))


#TODO if already on that group in that screen, dont switch group or else it moves to prev group
for i in left_groups:
    keys.extend([
        Key([mod], i, lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 1".format(str(i))),
        Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 1".format(str(i))),
    ])

for i in right_groups:
    keys.extend([
        Key([mod], i, lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 2".format(str(i))),
        Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 2".format(str(i))),
    ])

keys.extend([
    Key([], 'F8', lazy.group['scratchpad'].dropdown_toggle('ranger-scratch')),
    Key([], 'F9', lazy.group['scratchpad'].dropdown_toggle('pavucontrol-scratch')),
    Key([], 'F10', lazy.group['scratchpad'].dropdown_toggle('terminal-scratch')),
])


#@lazy.function
# def aka(num):
#     def f(qtile):
#         groups[0].label = "B"
#         #qtile.cmd_to_screen(num)

#     return f

# keys.extend([
#     #Key([], 'F7', lazy.function(aka2(0))),
#     Key([], 'F6', lazy.group['2'].set_label('D')),
# ])


# keys.extend([
#     #Key([], 'F7', lazy.function(aka(0))),
#     Key([], 'F7', lazy.function(change_text())),
# ])
