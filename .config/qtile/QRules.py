from QGroup import MatchType

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
            Match(wm_class='vlc'),
            Match(wm_class='org.remmina.Remmina'),
            Match(title='branchdialog'),
            Match(title='pinentry'),
        ]

    def get_match(self, matchType):

        switcher = {
            MatchType.DEFAULT: self.get_default(),
            MatchType.CHAT: self.get_chat_match(),
            MatchType.WORKCHAT: self.get_work_chat_match(),
        }

        return switcher.get(matchType, self.get_default())

    def get_default(self):

        return None

    def get_chat_match(self):

        return [
            Match(wm_class = ["discord"]),
            Match(wm_class = ["signal"]),
        ]

    def get_work_chat_match(self):

        return [
            Match(wm_class = ["slack"]),
            Match(wm_class = ["microsoft teams - preview"])
        ]
