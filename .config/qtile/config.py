# Qtile config
# for rangr

from QBindings import QKeys, QMouse
from QScreen import QScreen
from QGroups import QGroups
from QGroup import QGroup, LayoutType, MatchType
from QScratchPad import QScratchPad
from QTheme import QDefaults
from QRules import QRules

from libqtile.layout import Floating
from libqtile import hook

from typing import List  # noqa: F401

import os
import subprocess

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
        QGroup("w", layout=LayoutType.SPACER, match=MatchType.CHAT),
        QGroup("e", layout=LayoutType.SPACER, match=MatchType.WORKCHAT),
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
    #subscribe.client_urgent_hint_changed(func)
    #this should help me with teams

    def update_sticky_group():
        # for grupo in qtile.groups:
        #     for window in grupo.windows:
        windows = qtile.windows_map.values()
        for window in windows:
            if 'sticky' not in window.cmd_hints():
                continue

            screen_id = window.hints["sticky"]
            if qtile.current_screen.index != screen_id:
                continue

            cw = qtile.groups.index(qtile.current_group)
            window.togroup(qtile.groups[cw].name)

    def update_sticky_focus():
        # for grupo in qtile.groups:
        #     for window in grupo.windows:
        windows = qtile.windows_map.values()
        for window in windows:
            if 'sticky' in window.cmd_hints():
                window.cmd_bring_to_front()

    def update_group_labels():
        #●雷綠祿
        for group in qtile.groups:
            number_of_windows = len(group.windows)
            current_groups = [screen.group.name for screen in qtile.screens if screen.group]
            label = ""
            if number_of_windows > 0 or group.name in current_groups:
                label = ""

            if group.label != label:
                group.cmd_set_label(label)

    # dont like bash for init
    # make startuponce my own method
    @hook.subscribe.startup_once
    def startup_once():
        home = os.path.expanduser('~')
        subprocess.call([home + '/.config/qtile/autostart.sh'])

    @hook.subscribe.setgroup
    def setgroup():
        update_sticky_group()
        update_group_labels()

    # @todo group_window_add - maybe this hook is better
    @hook.subscribe.client_managed
    def client_managed(window):
        update_group_labels()

    @hook.subscribe.focus_change
    def focus_change():
        update_sticky_focus()
