from QLayouts import QLayouts
from QRules import QRules

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

class QGroups:

    layouts = QLayouts()
    rules = QRules()

    def init_group(self, groups):
        result = []
        for i in range(len(groups)):
            result.append(
                Group(
                    name=groups[i].name,
                    matches=self.rules.get_match(groups[i].match_type),
                    layouts=self.layouts.get_layout(groups[i].layout_type),
                    init=True,
                    persist=True
                ))

        return result

    def init_keys(self, mod, groups, screen):
        keys = []

        for i in groups:
            keys.extend([
                Key([mod], i.name, self.go_to_group_on_screen(i.name, screen),
                    desc="Switch to Group {} on Monitor {}".format(str(i.name), screen)),
                Key([mod, 'shift'], i.name, self.shift_to_group(i.name, screen),
                    desc="Shift to Group {} on Monitor {}".format(str(i.name), screen)),
            ])

        return keys

    def go_to_group(self, qtile, group, screen):
        # if current group not visible - switch
        current_groups = [screen.group.name for screen in qtile.screens if screen.group]
        if group not in current_groups:
            qtile.groups_map.get(group).cmd_toscreen()

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
