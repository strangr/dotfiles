from libqtile.config import Match
from libqtile.layout import Floating

class QRules:

    def init_floating_rules(self):

        return [
            *Floating.default_float_rules,
            Match(wm_class='confirmreset'),
            Match(wm_class='makebranch'),
            Match(wm_class='maketag'),
            Match(wm_class='ssh-askpass'),
            Match(title='branchdialog'),
            Match(title='pinentry'),
        ]
