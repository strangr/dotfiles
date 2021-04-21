class Colors:

    black   = ["#282425"]
    white   = ["#C0C5CE"]
    red     = ["#BF616A"]
    green   = ["#99b9ac"]
    yellow  = ["#d8c9aa"]
    grey    = ["#766a5a"]

class Fonts:

    base = "sans"
    bold = "sans"

class QDefaults:

    layout_theme = {
        "margin":           2,
        "border_width":     2,
        "border_focus":     Colors.green[0],
        "border_normal":    Colors.black[0],
    }

    floating_layout = dict(
        border_width =  1,
        border_focus =  Colors.green[0],
        border_normal = Colors.black[0],
        fullscreen_border_width = 0
    )

    widget_defaults = dict(
        font        = Fonts.base,
        fontsize    = 12,
        padding     = 3,
        foreground  = Colors.yellow[0]
    )

    extension_defaults = widget_defaults.copy()