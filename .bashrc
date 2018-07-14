#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#export GUROBI_HOME="/opt/gurobi800/linux64"
#export PATH="${PATH}:${GUROBI_HOME}/bin"
#export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"

#export PATH="${PATH}":/opt/hmetis-2.0pre1/Linux-x86_64/
#export PATH="${PATH}":/opt/alanmi-abc-c3ebee81b8d8/

# ranger
export EDITOR=nvim

# neovim
export XDG_CONFIG_HOME=~/.config
export XDG_CACHE_HOME=~/.cache

exec fish

