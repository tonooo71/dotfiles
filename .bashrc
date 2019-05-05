#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export PATH=/home/maruoka/.nimble/bin:$PATH

# ranger
export EDITOR=nvim

# neovim
export XDG_CONFIG_HOME=~/.config
export XDG_CACHE_HOME=~/.cache

exec fish

