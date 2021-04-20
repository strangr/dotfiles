from QLayouts import QLayouts

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

#from typing import List  # noqa: F401
#from keys import keys, mod
#import re

#●雷綠祿
#僧
#类﩯舘麗
#ﰧﳶ
#﵁恵頻侀𤋮全充

# @TODO groups w,e will have gaps
class QGroups:

    mod = "mod4"

    dilam_l = []
    dilam_r = []

    qlayous = QLayouts()
    q_default_layouts = [
        qlayous.max(),
        qlayous.two_stack_new()
    ]

    def __init__(self, l, r):
        self.dilam_l = l
        self.dilam_r = r

    group_matches = [
        None, None, None, None, None, None,
        [Match(wm_class=[
            "discord",
        ]), ],
        [Match(wm_class=[
            "slack", "microsoft teams - preview",
        ]), ],
        None,None,
    ]

    def init_left_groups(self):
        result = []
        for i in range(len(self.dilam_l)):
            result.append(
                Group(
                    name=self.dilam_l[i],
                    #matches=group_matches[i],
                    #exclusive=group_exclusives[i],
                    layouts=self.q_default_layouts,
                    init=True,
                    persist=True,
                    label=""
                ))

        return result

    # @TODO groups w,e will have gaps
    def init_right_groups(self):
        result = []
        for i in range(len(self.dilam_r)):
            result.append(
                Group(
                    name=self.dilam_r[i],
                    #matches=group_matches[i],
                    #exclusive=group_exclusives[i],
                    layouts=self.q_default_layouts,
                    init=True,
                    persist=True,
                    label=""
                ))

        return result

    #TODO if already on that group in that screen, dont switch group or else it moves to prev group
    def init_keys2(self):
        # @TODO groups w,e will have gaps
        keys = []

        for i in self.dilam_l:
            keys.extend([
                Key([self.mod], i, lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 1".format(str(i))),
                Key([self.mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(0), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 1".format(str(i))),
            ])

        for i in self.dilam_r:
            keys.extend([
                Key([self.mod], i, lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Switch to group {} on screen 2".format(str(i))),
                Key([self.mod, 'shift'], i, lazy.window.togroup(i), lazy.to_screen(1), lazy.group[str(i)].toscreen(), desc="Shift to group {} on screen 2".format(str(i))),
            ])

        return keys


# def init_groups(self):
#     return [
#         Group("1",
#             layouts = self.q_default_layouts,
#         ),
#         Group("2",
#             layouts = self.q_default_layouts,
#         ),
#     ]

# return [
#     Group("SYS",
#         layouts = q_default_layouts,
#     ),
#     Group("CLI",
#         layouts = q_default_layouts,
#         matches = []
#     ),
#     Group("TYP",
#         layouts = q_default_layouts,
#         matches = []
#     ),
#     Group("VRT",
#         layouts = q_default_layouts,
#         matches = []
#     ),
#     Group("MNG",
#         layouts = q_default_layouts,
#         matches = []
#     ),

#     Group("AUX",
#         layouts = q_default_layouts
#     ),
#     Group("DOC",
#         layouts = q_default_layouts,
#         matches = [
#             Match(wm_class = [
#                 "Zathura",
#                 "Evince"
#             ])
#         ]
#     ),
#     Group("OFC",
#         layouts = q_default_layouts,
#         matches = [
#             Match(wm_class = [
#                 "calibre",
#                 re.compile("NetBeans")
#             ]),
#             Match(title = [re.compile("LibreOffice")])
#         ]
#     ),
#     Group("GPX",
#         layouts = q_default_layouts,
#         matches = []
#     ),
#     Group("TCM",
#         layouts = q_default_layouts,
#         matches = []
#     ),
#     Group("", layouts = q_default_layouts)
# ]
