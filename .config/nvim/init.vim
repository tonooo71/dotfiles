"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=$HOME/.cache/dein//repos/github.com/Shougo/dein.vim

" Required:
if dein#load_state('$HOME/.cache/dein/')
  call dein#begin('$HOME/.cache/dein/')

  let s:toml_dir = expand('$HOME/.config/nvim')

  call dein#load_toml(s:toml_dir . '/dein.toml', {'lazy': 0})
  call dein#load_toml(s:toml_dir . '/dein_lazy.toml', {'lazy': 1})

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif
"End dein Scripts-----------------------------

set number
set termguicolors
set background=light
" colorscheme solarized8_flat
" colorscheme OceanicNext
colorscheme onedark
