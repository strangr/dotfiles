#from typing import List  # noqa: F401
from libqtile import layout, hook
from libqtile.config import Match

import os
import subprocess

from groups import groups
from screens import screens
from keys import keys, mouse

homeDir = os.path.expanduser('~')

#
#
#
#
# 僧
#
#
#
#
#
#
#
#
#ﮑ
#ﲣ
#
#麗
#ﳶ
#僧
#类
#響頻恵𤋮舘﵁﩮﩯並况全ﰦ侀ﰧ充冀ﳼﰪ

layouts = [
    layout.Columns(name="",border_focus_stack='#d75f5f'),
    layout.MonadTall(name=""),
    layout.Max(name=""),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
    foreground = "#d8c9aa")
extension_defaults = widget_defaults.copy()







dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    subprocess.call([homeDir + '/.config/qtile/autostart.sh'])
