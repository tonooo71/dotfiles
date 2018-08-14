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

set termguicolors
set background=light

set number          " 行番号を表示
set expandtab       " TabをSpaceで変換する
set tabstop=4       " ファイル上のTab文字の幅
set shiftwidth=4    " 自動で挿入されるインデントの幅
set softtabstop=4   " Tabを押したときに挿入されるSpace

set hlsearch        " 検索語句のハイライト
set ignorecase      " 検索時の英大小文字の区別を無視
set smartcase       " 英小文字の場合のみ検索時の区別を無視

set cindent         " C言語スタイルのインデントを自動挿入
set showcmd         " 入力中のコマンドを表示

set list            " 空白文字の可視化(Tabと文末のSpace)
set listchars=tab:>-,trail:.
set ambiwidth=double    " 全角文字の幅を2に固定
syntax on           " シンタックスハイライト

filetype plugin indent on  " よくわからん

set encoding=utf-8  " デフォルトエンコーディング
set nobackup        " バックアップファイルを作らない

colorscheme onedark

tnoremap <silent> <ESC> <C-\><C-n>
