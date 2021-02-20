---------------------------------------------------------------------------
--                                                                       --
--     _|      _|  _|      _|                                      _|    --
--       _|  _|    _|_|  _|_|    _|_|    _|_|_|      _|_|_|    _|_|_|    --
--         _|      _|  _|  _|  _|    _|  _|    _|  _|    _|  _|    _|    --
--       _|  _|    _|      _|  _|    _|  _|    _|  _|    _|  _|    _|    --
--     _|      _|  _|      _|    _|_|    _|    _|    _|_|_|    _|_|_|    --
--                                                                       --
---------------------------------------------------------------------------
-- strangr
-- https://github.com/strangr
-- xmonad 0.15
--

import Data.Monoid
import System.Exit
import System.IO

import XMonad

import XMonad.Util.Run(spawnPipe)
import XMonad.Util.Paste

import XMonad.Hooks.ManageDocks
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.DynamicLog as DL
import XMonad.Actions.OnScreen


-- experimentals
-- import XMonad.Layout.SimpleFloat
-- import XMonad.Layout.Spacing
-- import XMonad.Layout.Named
import XMonad.Layout.NoBorders

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

-- The preferred terminal program, which is used in a binding below and by
-- certain contrib modules.
--
myTerminal      = "urxvt"

-- Whether focus follows the mouse pointer.
myFocusFollowsMouse :: Bool
myFocusFollowsMouse = False

-- Whether clicking on a window to focus also passes the click to the window
myClickJustFocuses :: Bool
myClickJustFocuses = False

-- Width of the window border in pixels.
--
myBorderWidth   = 1

-- modMask lets you specify which modkey you want to use. The default
-- is mod1Mask ("left alt").  You may also consider using mod3Mask
-- ("right alt"), which does not conflict with emacs keybindings. The
-- "windows key" is usually mod4Mask.
--
-- myModMask       = mod1Mask
winKey :: KeyMask
winKey = mod4Mask
myModMask       = winKey
-- The default number of workspaces (virtual screens) and their names.
-- By default we use numeric strings, but any string may be used as a
-- workspace name. The number of workspaces is determined by the length
-- of this list.
--
-- A tagging example:
--
-- > workspaces = ["web", "irc", "code" ] ++ map show [4..9]
--
--myWorkspaces    = ["1","2","3","4","5","6","7","8","9"]
--myWorkspaces    = ["1","2","3","4","5","6","7","8","9"]

-- myWorkspaces1,myWorkspaces2 :: [String]
-- myWorkspaces1 = ["web1", "2", "3", "4"]
-- myWorkspaces2 = ["web2", "2", "3", "4"]

-- @TODO maybe I can remake this into a list of tags so I can get rid of independed screens

-- Name workspaces (@TODO change names to better fit my new workflow)
-- # Monitor 1
ws1 = "1:www"
ws2 = "2:work"
ws3 = "3:terms"
ws4 = "4:mics"
ws5 = "5:chat"

-- # Monitor 2
wsF1 = "F1:/usr/www"
wsF2 = "F2:/usr/terms"
wsF3 = "F3:/usr/chat"
wsF4 = "F4:/wrk/chat"
wsF5 = "F5:f5"

workspacesLeft  = [ws1,  ws2,  ws3,  ws4,  ws5]
workspacesRight = [wsF1, wsF2, wsF3, wsF4, wsF5]
myWorkspaces = workspacesLeft ++ workspacesRight

-- Border colors for unfocused and focused windows, respectively.
--
myNormalBorderColor  = "#333333"
myFocusedBorderColor = "#00CC00"

