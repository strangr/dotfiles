from QScreens import QScreens
from QGroups import QGroups

from keys import keys, mouse

from typing import List  # noqa: F401
from libqtile import layout, hook
from libqtile.config import Match

from libqtile.config import Group, Key
from libqtile.lazy import lazy


import os
import subprocess

#@TODO try catch
if __name__ in ["config", "__main__"]:

    homeDir = os.path.expanduser('~')

    #groupsPerPage = 5
    #TODO make them into dicts with basic configs
    # ex: name,
    #     label,
    #       layout_style=spacer
    #       layout_match=chat

    left_groups = ["1","2","3","4","grave"]
    right_groups = ["q","w","e","r","t"]


    qScreens = QScreens()
    qGroups = QGroups(left_groups, right_groups)
    
    groups = []
    groups += qGroups.init_left_groups()
    groups += qGroups.init_right_groups()


    screens = qScreens.init_dual_screen_bar()

    keys += qGroups.init_keys2()


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
