from libqtile.config import ScratchPad, DropDown, Key
from libqtile.command import lazy

class QScratchPad:

    rect_small = dict(
        opacity=0.9,
        height=0.5,
        width=0.5,
        x=0.25,
        y=0.25
    )

    rect_large = dict(
        opacity=0.9,
        height=0.8,
        width=0.8,
        x=0.1,
        y=0.1
    )

    def init_scratchpads(self):
        return [
            ScratchPad("scratchpad", [
                DropDown("terminal-scratch",
                    "urxvt -name term-scratch",
                    **self.rect_small,
                    on_focus_lost_hide=False),

                DropDown("ranger-scratch",
                    "urxvt -name ranger-scratch -e ranger",
                    **self.rect_large,
                    on_focus_lost_hide=False),

                DropDown("pavucontrol-scratch",
                    "pavucontrol",
                    **self.rect_small,
                    on_focus_lost_hide=True),
            ])
        ]

    def init_keys(self):
        return [
            Key([], 'F8', lazy.group['scratchpad'].dropdown_toggle('ranger-scratch')),
            Key([], 'F9', lazy.group['scratchpad'].dropdown_toggle('pavucontrol-scratch')),
            Key([], 'F10', lazy.group['scratchpad'].dropdown_toggle('terminal-scratch')),
        ]
