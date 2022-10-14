# Make aliases
---
## Make copy aliases
---
Get xsel
```bash
sudo apt install xsel
```

From the home directory open the `.zshrc` file

```bash
code .zshrc 
```

add alias
```bash
# make copy aliases
alias copy=' tee /dev/tty|xsel -ib'
```
