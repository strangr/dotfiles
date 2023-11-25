# ZSH @TODO

# 1. review omz pugings at https://github.com/janeczku/oh-my-zsh/tree/master/plugins

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
export BROWSER=firefox





#Export the variable using your shell of use:

#.bash_profile
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
# ~/.config/fish/config.fish
#set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket




# Keychain @TODO temp disabled
# eval $(keychain --eval --quiet ~/.ssh/id_ed25519)


###########
# Aliases #
###########
# @TODO move this part to aliases and source /path/to/my/aliases
alias please='sudo $(fc -ln -1)'

alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias ls='ls --color=auto'

alias calc='bc -l'

alias stt='subl .'

alias pacrem='pacman -Rns'
alias yarem='yay -Rns'
alias parem='pacaur -Rns'

###############
# keybindings # @TODO move to a different file
###############

# @TODO revive fzf
# [ -f /usr/share/fzf/key-bindings.zsh ] && source /usr/share/fzf/key-bindings.zsh
# [ -f /usr/share/fzf/completion.zsh ] && source /usr/share/fzf/completion.zsh

# basic key navigations
bindkey "\e[7~" 	beginning-of-line	# home
bindkey "\e[8~" 	end-of-line			# end
bindkey "^[[3~" 	delete-char			# delete
bindkey '^[[1;5D'   backward-word       # ctrl+left
bindkey '^[[1;5C'   forward-word        # ctrl+right
bindkey '^H' 		backward-kill-word 	# ctrl+backsapce
bindkey '^[[3^' 	kill-word			#ctrl+delete



# +--------+
# | PROMPT |
# +--------+

fpath=($ZDOTDIR/prompt $fpath)
autoload -Uz simple_prompt_setup; simple_prompt_setup


# Dir Stack
setopt AUTO_PUSHD           # Push the current directory visited on the stack.
#setopt PUSHD_IGNORE_DUPS    # Do not store duplicates in the stack.
setopt PUSHD_SILENT         # Do not print the directory stack after pushd or popd.

alias d='dirs -v'
for index ({1..9}) alias "$index"="cd +${index}"; unset index

###########################
# End Personal Configurations #
###########################

# The following lines were added by compinstall
# @TODO move this part to completion and source /path/to/my/completion

zstyle ':completion:*' completer _complete _ignored _approximate
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|[._-]=** r:|=**' 'm:{[:lower:]}={[:upper:]}' ''
zstyle ':completion:*' max-errors 2 numeric
zstyle ':completion:*' menu select=3
zstyle ':completion:*' original true
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true
zstyle :compinstall filename '/home/st/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Lines configured by zsh-newuser-install
HISTFILE=$HOME/Logs/zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt autocd notify
bindkey -e
# End of lines configured by zsh-newuser-install

# plugin to quick navigate history
source ~/.config/zsh/plugins/dirhistory.plugin.zsh

bindkey "^[[1;6D" dirhistory_zle_dirhistory_back
bindkey "^[[1;6C" dirhistory_zle_dirhistory_future
bindkey "^[[1;6A" dirhistory_zle_dirhistory_up

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh

# zsh-history-substring-search binding
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
