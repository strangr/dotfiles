class Colors:

    black       = "#282425"
    white       = "#C0C5CE"
    red         = "#BF616A"
    green       = "#99b9ac"
    yellow      = "#d8c9aa"
    grey        = "#766a5a"
    transparent = "#00000000"

class Fonts:

    base = "sans"
    bold = "sans"

class QDefaults:

    # @TODO use this as defaults for layouts
    layout_theme = {
        "margin":           0,
        "border_width":     1,
        "border_focus":     Colors.green,
        "border_normal":    Colors.grey,
    }

    floating_layout = dict(
        border_width =  1,
        border_focus =  Colors.green,
        border_normal = Colors.black,
        fullscreen_border_width = 0
    )

    widget_defaults = dict(
        font        = Fonts.base,
        fontsize    = 12,
        padding     = 3,
        foreground  = Colors.yellow
    )

    extension_defaults = widget_defaults.copy()
