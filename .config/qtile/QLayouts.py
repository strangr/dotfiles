from libqtile.layout.max import Max
from libqtile.layout.zoomy import Zoomy
# from libqtile.layout.stack import Stack
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
# from libqtile.layout.xmonad import MonadTall, MonadWide

# class Layout_Aesthetics(object):

#   layout_theme = {
#       "margin":           2,
#       "border_width":     2,
#       "border_focus":     "0000FF",
#       "border_normal":    "000000",
#   }

#   floating_layout = Floating(
#       border_width =  2,
#       border_focus =  "0000FF",
#       border_normal = "000000",
#   )


# layouts = [
#     layout.Columns(
#         name="舘",
#         border_focus='#881111', #‘Border colour for the focused window.’
#         border_normal='#220000', #‘Border colour for un-focused windows.’
#         border_focus_stack='#d75f5f', #‘Border colour for the focused window in stacked columns.’
#         border_normal_stack='#220000', #‘Border colour for un-focused windows in stacked columns.’
#         border_width=1,
#         #insert_position=0,
#         #split=True, #‘New columns presentation mode.’
#         #wrap_focus_columns=True, #‘Wrap the screen when moving focus across columns.’
#         #wrap_focus_rows=True, #‘Wrap the screen when moving focus across rows.’
#         #wrap_focus_stacks=True, #‘Wrap the screen when moving focus across stacked.’
#     ),
#     #layout.MonadTall(name=""),
#     layout.Max(name=""),
#     # Try more layouts by unleashing below layouts.
#     # layout.Stack(num_stacks=2),
#     # layout.Bsp(),
#     # layout.Matrix(),
#     # layout.MonadTall(),
#     # layout.MonadWide(),
#     # layout.RatioTile(),
#     # layout.Tile(),
#     # layout.TreeTab(),
#     # layout.VerticalTile(),
#     # layout.Zoomy(),
# ]

class QLayouts(object):

    #theme = Layout_Aesthetics.layout_theme

    # def max(self, name = None):
    #   if name is None:
    #       return Max(**self.theme)

    #   return Max(name = name, **self.theme)

    # def two_stack_new(self, name = None):
    #   if name is None:
    #       return Columns(num_columns = 2, split = False, **self.theme)

    #   return Columns(name = name, num_columns = 2, split = False, **self.theme)

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
