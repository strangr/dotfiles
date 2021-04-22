from QLayouts import QLayouts

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

class QGroups:

    left_groups = []
    right_groups = []

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
                    #label=""
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

    def init_keys(self, mod):
        #TODO divide key inits into two
        keys = []

        for i in self.left_groups:
            keys.extend([
                Key([mod], i, self.go_to_group_on_screen(i, 0), desc="Switch to Group {} on Monitor 1".format(str(i))),
                Key([mod, 'shift'], i, self.shift_to_group(i,0), desc="Shift to Group {} on Monitor 1".format(str(i))),
            ])

        for i in self.right_groups:
            keys.extend([
                Key([mod], i, self.go_to_group_on_screen(i, 1), desc="Switch to Group {} on Monitor 2".format(str(i))),
                Key([mod, 'shift'], i, self.shift_to_group(i,1), desc="Shift to Group {} on Monitor 2".format(str(i))),
            ])

        # Screen Navigation
        keys.extend([
            Key([mod], "s", self.go_to_screen(0), desc="Shift to Monitor 1"),
            Key([mod], "d", self.go_to_screen(1), desc="Shift to Monitor 2"),
        ])
        

        return keys

    def go_to_group(self, qtile, group, screen):
        # if current group not visible - switch
        current_groups = [screen.group.name for screen in qtile.screens if screen.group]
        if group not in current_groups:
            qtile.groups_map.get(group).cmd_toscreen()

    def go_to_screen(self, screen):
        @lazy.function
        def f(qtile):
            qtile.cmd_to_screen(screen)

        return f

    def go_to_group_on_screen(self, group, screen):
        @lazy.function
        def f(qtile):
            qtile.cmd_to_screen(screen)
            self.go_to_group(qtile, group, screen)

        return f

    def shift_to_group(self, group, screen):
        @lazy.function
        def f(qtile):
            # bug: if two windows on target group, sometimes both get displaced (displace only window that we want)
            qtile.current_window.togroup(group)
            qtile.cmd_to_screen(screen)
            self.go_to_group(qtile, group, screen)

        return f
