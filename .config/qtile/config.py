from QBindings import QKeys, QMouse
from QScreen import QScreen
from QGroups import QGroups
from QGroup import QGroup, LayoutType, MatchType
from QScratchPad import QScratchPad
from QTheme import QDefaults
from QRules import QRules

from typing import List  # noqa: F401

from libqtile.layout import Floating
from libqtile import hook

import os
import subprocess

#僧
#类﩯舘麗
#ﰧﳶ
#﵁恵頻侀𤋮全充

# @TODO groups w,e will have gaps
# @TODO try catch
if __name__ in ["config", "__main__"]:

    mod = "mod4"
    terminal = "urxvt"
    
    left_groups = [
        QGroup("1"),
        QGroup("2", layout=LayoutType.FULLSCREEN),
        QGroup("3"),
        QGroup("4"),
        QGroup("grave")
    ]

    right_groups = [
        QGroup("q"),
        QGroup("w", match=MatchType.CHAT),
        QGroup("e", match=MatchType.WORKCHAT),
        QGroup("r"),
        QGroup("Tab")
    ]

    keys = []
    screens = []
    groups = []
    mouse = []

    qScreen = QScreen()
    qGroups = QGroups()
    qScratchPad = QScratchPad()
    qKeys = QKeys()
    qMouse = QMouse()
    qRules = QRules()

    screens += qScreen.init_dual_screen_bar(left_groups, right_groups)

    groups += qGroups.init_group(left_groups)
    groups += qGroups.init_group(right_groups)
    groups += qScratchPad.init_scratchpads(terminal)

    keys += qKeys.init_keys(mod, terminal)
    keys += qGroups.init_keys(mod, left_groups, 0)
    keys += qGroups.init_keys(mod, right_groups, 1)
    keys += qScratchPad.init_keys(mod)
    keys += qScreen.init_keys(mod)

    mouse += qMouse.init_mouse(mod)

    widget_defaults = QDefaults.widget_defaults
    extension_defaults = QDefaults.extension_defaults
    floating_layout = Floating(
        float_rules=qRules.init_floating_rules(),
        **QDefaults.floating_layout
    )

    auto_fullscreen     = True
    cursor_warp         = False
    follow_mouse_focus  = False
    reconfigure_screens = False
    auto_minimize       = False
    bring_front_click   = "floating_only"
    wmname              = "LG3D"

def main(qtile):

    # dont like bash for init
    # make startuponce my own method
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~')
        subprocess.call([home + '/.config/qtile/autostart.sh'])

    #●雷綠祿
    def update_group_labels():
        for group in qtile.groups:
            number_of_windows = len(group.windows)
            current_groups = [screen.group.name for screen in qtile.screens if screen.group]
            if number_of_windows > 0 or group.name in current_groups:
                group.cmd_set_label("")
            else:
                group.cmd_set_label("")

    @hook.subscribe.setgroup
    def group_change():
        update_group_labels()

    #subscribe.client_urgent_hint_changed(func)
    #this should help me with teams

    # @todo group_window_add - maybe this hook is better
    @hook.subscribe.client_managed
    def func(window):
        update_group_labels()
