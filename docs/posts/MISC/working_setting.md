### Terminal
Windows: Windows Terminal Preview
Mac: ITerm2

### Shell 
Windows: WSL + Oh-My-Bash
Mac: Oh-My-Zsh
Oh-My-Tmux

### Editor
VSCode + Vim keymap

### Personal Notes
mkdocs-material: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/

```bash
pip install mkdocs
pip install mkdocs-material
pip install pymdown-extensions

mkdocs serve &
```

### Version Control & Code Storage
lazygit: https://github.com/jesseduffield/lazygit

```bash title="github ssh"
echo "IdentityFile path/to/sshkey" >> ~/.ssh/config # add key
ssh -T git@github.com # test ssh connection
```