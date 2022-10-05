- [x] markdown enhanced preview extension
- [x] python extension
- [x] install pip: `apt update && apt install -y python3-pip`
- [x] ~~symlink python3 to python: `ln -s /usr/bin/python3 /usr/bin/python`~~
- ~~[ ] add alias for pip~~ 
```
cat >> ~/.bashrc <<-eot
    alias pip="python -m pip"
eot
source ~/.bashrc
```
- [ ] telegram bot by example
    - [x] find gh repo: https://github.com/python-telegram-bot/python-telegram-bot
    - [x] install requirements
    - [ ] register with Bot Father
    - [ ] add custom action
    - [ ] run and check with tg client