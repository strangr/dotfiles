from enum import Enum

class LayoutType(Enum):
    NORMAL = 1
    SPACER = 2
    FULLSCREEN = 3

class MatchType(Enum):
    NORMAL = 1
    CHAT = 2
    WORKCHAT = 3

class QGroup:

    name = ""
    layout_type = ""
    match_type = ""

    def __init__(self, name, layout=LayoutType.NORMAL, match=MatchType.NORMAL):
        self.name = name
        self.layout_type = layout
        self.match_type = match
