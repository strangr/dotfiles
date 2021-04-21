from QWidgetsList import QWidgetsList
from QTheme import Colors

from libqtile.bar import Bar
from libqtile.config import Screen

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

class QScreen(object):

    left_groups = []
    right_groups = []

    bars = QBars()

    def __init__(self, l, r):
        self.left_groups = l
        self.right_groups = r


    def init_dual_screen_bar(self):
        return [
            Screen(
                top = self.bars.init_left_bar(self.left_groups)
            ),
            Screen(
                top = self.bars.init_right_bar(self.right_groups)
            )
        ]