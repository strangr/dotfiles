# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.config/zsh/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

###########################
# Personal Configurations #
###########################

# Add bin directory in home
typeset -U path
path=("$HOME/bin" $path)
path=("$HOME/Android/Sdk/platform-tools" $path)
export PATH

# Default Variables
export VISUAL=subl
export EDITOR=nano
export BROWSER=google-chrome-stable

eval $(keychain --eval --quiet ~/.ssh/id_ed25519)


HISTFILE=$ZDOTDIR/.zsh_history

# FROM HERE STARTS OH MY ZSH PART

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
ZSH=/usr/share/oh-my-zsh/

ZSH_THEME="powerlevel10k/powerlevel10k"
POWERLEVEL9K_MODE="nerdfont-complete"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
DISABLE_AUTO_UPDATE="true"

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
ZSH_CUSTOM=$ZDOTDIR/custom

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
	vi-mode
	dirhistory
	fzf
	git # maybe replace with gitfast? faster but less descriptive
	sudo # press escape twice to repeat command with sudo
	#sublime #
	#wd -- bookmark (warp) dirs and jump, disabled for now as I dont need it
	alias-finder # testing for now
	zsh-autosuggestions # fish like suggestions
	history-substring-search # fish like history search (experiment if I need it)
)

# User configuration

#VI_MODE_RESET_PROMPT_ON_MODE_CHANGE=true
#MODE_INDICATOR="%F{yellow}+%f"

ZSH_AUTOSUGGEST_STRATEGY=(history completion) # @TODO! completion makes it little slower, experiment for now

ZSH_ALIAS_FINDER_AUTOMATIC=true

#DISABLE_FZF_AUTO_COMPLETION="true"
export FZF_BASE=/usr/bin/fzf
# @TODO FZF shortcuts not working, **, CTRL+C, CTRL+R ..
#export FZF_DEFAULT_COMMAND='fd --type f'
export FZF_DEFAULT_COMMAND="fd --hidden --follow --exclude '.git'"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="$FZF_DEFAULT_COMMAND --type d"
# for more info see fzf/shell/completion.zsh
#_fzf_compgen_path() {
#    fd . "$1"
#}
#_fzf_compgen_dir() {
#    fd --type d . "$1"
#}
export FZF_COMPLETION_TRIGGER='!!'
export FZF_DEFAULT_OPTS='
--exact
--height 60%
--layout=reverse
--border=sharp
--cycle
--info=inline
--multi
--preview-window=:hidden
--preview-window=:sharp
--preview-window=:right
--preview "([[ -f {} ]] && (bat --style=numbers --color=always {} || cat {})) || ([[ -d {} ]] && (tree -C {} | less)) || echo {} 2> /dev/null | head -200"
--color="hl:148,hl+:154,pointer:032,marker:010,bg+:237,gutter:008"
--prompt="~ "
--pointer="▶"
--marker="✗"
--bind "?:toggle-preview"
--bind "ctrl-a:select-all"
--bind "ctrl-e:execute(echo {+} | xargs -o vim)"
--bind "ctrl-v:execute(code {+})"'

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

ZSH_CACHE_DIR=$HOME/.cache/oh-my-zsh
if [[ ! -d $ZSH_CACHE_DIR ]]; then
  mkdir $ZSH_CACHE_DIR
fi

source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/.p10k.zsh.
[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh

# Syntax Highlighter must be last to be sourced
source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=magenta,bold'
ZSH_HIGHLIGHT_STYLES[path]='fg=magenta,bold'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=magenta,bold'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=magenta,bold'

###########
# Aliases #
###########

alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias ls='ls --color=auto'

alias pacrem='pacman -Rns'
alias yarem='yay -Rns'

###############
# keybindings # @TODO move to a different file
###############

# EXPERIMENTAL! (read moar)
bindkey -v

[ -f /usr/share/fzf/key-bindings.zsh ] && source /usr/share/fzf/key-bindings.zsh
[ -f /usr/share/fzf/completion.zsh ] && source /usr/share/fzf/completion.zsh

bindkey "^[h" dirhistory_zle_dirhistory_back
bindkey "^[l" dirhistory_zle_dirhistory_future
bindkey "^[k" dirhistory_zle_dirhistory_up
bindkey "^[j" dirhistory_zle_dirhistory_down