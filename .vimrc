color delek
syntax on

"  Set colors
hi Comment ctermfg=Green      "  html comments
hi Constant ctermfg=DarkGreen "  rst code block coding
hi Identifier ctermfg=Blue    "  rst links
hi Normal ctermfg=Gray        "  normal text
hi Statement ctermfg=Blue     "  rst .. code-block tag
hi Type ctermfg=DarkCyan       "  rst section headings
hi Title ctermfg=DarkRed      "  html section headings

"  Set formatting    
highlight SpecialKey ctermfg=Yellow ctermbg=LightRed  Colors special keys yellow
set list
set listchars=tab:T>                "  Shows all space after tabs as > chars
match ErrorMsg '\s\+$'  "  Highlighted in RED end of line whitespace
set tw=80
