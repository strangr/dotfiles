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
import XMonad

import Data.Monoid
import System.Exit
import System.IO
import Control.Monad

import XMonad.Layout.NoBorders
import XMonad.Layout.Spacing
import XMonad.Layout.IndependentScreens
import XMonad.Layout.ToggleLayouts
import XMonad.Layout.PerWorkspace

import XMonad.Hooks.ManageDocks
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.DynamicLog as DL

import XMonad.Actions.OnScreen
import XMonad.Actions.CopyWindow

import XMonad.Util.Run(spawnPipe)
import XMonad.Util.SpawnOnce
import XMonad.Util.Paste
import XMonad.Util.NamedScratchpad

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

-----
-- https://wiki.haskell.org/Xmonad/General_xmonad.hs_config_tips#Skipping_the_Scratchpad_workspace_while_using_CycleWS
-- https://hackage.haskell.org/package/xmonad-contrib-0.16/docs/XMonad-Layout-LayoutCombinators.html
-- https://www.reddit.com/r/xmonad/comments/he6ezv/xmonad_xmobar_clickable_workspaces_help/
-- https://github.com/disconsis/literate-xmonad-config/blob/master/src/config.org#workspace-switch-buttons
-- https://gist.github.com/tylevad/3146111#file-xmonad-hs-L186 <- see how bindin works, per layout bindings
-- https://github.com/jaor/xmobar/blob/master/doc/quick-start.org
-- https://xiangji.me/2018/11/19/my-xmonad-configuration/
-----

------------------------------------------------------------------------
-- Some Defaults
------------------------------------------------------------------------

winKey :: KeyMask
winKey = mod4Mask

myModMask :: KeyMask
myModMask = winKey

myTerminal :: String
myTerminal = "urxvt"

-- Floating window sizes XXS XS S M L XL XXL XXXL
rectXL = (customFloating $ W.RationalRect (1/20) (1/20) (9/10) (9/10))
rectL  = (customFloating $ W.RationalRect (1/10) (1/10) (8/10) (8/10))
rectM  = (customFloating $ W.RationalRect (1/6) (1/6) (2/3) (2/3))
rectS  = (customFloating $ W.RationalRect (1/4) (1/4) (1/2) (1/2))

------------------------------------------------------------------------
-- Named workspaces (@TODO change names to better fit my new workflow)
------------------------------------------------------------------------

-- Monitor 1
ws1 = "0_1"
ws2 = "0_2"
ws3 = "0_3"
ws4 = "0_4"
ws5 = "0_5"

-- Monitor 2
wsF1 = "1_1"
wsF2 = "1_2"
wsF3 = "1_3"
wsF4 = "1_4"
wsF5 = "1_5"

d = M.fromList [ (ws1, "www")
               , (ws2, "work")
               , (ws3, "terms")
               , (ws4, "mics")
               , (ws5, "chat")
               ]

b = M.fromList [ (wsF1, "/usr/www")
               , (wsF2, "/usr/terms")
               , (wsF3, "/usr/chat")
               , (wsF4, "/wrk/chat")
               , (wsF5, "f5")
               ]


ddd = ["www", "dd", "bb"]

workspacesLeft  = [ws1, ws2, ws3, ws4, ws5]
workspacesRight = [wsF1, wsF2, wsF3, wsF4, wsF5]
myWorkspaces    = withScreens 2 ["1","2","3","4","5"]

------------------------------------------------------------------------
-- KEY BINDINGS
------------------------------------------------------------------------

myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    -- launch a terminal
    [ ((modm .|. shiftMask, xK_Return), spawn $ XMonad.terminal conf)

    ------------------------------------------------------------------------
    -- Control Workspace
    ------------------------------------------------------------------------

    -- close focused window
    , ((modm .|. shiftMask, xK_c     ), kill)

     -- Rotate through the available layout algorithms
    , ((modm,               xK_space ), sendMessage NextLayout)

    --  Reset the layouts on the current workspace to default
    , ((modm .|. shiftMask, xK_space ), setLayout $ XMonad.layoutHook conf)

    -- Set/Unset Full Layout
    , ((modm, xK_f), sendMessage (Toggle "Full"))

    -- Resize viewed windows to the correct size
    , ((modm,               xK_n     ), refresh)

    -- Move focus to the next window
    , ((modm,               xK_Tab   ), windows W.focusDown)

    -- Move focus to the previous window
    , ((modm .|. shiftMask, xK_Tab   ), windows W.focusUp)

    -- Move focus to the next window
    , ((modm,               xK_j     ), windows W.focusDown)

    -- Move focus to the previous window
    , ((modm,               xK_k     ), windows W.focusUp)

    -- Move focus to the master window
    , ((modm,               xK_m     ), windows W.focusMaster)

    -- Swap the focused window and the master window
    , ((modm,               xK_Return), windows W.swapMaster)

    -- Swap the focused window with the next window
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown)

    -- Swap the focused window with the previous window
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp)

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

    -- @TODO Sticky
    -- XMonad.Actions.CopyWindow
    -- To make it work first I have to determine current screen and then copy to only current screen workspaces
    -- , ((modm              , xK_a     ), windows copyToAll) -- Pin to all workspaces  (sticky)
    -- , ((modm .|. shiftMask, xK_a     ), killAllOtherCopies) -- remove window from all but current (remove sticky)
    --, ("M-S-a"          , kill1      ), -- remove window from current, kill if only one
    ------------------------------------------------------------------------
    -- Utils
    ------------------------------------------------------------------------

    -- Quit xmonad (@TEMP ASSIGNMENT SINCE I ALWAY PRESS IT OUT OF HABBIT) Make warning with rofi
    , ((modm .|. shiftMask, xK_o     ), io (exitWith ExitSuccess))
    -- Toggle the status bar gap
    , ((modm              , xK_b     ), sendMessage ToggleStruts)
    -- Restart xmonad
    , ((modm              , xK_q     ), spawn "xmonad --recompile; xmonad --restart")

    -- X-selection-paste buffer (@TODO replace with ctrl+shift+v for better one hand handling)
    , ((0                 , xK_Insert), pasteSelection)

    -- Scratchpads
    , ((0                 , xK_F10   ), namedScratchpadAction scratchpads "terminal-scratch")
    , ((0                 , xK_F9    ), namedScratchpadAction scratchpads "pavucontrol-scratch")
    , ((0                 , xK_F8    ), namedScratchpadAction scratchpads "ranger-scratch")

    ------------------------------------------------------------------------
    -- Launching Apps
    ------------------------------------------------------------------------

    -- launch rofi
    , ((modm              , xK_p     ), spawn "rofi -show run")

    -- Screenshots
    , ((0                 , xK_Print ), spawn "scrot $HOME/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png")
    , ((shiftMask         , xK_Print ), spawn "scrot -s $HOME/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png")

    -- Volume Control
    , ((modm .|. shiftMask, xK_period), spawn "~/bin/changeVolume plus")
    , ((modm .|. shiftMask, xK_comma ), spawn "~/bin/changeVolume minus")
    , ((modm .|. shiftMask, xK_m     ), spawn "~/bin/changeVolume mute")
    , ((modm .|. shiftMask, xK_n     ), spawn "~/bin/changeVolume 120")

    -- redshift -x; redshift -O 4000
    -- redshift -x

    ]

    ++

    [((m .|. modm, k), windows $ f i)
    | (i, k) <- zip workspacesLeft [xK_1 .. xK_5]
    , (f, m) <- [(viewOnScreen 0, 0), (shiftThenView 0, shiftMask)]]

    ++

    [((m .|. modm, k), windows $ f i)
    | (i, k) <- zip workspacesRight [xK_F1 .. xK_F5]
    , (f, m) <- [(viewOnScreen 1, 0), (shiftThenView 1, shiftMask)]]

    ++
    
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
    | (key, sc) <- zip [xK_w, xK_e] [0,1]
    , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]
    
    where shiftThenView scrnid wsid = (viewOnScreen scrnid wsid) . (W.shift wsid)

------------------------------------------------------------------------
-- MOUSE BINDINGS
------------------------------------------------------------------------

myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))
    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))

    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))
    ]

------------------------------------------------------------------------
-- LAYOUTS
------------------------------------------------------------------------

myLayout = avoidStruts $ smartBorders $ toggleLayouts Full workspaceLayouts

workspaceLayouts =
  onWorkspace wsF1 layoutTallSpaced $
  onWorkspace wsF2 layoutTallSpaced $
  layoutDefaults
  where
    layoutTallSpaced = spaceTiled
    layoutDefaults   = tiled ||| Mirror tiled

    tiled   = Tall nmaster delta ratio

    spaceTiled = spacingR $ Tall nmaster delta ratio

    -- The default number of windows in the master pane
    nmaster = 1

    -- Percent of screen to increment by when resizing panes
    delta   = 3/100

    -- Default proportion of screen occupied by master pane
    ratio   = 1/2

    spacingL = spacing 10
    spacingR = spacingRaw False (Border 10 0 10 0) True (Border 0 10 0 10) True

------------------------------------------------------------------------
-- WINDOW RULES
------------------------------------------------------------------------

myManageHook = composeAll
    [ isFullscreen                  --> doFullFloat
    --, manageDocks
    , isDialog                      --> doCenterFloat
    , className =? "feh"            --> rectS
    , className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , className =? "vlc"            --> rectS
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore
    , className =? "stalonetray"    --> doIgnore
    , className =? "discord"        --> doShift wsF2
    ] <+> namedScratchpadManageHook scratchpads <+> manageDocks

------------------------------------------------------------------------
-- SCRATCHPADS
------------------------------------------------------------------------

