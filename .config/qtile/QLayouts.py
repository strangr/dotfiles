from QTheme import Colors
from QGroup import LayoutType

from libqtile.layout.max import Max
from libqtile.layout.columns import Columns
from libqtile.layout.bsp import Bsp
from libqtile.layout.xmonad import MonadTall

#僧
#类﩯舘麗
#ﰧﳶ
#﵁恵頻侀𤋮全充

class QLayouts:

    colors = Colors()
    icon_full = ""
    icon_monad = ""
    icon_columns = "舘"

    def col_test(self):

        return Columns(
            Name=self.icon_columns,
            border_focus=self.colors.green[0],
            border_focus_stack=self.colors.green[0],
            border_normal=self.colors.grey[0],
            border_normal_stack=self.colors.grey[0],
            border_on_single=False,
            border_width=1,
            fair=False,
            grow_amount=10,
            insert_position=1,
            margin=2,
            margin_on_single=0,
            num_columns=2,
            split=True,
            wrap_focus_columns=True,
            wrap_focus_rows=True,
            wrap_focus_stacks=True
        )

    def monad_test(self):

        return MonadTall(
            name=self.icon_monad,
            align=MonadTall._left,
            margin=0,
            single_margin=0,
            new_client_position='after_current',
            border_focus=self.colors.green[0],
            border_normal=self.colors.grey[0],
            border_width=1,
            single_border_width=1,
            ratio=0.65,
            max_ratio=0.75,
            min_ratio=0.25,
            change_ratio=0.05,
            change_size=20,
            min_secondary_size=85
        )

    def get_testing(self):

        return [
            self.col_test(),
            self.monad_test(),
        ]


    def max(self):

        return Max(
            name=""
        )

    def master_pane(self):

        return MonadTall(
            name=self.icon_monad,
            align=MonadTall._left,
            margin=0,
            single_margin=0,
            new_client_position='after_current',
            border_focus=self.colors.green[0],
            border_normal=self.colors.grey[0],
            border_width=1,
            single_border_width=1,
            ratio=0.60,
            max_ratio=0.75,
            min_ratio=0.25,
            change_ratio=0.05,
            change_size=20,
            min_secondary_size=85
        )

    def master_pane_spacer(self):

        return MonadTall(
            name=self.icon_monad,
            align=MonadTall._left,
            margin=6,
            single_margin=6,
            new_client_position='after_current',
            border_focus=self.colors.green[0],
            border_normal=self.colors.grey[0],
            border_width=1,
            single_border_width=1,
            ratio=0.58
        )

    def two_stack(self):

        return Columns(
            name="舘",
            border_focus=self.colors.green[0], #‘Border colour for the focused window.’
            border_normal=self.colors.grey[0], #‘Border colour for un-focused windows.’
            border_focus_stack=self.colors.green[0], #‘Border colour for the focused window in stacked columns.’
            border_normal_stack=self.colors.grey[0], #‘Border colour for un-focused windows in stacked columns.’
            border_width=1,
            #insert_position=0,
            #split=True, #‘New columns presentation mode.’
            #wrap_focus_columns=True, #‘Wrap the screen when moving focus across columns.’
            #wrap_focus_rows=True, #‘Wrap the screen when moving focus across rows.’
            #wrap_focus_stacks=True, #‘Wrap the screen when moving focus across stacked.’
        )

    def get_default(self):

        return [
            self.master_pane(),
            self.max(),
        ]

    def get_spacer(self):

        return [
            self.master_pane_spacer(),
            self.max(),
        ]

    def get_fullscreen(self):

        return [
            self.max(),
        ]

    def get_layout(self, layoutType):

        switcher = {
            LayoutType.DEFAULT: self.get_default(),
            LayoutType.SPACER: self.get_spacer(),
            LayoutType.FULLSCREEN: self.get_fullscreen(),
            LayoutType.TESTING: self.get_testing()
        }

        return switcher.get(layoutType, self.get_default())