------------------------------------------------------------------------
-- Key bindings. Add, modify or remove key bindings here.
--
myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    -- launch a terminal
    [ ((modm .|. shiftMask, xK_Return), spawn $ XMonad.terminal conf)

    -- launch rofi
    , ((modm,               xK_p     ), spawn "rofi -show run")

    -- close focused window
    , ((modm .|. shiftMask, xK_c     ), kill)

     -- Rotate through the available layout algorithms
    , ((modm,               xK_space ), sendMessage NextLayout)

    --  Reset the layouts on the current workspace to default
    , ((modm .|. shiftMask, xK_space ), setLayout $ XMonad.layoutHook conf)

    -- Resize viewed windows to the correct size
    , ((modm,               xK_n     ), refresh)

    -- Move focus to the next window
    , ((modm,               xK_Tab   ), windows W.focusDown)

    -- Move focus to the next window
    , ((modm,               xK_j     ), windows W.focusDown)

    -- Move focus to the previous window
    , ((modm,               xK_k     ), windows W.focusUp  )

    -- Move focus to the master window
    , ((modm,               xK_m     ), windows W.focusMaster  )

    -- Swap the focused window and the master window
    , ((modm,               xK_Return), windows W.swapMaster)

    -- Swap the focused window with the next window
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown  )

    -- Swap the focused window with the previous window
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp    )

    -- Shrink the master area
    , ((modm,               xK_h     ), sendMessage Shrink)

    -- Expand the master area
    , ((modm,               xK_l     ), sendMessage Expand)

    -- Push window back into tiling
    , ((modm,               xK_t     ), withFocused $ windows . W.sink)

    -- Increment the number of windows in the master area
    , ((modm              , xK_comma ), sendMessage (IncMasterN 1))

    -- Deincrement the number of windows in the master area
    , ((modm              , xK_period), sendMessage (IncMasterN (-1)))

    -- Toggle the status bar gap
    -- Use this binding with avoidStruts from Hooks.ManageDocks.
    -- See also the statusBar function from Hooks.DynamicLog.
    --
    , ((modm           , xK_b        ), sendMessage ToggleStruts)

    -- Quit xmonad (@TEMP ASSIGNMENT SINCE I ALWAY PRESS IT OUT OF HABBIT)
    , ((modm .|. shiftMask, xK_o     ), io (exitWith ExitSuccess))

    -- Restart xmonad
    , ((modm,               xK_q     ), spawn "xmonad --recompile; xmonad --restart")

    -- X-selection-paste buffer (@TODO replace with ctrl+shift+v for better one hand handling)
    , ((0,                  xK_Insert), pasteSelection)

    -- Screenshots
    , ((0,                  xK_Print),  spawn "scrot $HOME/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png")
    , ((shiftMask,          xK_Print),  spawn "scrot -s $HOME/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png")

    , ((modm ,              xK_1),         windows (viewOnScreen 0 ws1))
    , ((modm ,              xK_2),         windows (viewOnScreen 0 ws2))
    , ((modm ,              xK_3),         windows (viewOnScreen 0 ws3))
    , ((modm ,              xK_4),         windows (viewOnScreen 0 ws4))
    , ((modm ,              xK_5),         windows (viewOnScreen 0 ws5))

    , ((modm ,              xK_F1),        windows (viewOnScreen 1 wsF1))
    , ((modm ,              xK_F2),        windows (viewOnScreen 1 wsF2))
    , ((modm ,              xK_F3),        windows (viewOnScreen 1 wsF3))
    , ((modm ,              xK_F4),        windows (viewOnScreen 1 wsF4))
    , ((modm ,              xK_F5),        windows (viewOnScreen 1 wsF5))

    , ((modm .|. shiftMask, xK_1),         windows $ shiftThenView 0 ws1)
    , ((modm .|. shiftMask, xK_2),         windows $ shiftThenView 0 ws2)
    , ((modm .|. shiftMask, xK_3),         windows $ shiftThenView 0 ws3)
    , ((modm .|. shiftMask, xK_4),         windows $ shiftThenView 0 ws4)
    , ((modm .|. shiftMask, xK_5),         windows $ shiftThenView 0 ws5)

    , ((modm .|. shiftMask, xK_F1),        windows $ shiftThenView 1 wsF1)
    , ((modm .|. shiftMask, xK_F2),        windows $ shiftThenView 1 wsF2)
    , ((modm .|. shiftMask, xK_F3),        windows $ shiftThenView 1 wsF3)
    , ((modm .|. shiftMask, xK_F4),        windows $ shiftThenView 1 wsF4)
    , ((modm .|. shiftMask, xK_F5),        windows $ shiftThenView 1 wsF5)
    ]

    ++

    --
    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    --
    -- @TODO follow shift here
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]
    where
        shiftThenView scrnid wsid = (viewOnScreen scrnid wsid) . (W.shift wsid)

------------------------------------------------------------------------
-- Mouse bindings: default actions bound to mouse events
--
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))

    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))

    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))

    -- you may also bind events to the mouse scroll wheel (button4 and button5)
    ]

------------------------------------------------------------------------
-- Layouts:

-- You can specify and transform your layouts by modifying these values.
-- If you change layout bindings be sure to use 'mod-shift-space' after
-- restarting (with 'mod-q') to reset your layout state to the new
-- defaults, as xmonad preserves your old layout settings by default.
--
-- The available layouts.  Note that each layout is separated by |||,
-- which denotes layout choice.
--
myLayout = avoidStruts $ smartBorders (tiled ||| Mirror tiled ||| Full)
  where
    -- default tiling algorithm partitions the screen into two panes
    -- tiled   = spacingRaw False (Border 10 0 10 0) True (Border 0 10 0 10) True $ Tall nmaster delta ratio
    tiled   = Tall nmaster delta ratio

    -- The default number of windows in the master pane
    nmaster = 1

    -- Percent of screen to increment by when resizing panes
    delta   = 3/100

    -- Default proportion of screen occupied by master pane
    ratio   = 1/2

    -- float = named "Float" simpleFloat

------------------------------------------------------------------------
-- Window rules:

