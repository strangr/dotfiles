from QLayouts import QLayouts

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

class QGroups:

    left_groups = []
    right_groups = []

    group_matches = [
        None, None, None, None, None, None,
        [Match(wm_class=[
            "discord",
        ]), ],
        [Match(wm_class=[
            "slack", "microsoft teams - preview",
        ]), ],
        None,None,
    ]

    right_group_matches = [
        None,
        [Match(wm_class=[
            "discord",
        ]), ],
        [Match(wm_class=[
            "slack", "microsoft teams - preview",
        ]), ],
        None,None,
    ]

    layouts = QLayouts()
    
    def __init__(self, l, r):
        self.left_groups = l
        self.right_groups = r

    def init_left_groups(self):
        result = []
        for i in range(len(self.left_groups)):
            result.append(
                Group(
                    name=self.left_groups[i],
                    #matches=group_matches[i],
                    #exclusive=group_exclusives[i],
                    layouts=self.layouts.get_defaults(),
                    init=True,
                    persist=True,
                    label=""
                ))

        return result

    def init_right_groups(self):
        result = []
        for i in range(len(self.right_groups)):
            result.append(
                Group(
                    name=self.right_groups[i],
                    #matches=self.right_group_matches[i],
                    #exclusive=group_exclusives[i],
                    layouts=self.layouts.get_defaults(),
                    init=True,
                    persist=True,
                    label=""
                ))

        return result

    #TODO if already on that group in that screen, dont switch group or else it moves to prev group
    def init_keys(self, mod):
        keys = []

        for i in self.left_groups:
            keys.extend([
                Key([mod], i, lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 1".format(str(i))),
                Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 1".format(str(i))),
            ])

        for i in self.right_groups:
            keys.extend([
                Key([mod], i, lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 2".format(str(i))),
                Key([mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 2".format(str(i))),
            ])

        # Screen Navigation
        keys.extend([
            Key([mod], "s", lazy.function(self.go_to_screen(0))),
            Key([mod], "d", lazy.function(self.go_to_screen(1))),
        ])
        

        return keys

    #@lazy.function
    # TODO move inside helpers
    def go_to_screen(self, num):
        def f(qtile):
            qtile.cmd_to_screen(num)

        return f

# keys.extend([
#     Key([], 'F6', lazy.group['2'].set_label('D')),
# ])

