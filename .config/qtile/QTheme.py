from libqtile.layout.floating import Floating


class Colors:

    # Ocean
    black =     ["#2B303B", "#2B303B"]
    grey =      ["#40444D", "#424A5B"]
    lightgrey = ["#8E9299", "#8E9299"]
    white =     ["#C0C5CE", "#C0C5CE"]
    red =       ["#BF616A", "#BF616A"]
    magenta =   ["#B48EAD", "#B48EAD"]
    green =     ["#A3BE8C", "#A3BE8C"]
    darkgreen = ["#859900", "#859900"]
    blue =      ["#8FA1B3", "#8FA1B3"]
    darkblue =  ["#65737E", "#65737E"]
    orange =    ["#EBCB8B", "#EBCB8B"]

    #d8c9aa

class Fonts:

    base = "sans"
    bold = "sans"

class QDefaults:

    layout_theme = {
        "margin":           2,
        "border_width":     2,
        "border_focus":     Colors.blue[0],
        "border_normal":    Colors.black[0],
    }

    floating_layout = dict(
        border_width =  1,
        border_focus =  Colors.blue[0],
        border_normal = Colors.black[0],
        fullscreen_border_width = 0
    )

    widget_defaults = dict(
        font        = Fonts.base,
        fontsize    = 12,
        padding     = 3,
        foreground  = "#d8c9aa"
    )

    extension_defaults = widget_defaults.copy()