
# ansible-kali

Bootup Kali with Ansible


## Installation

```shell
# Make sure system is up to date
sudo apt update -y; sudo apt upgrade -y

# Install Ansible
pip install ansible 
```
    
## Usage

Simply run the command and supply the root password
```shell
cd ansible-kali
ansible-playbook -K main.yml
```

## Features

- Install Alacritty and configure as default terminal
- Shorten Grub menu waiting time to 1 second
- Make defaul user autologin on start
- Overwrite tmux and vim configurations
- Configure Clipman to autostart, popup at pointer and Super+v keyboard shortcut