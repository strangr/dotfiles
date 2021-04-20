from Helpers import Helpers

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

#from widgets import update_kbd_layout

import os

terminal = "urxvt"

mod = "mod4"
shift = "shift"
control = "control"
caps = "mod3"

homeDir = os.path.expanduser('~')

#@lazy.function
# TODO move inside helpers
def go_to_screen(num):
    def f(qtile):
        qtile.cmd_to_screen(num)

    return f

keys = [

    # Window Controls
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod, shift], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displtayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Qtile Controls
    Key([mod, shift], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, control], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move focus next"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    #
    Key([], "ISO_Next_Group", lazy.function(Helpers.update_kbd_layout())),

    # Screen Navigation
    Key([mod], "s", lazy.function(go_to_screen(0))),
    Key([mod], "d", lazy.function(go_to_screen(1))),

    # Utils
    Key([mod, shift], "period", lazy.spawn("changeVolume plus"), desc="Increase Sound"),
    Key([mod, shift], "comma", lazy.spawn("changeVolume minus"), desc="Decrease Sound"),
    Key([mod, shift], "m", lazy.spawn("changeVolume mute"), desc="Mute"),
    Key([mod, shift], "n", lazy.spawn("changeVolume 120"), desc="120"),
    # @TODO mute/unmute mic

    # ROFI
    Key([mod], "p", lazy.spawn("rofi -show run"), desc="Application Launcher"),
    Key([mod], "g", lazy.spawn("rofimoji --prompt=Type"), desc="Insert Emoji"),

    # Screenshots
    Key([], "Print", lazy.spawn("scrot " + homeDir + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot"),
    Key(["shift"], "Print", lazy.spawn("scrot -s " + homeDir + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot Rectangle"),

    # Redshift
    Key([mod], "z", lazy.spawn("redshift -x"), lazy.spawn("redshift -O 4000"), desc="Redshift 4000"),
    Key([mod, shift], "z", lazy.spawn("redshift -x"), desc="Redshift Reset"),

    # TODO win+n new firefox window
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
