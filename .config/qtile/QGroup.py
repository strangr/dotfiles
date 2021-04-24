from enum import Enum

class LayoutType(Enum):
    DEFAULT = 1
    SPACER = 2
    FULLSCREEN = 3
    TESTING = 4

class MatchType(Enum):
    DEFAULT = 1
    CHAT = 2
    WORKCHAT = 3

class QGroup:

    name = ""
    layout_type = ""
    match_type = ""

    def __init__(self, name, layout = LayoutType.DEFAULT, match = MatchType.DEFAULT):
        self.name = name
        self.layout_type = layout
        self.match_type = match
