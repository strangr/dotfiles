from libqtile.config import ScratchPad, DropDown, Key
from libqtile.command import lazy

class QScratchPad:

    rect_small = dict(
        opacity=0.9,
        height=0.6,
        width=0.7,
        x=0.15,
        y=0.01
    )

    rect_large = dict(
        opacity=0.9,
        height=0.8,
        width=0.8,
        x=0.1,
        y=0.1
    )

    def init_scratchpads(self, terminal):
        return [
            ScratchPad("scratchpad", [
                DropDown("terminal-scratch",
                    terminal + " -name term-scratch",
                    **self.rect_small,
                    on_focus_lost_hide=False
                ),

                DropDown("ranger-scratch",
                    terminal + " -name ranger-scratch -e ranger",
                    **self.rect_large,
                    on_focus_lost_hide=False
                ),

                DropDown("pavucontrol-scratch",
                    "pavucontrol",
                    **self.rect_small,
                    on_focus_lost_hide=True
                )
            ])
        ]

    def init_keys(self, mod):
        return [
            # @TODO if already displayed on this screen, focus it
            Key([], 'F8', lazy.group['scratchpad'].dropdown_toggle('ranger-scratch'), desc="Toggle Ranger"),
            Key([], 'F7', lazy.group['scratchpad'].dropdown_toggle('pavucontrol-scratch'), desc="Toggle PavuControl"),
            Key([], 'F10', lazy.group['scratchpad'].dropdown_toggle('terminal-scratch'), desc="Toggle Terminal")
        ]
