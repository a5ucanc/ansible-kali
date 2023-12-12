
# ansible-kali

Bootup Kali with Ansible


## Installation

```shell
# Make sure system cache is up to date
sudo apt update -y

# Install Ansible
sudo apt install ansible

# Clone this repo
git clone https://github.com/a5ucanc/ansible-kali
```


## Usage

Simply run the command and supply the root password
```shell
cd ansible-kali
ansible-playbook -K main.yml
```


## Features

### System

- Make current user autologin on start
- Shorten Grub menu waiting time to 1 second
- Configure Clipman to autostart, popup at pointer and Super+v keyboard shortcut
- Install Alacritty and configure as default terminal


### Tools

- Overwrite tmux and vim configurations
- Fix remote path completion of evil-winrm
