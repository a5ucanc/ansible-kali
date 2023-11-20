
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

### System

- Make defaul user autologin on start
- Shorten Grub menu waiting time to 1 second
- Configure Clipman to autostart, popup at pointer and Super+v keyboard shortcut
- Install Alacritty and configure as default terminal


### Tools

- Overwrite tmux and vim configurations
- Fix remote path completion of evil-winrm

# Todo
- [ ] Create new user if needed
- [ ] Reboot the system after finishing
- [ ] Update and upgrade the system
