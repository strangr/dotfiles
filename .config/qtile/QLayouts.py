from libqtile.layout.max import Max
from libqtile.layout.columns import Columns

class QLayouts(object):

    def max(self):
        return Max(name="")

    def two_stack_new(self):
        return Columns(
            name="舘",
            border_focus='#881111', #‘Border colour for the focused window.’
            border_normal='#220000', #‘Border colour for un-focused windows.’
            border_focus_stack='#d75f5f', #‘Border colour for the focused window in stacked columns.’
            border_normal_stack='#220000', #‘Border colour for un-focused windows in stacked columns.’
            border_width=1,
            #insert_position=0,
            #split=True, #‘New columns presentation mode.’
            #wrap_focus_columns=True, #‘Wrap the screen when moving focus across columns.’
            #wrap_focus_rows=True, #‘Wrap the screen when moving focus across rows.’
            #wrap_focus_stacks=True, #‘Wrap the screen when moving focus across stacked.’
        )

    def get_defaults(self):
        return [
            self.two_stack_new(),
            self.max(),
        ]
