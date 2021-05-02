from QWidgetsList import QWidgetsList
from QTheme import Colors

from libqtile.bar import Bar
from libqtile.config import Screen
from libqtile.config import Key
from libqtile.lazy import lazy

class QBars:

    widgets_list = QWidgetsList()
    colors = Colors()

    bar_config = dict(
        background = colors.black[0],
        margin = [0,0,0,0],
        opacity = 1,
        size=26
    )

    def init_left_bar(self, groups):
        return Bar(
            widgets=self.widgets_list.left_widgets_list(groups),
            **self.bar_config
        )

    def init_right_bar(self, groups):
        return Bar(
            widgets=self.widgets_list.right_widgets_list(groups),
            **self.bar_config
        )

class QScreen:

    bars = QBars()

    def init_dual_screen_bar(self, l, r):
        
        left_groups = [group.name for group in l if group]
        right_groups = [group.name for group in r if group]

        return [
            Screen(
                top = self.bars.init_left_bar(left_groups)
            ),
            Screen(
                top = self.bars.init_right_bar(right_groups)
            )
        ]

    def init_keys(self, mod):
        keys = []

        # Screen Navigation
        keys.extend([
            Key([mod], "s", self.go_to_screen(0), desc="Shift to Monitor 1"),
            Key([mod], "d", self.go_to_screen(1), desc="Shift to Monitor 2"),

            Key([mod, "control"], "s", self.toggle_sticky()),
        ])

        return keys

    def go_to_screen(self, screen):
        @lazy.function
        def f(qtile):
            qtile.cmd_to_screen(screen)

        return f

    def toggle_sticky(self):
        @lazy.function
        def f(qtile):
            if 'sticky' in qtile.current_window.cmd_hints():
                qtile.current_window.cmd_disable_floating()
                qtile.current_window.hints.pop("sticky", None)
            else:
                qtile.current_window.cmd_bring_to_front()
                qtile.current_window.cmd_enable_floating()
                qtile.current_window.hints["sticky"] = qtile.current_screen.index

        return f
