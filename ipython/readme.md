# Ipython configs

 - I use ipython as the repl for vim-slime when working in neovim
 - autoindent can mess up the repl input by accumulating tabs when passing in indented blocks
 - either toggle `%autoindent` in the ipython repl or set defaults in `~/.ipython/profile_default/ipython_config.py`
 - if the above doesn't exist, init it with `ipython profile create default` first 
 - Then place `c.TerminalInteractiveShell.autoindent = False` in it.
