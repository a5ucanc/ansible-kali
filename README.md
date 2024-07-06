
# ansible-kali

Automate configuration and customization of stock Kali image with Ansible


## Installation

Clone this repository and install ansible.
```shell
git clone https://github.com/a5ucanc/ansible-kali
sudo apt update
sudo apt install ansible 
```


## Usage

The changes will affect the current user.

Run the command and supply the root password
```shell
cd ansible-kali
ansible-playbook -i inventory.yml -K main.yml
```

## Configuration

Edit the ```inventory.yml``` to configure the process. 

* ```hosts``` - Remote and local hosts.
* ```burpsuite``` - Include burpsuite pro download.
* ```burpsuite_folder``` - Burpsuite pro download directory (default: /opt/burpsuite).
* ```apt_packages``` - Additional system packages to install.
* ```pip_packages``` - Pip packages to install for the user.
* ```repos_dir``` - Location for github repos (default: ~/tools).
* ```repos``` - Repositories to download.
* ```path_dirs``` - Directories to add to the PATH environment variable.

## Features

- Make curent user autologin on start
- Shorten Grub menu waiting time to 1 second
- Configure Clipman to autostart, popup at pointer and Super+v keyboard shortcut
- Install Alacritty and configure as default terminal
- Install [ohmytmux](https://github.com/gpakosz/.tmux) and [vimrc](https://github.com/amix/vimrc) configurations
- Install user specified packages and apply defalult configurations to some tools
- Download Burpsuite pro and supplementary libraries (jython, jruby and ysoserial)
- Add folders to PATH env