-- Execute arbitrary actions and WindowSet manipulations when managing
-- a new window. You can use this to, for example, always float a
-- particular program, or have a client always appear on a particular
-- workspace.
--
-- To find the property name associated with a program, use
-- > xprop | grep WM_CLASS
-- and click on the client you're interested in.
--
-- To match on the WM_NAME, you can use 'title' in the same way that
-- 'className' and 'resource' are used below.
--
myManageHook = composeAll
    [ isFullscreen                  --> doFullFloat
    --, manageDocks
    , isDialog                      --> doCenterFloat
    , className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , className =? "Pavucontrol"    --> doFloat
    , className =? "vlc"            --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore
    , className =? "stalonetray"    --> doIgnore
    ]

 -- myManageHook ::  ManageHook
 -- myManageHook = composeAll . concat $
 --     [
 --      [isDialog --> doCenterFloat]
 --    --, [ isFullscreen --> (doF W.focusDown <+> doFullFloat) ]
 --    , [ isFullscreen --> doFullFloat ]
 --    --, [ composeOne [ isFullscreen -?> doFullFloat ] ]
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doIgnore         | c <- bars ]
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doFloat          | c <- float    ]
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doCenterFloat        | c <- cfloat   ]
 --        , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 0)  | c <- main ]   -- i
 --        , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 1)  | c <- www  ]   -- ii
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 2)  | c <- office   ]   -- iii
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 3)  | c <- rdp  ]   -- iv
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 4)  | c <- file ]   -- v
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 5)  | c <- email    ]   -- vi
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 6)  | c <- editor   ]   -- vii
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 7)  | c <- media    ]   -- vii
 --    , [(className =? c <||> title =? c <||> resource =? c) --> doShift (myWorkspaces !! 8)  | c <- chat ]   -- ix
 --    , [role =? c --> doFloat | c <- im ]    -- place roles on im
 --    ]
 --    where   
 --        bars    = ["xmobar","dzen2","desktop_window"]
 --        float   = ["feh"]
 --        cfloat  = ["Xmessage","Gxmessage","Eog","Xscreensaver-demo","Brasero","xclock","Xscreensaver-demo","xfreerdp"]
 --            ++ ["SimpleScreenRecorder","Evolution-alarm-notify","Evolution","Gns3","Mtpaint"]
 --        main    = ["Wine","Pidgin","Skype"]
 --        media   = ["Pithos","Ario","Vlc","Ncmpcpp"]
 --        www = ["Chromium"]
 --        rdp = ["xfreerdp","rdesktop"]
 --        office  = ["libreoffice-calc","libreoffice-writer","VirtualBox","libreoffice"]
 --        editor  = ["Gvim","Xconfigs"]
 --        email   = ["Evolution"]
 --        file    = ["Brasero","spacefm","Xpdf"]
 --        chat    = ["Xchat","Gimp"]
 --        im  = ["nothing"]
 --        role    = stringProperty "WM_WINDOW_ROLE"


------------------------------------------------------------------------
-- Event handling

-- * EwmhDesktops users should change this to ewmhDesktopsEventHook
--
-- Defines a custom handler function for X Events. The function should
-- return (All True) if the default handler is to be run afterwards. To
-- combine event hooks use mappend or mconcat from Data.Monoid.
--
myEventHook = fullscreenEventHook

------------------------------------------------------------------------
-- Status bars and logging

-- Perform an arbitrary action on each internal state change or X event.
-- See the 'XMonad.Hooks.DynamicLog' extension for examples.
--
-- myLogHook = return ()
-- myLogHook = dynamicLog

------------------------------------------------------------------------
-- Startup hook

-- Perform an arbitrary action each time xmonad starts or is restarted
-- with mod-q.  Used by, e.g., XMonad.Layout.PerWorkspace to initialize
-- per-workspace layout choices.
--
-- By default, do nothing.
myStartupHook = return ()

------------------------------------------------------------------------
main = do
    xmproc0 <- spawnPipe "xmobar -x 0 ~/.xmonad/xmobarrc"
    xmproc1 <- spawnPipe "xmobar -x 1 ~/.xmonad/xmobarrc"
    xmonad $ docks
           $ ewmh
           $ def {
        -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

        -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

        -- hooks, layouts
        layoutHook         = myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        startupHook        = myStartupHook,
        logHook            = DL.dynamicLogWithPP $ xmobarPP
                             { DL.ppOutput  = \x-> hPutStrLn xmproc0 x >> hPutStrLn xmproc1 x
                             , DL.ppTitle   = DL.xmobarColor "#00CC00" "" . DL.shorten 50
                             , DL.ppCurrent = \x -> "[" ++ x ++ "]"
                             }
        }
------------------------------------------------------------------------
-- , DL.ppVisible = DL.xmobarColor "#fffff0" ""
-- , DL.ppCurrent = DL.xmobarColor "#60ff45" ""
