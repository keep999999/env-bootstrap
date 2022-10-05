#!/bin/bash

sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
# ln -s /usr/bin/python3 /usr/bin/python

alias_ll="alias ll='ls -al'"
# alias_pip="alias pip='python -m pip'"

add_alias_ll="echo \"${alias_ll}\" >> ~/.bash_aliases"
# add_alias_pip="echo \"${alias_pip}\" >> ~/.bash_aliases"

cat ~/.bash_aliases
echo "-----------------------------------------------------------------------------------"
[[ -z $(grep "${alias_ll}" ~/.bash_aliases) ]] && eval "${add_alias_ll}" || :
# [[ -z $(grep "${alias_pip}" ~/.bash_aliases) ]] && eval "${add_alias_pip}" || :

cat ~/.bash_aliases
source ~/.bashrc