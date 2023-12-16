
# ansible-kali

Automate configuration and customization of stock Kali image with Ansible


## Installation

Clone this repository and install ansible.
```shell
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
* ```packages``` - Additional packages to install
* ```repos``` - Whole repositories that will be downloaded to ```~/repos```.
* ```releases``` - Repository releases to choose from that will be downloaded to ```~/executables```.
* ```path_dirs``` - Directories to add to the PATH environment variable.

## Features

### System

- Make cuurent user autologin on start
- Shorten Grub menu waiting time to 1 second
- Configure Clipman to autostart, popup at pointer and Super+v keyboard shortcut
- Install Alacritty and configure as default terminal
- Copy files from ```./roles/user/files/home``` to user home (apply configurations)
- Add folders to PATH env


### Tools
- Download github repos to ```~/repos``` and releases to ```~/executables```
- Fix remote path completion of evil-winrm
