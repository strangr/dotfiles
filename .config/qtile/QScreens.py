from QWidgetsList import QWidgetsList

from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

class QBars:

    widgets_list = QWidgetsList()
    bar_config = dict(
        background = '282425',
        margin = [0,0,0,0],
        opacity = 1,
        size=26
    )

    def init_left_bar(self):
        return Bar(
            widgets=self.widgets_list.left_widgets_list(),
            **self.bar_config
        )

    def init_right_bar(self):
        return Bar(
            widgets=self.widgets_list.right_widgets_list(),
            **self.bar_config
        )

class QScreens(object):

    bars = QBars()

    def init_dual_screen_bar(self):
        return [
            Screen(
                top = self.bars.init_left_bar()
            ),
            Screen(
                top = self.bars.init_right_bar()
            )
        ]