scratchpads :: [NamedScratchpad]
scratchpads = [
    NS "terminal-scratch" spawnTerminalScratch findTermScratch rectS,
    NS "ranger-scratch" spawnRangerScratch findRangerScratch rectL,
    NS "pavucontrol-scratch" spawnPavuScratch findPavuScratch rectS
  ] where
    spawnTerminalScratch = myTerminal ++ " -name term-scratch"
    spawnRangerScratch   = myTerminal ++ " -name ranger-scratch -e ranger"
    spawnPavuScratch     = "pavucontrol"

    findTermScratch      = resource =? "term-scratch"
    findRangerScratch    = resource =? "ranger-scratch"
    findPavuScratch      = resource =? "pavucontrol"

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
-- STARTUP HOOK (RUNS EVERYTIME WITH MOD-Q)
------------------------------------------------------------------------

myStartupHook :: X ()
myStartupHook = do
  spawnOnce "dunst &"

------------------------------------------------------------------------
-- Status bars and logging -- ● ○
------------------------------------------------------------------------

pp :: Handle -> ScreenId -> PP
pp h s = marshallPP s (namedScratchpadFilterOutWorkspacePP $ xmobarPP)
    { DL.ppCurrent          = \x -> clickable x "●" s
    , DL.ppVisible          = \x -> clickable x "●" s
    , DL.ppHidden           = \x -> clickable x "○" s
    , DL.ppHiddenNoWindows  = \x -> clickable x "○" s
    -- , DL.ppVisibleNoWindows = \x -> x
    , DL.ppUrgent           = \x -> "<fc=#FF0000>" ++ x ++ "</fc>"
    --, DL.ppSep = " "
    , DL.ppTitle            = DL.xmobarColor "#00CC00" "" . DL.shorten 50
    , DL.ppOrder            = \(ws:l:t:_) -> [ws ++ " : " ++ l]
    , DL.ppOutput           = hPutStrLn h
    , DL.ppLayout           = (\x -> case x of
        "Tall"        -> "[ | ]"
        "Mirror Tall" -> "[ - ]"
        "Full"        -> "[ X ]"
        _             -> x
        )
    }
    where color c = xmobarColor c ""

akaT :: String -> ScreenId -> String
akaT x s = ddd!!0

xmobarEscape :: String -> String
xmobarEscape = concatMap doubleLts
  where doubleLts '<' = "<<"
        doubleLts x   = [x]

-- clickable :: String -> ScreenId -> String
-- clickable d s = click (xmobarEscape d) s
--     where
--         click l@(x:xs) s = ("<action=xdotool key Super_L+1>"++ l ++"</action>")

clickable :: String -> String -> ScreenId -> String
clickable number symbol screen = click number symbol screen
    where
    click l@(x:xs) m s = case s of
        0 -> ("<action=xdotool key Super_L+"++ l ++">"++ m ++"</action>")
        _ -> ("<action=xdotool key Super_L+F"++ l ++">"++ m ++"</action>")

        
-- click l@(x:xs) s = ("<action=xdotool key Super_L+1>"++ l ++"</action>")
-- myWorkspacesX = clickable $ ["i","ii","iii","iv","v","vi","vii","viii","ix"] ++ ["NSP"]                            -- 4xmobar
--    where clickable l = ["<action=`xdotool key super+" ++ show (n) ++ "`>" ++ ws ++ "</action>" | (i,ws) <- zip [1..9] l, let n = i ]    -- 4xmobar
--    where clickable l = ["<action=`xdotool key super+" ++ show (n) ++ "`>" ++ ws ++ "</action>" | (i,ws) <- zip nums l, let n = i ]        -- 4xmobar


xmobarCommand (S s) = unwords ["xmobar", "-x", show s, template s]
    where template 0 = "~/.xmonad/xmobarrc0"
          template _ = "~/.xmonad/xmobarrc1"

------------------------------------------------------------------------
-- MAIN
------------------------------------------------------------------------

main = do
    nScreens <- countScreens
    hs <- mapM (spawnPipe . xmobarCommand) [0..nScreens-1]
    xmonad $ docks
           $ ewmh
           $ def { terminal           = myTerminal
                 , focusFollowsMouse  = False
                 , clickJustFocuses   = False
                 , borderWidth        = 1
                 , normalBorderColor  = "#333333"
                 , focusedBorderColor = "#00CC00"
                 , modMask            = myModMask
                 , workspaces         = myWorkspaces

                 , keys               = myKeys
                 , mouseBindings      = myMouseBindings

                 , layoutHook         = myLayout
                 , manageHook         = myManageHook
                 , handleEventHook    = myEventHook
                 , startupHook        = myStartupHook
                 , logHook            = mapM_ (dynamicLogWithPP . namedScratchpadFilterOutWorkspacePP) $ zipWith pp hs [0..nScreens-1]
                 }
