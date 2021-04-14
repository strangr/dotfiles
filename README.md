# strangr

Top secret text files that make my world a better place. :')

## dotfiles

super confidential dotfiles

Fish To Zsh

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

powerlevel10k
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k


     ______    ________  ______   _______    ______  
   _/      \_ /        |/      \ /       \  /      \ 
  / $$$$$$   \$$$$$$$$//$$$$$$  |$$$$$$$  |/$$$$$$  |
 /$$$ ___$$$  \  $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |
/$$/ /     $$  | $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |/$$$$$ |$$ | $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |$$  $$ |$$ | $$ |  $$ \__$$ |$$ |__$$ |$$ \__$$ |
$$ |$$  $$  $$/  $$ |  $$    $$/ $$    $$/ $$    $$/ 
$$  \$$$$$$$$/   $$/    $$$$$$/  $$$$$$$/   $$$$$$/  
 $$   \__/   |                                       
  $$$    $$$/                                        
    $$$$$$/                                          


1 . move .android inside config or something
The emulator searches the avd directory in the order of the values
in $ANDROID_AVD_HOME, $ANDROID_SDK_HOME/.android/avd/, and $HOME/.android/avd/.
https://developer.android.com/studio/command-line/variables

2. move my cal schedule inside some formatted file
and make cron job to send notification with each update? what about andr?

4. https://github.com/jeffreytse/zsh-vi-mode <- vi-mode pluginis nacvlad

5. moved from screenfetch to neofetch. add few configs
https://github.com/dylanaraps/neofetch/wiki/Customizing-Info
	1. gtk font (screefetch used to dispaly "Noto Font 11")
	2. disk size
	3. make default image

6. Reaearch AdGuard

https://github.com/AdguardTeam/AdGuardHome
https://github.com/AdguardTeam/AdGuardDNS
https://adguard.com/en/adguard-dns/overview.html#instruction
https://www.reddit.com/r/Adguard/comments/ac8v8l/adguard_or_adguard_dns_or_adguard_home/
https://home-assistant-guide.com/2020/09/26/adguard-home-vs-pi-hole-2020-two-ad-and-internet-tracker-blockers-compared/#:~:text=Pi%2Dhole%20and%20AdGuard%20Home,Windows%2C%20macOS%2C%20and%20FreeBSD.


7. https://searx.github.io/searx/

8. write out all my keybindings (that Im using) inside README

9. pron for insp
https://www.reddit.com/r/unixporn/comments/glbl4v/oc_its_not_normal_to_want_my_firefox_to_sit_on_my/
https://www.reddit.com/r/unixporn/comments/fvyix5/oc_blurry_discord_is_for_everyone_now/
https://www.reddit.com/r/unixporn/comments/dlxtlg/gnome_dynamic_wallpaper/
https://i.redd.it/y6ggh8x53yb61.png

10. Try Qtile after Xmonad




11. To Install Xmonad, xinitrc must contain
# Xmonad Variables
export XMONAD_CONFIG_DIR=$HOME/.config/xmonad/
export XMONAD_DATA_DIR=$HOME/.config/xmonad/
export XMONAD_CACHE_DIR=$HOME/.config/xmonad/