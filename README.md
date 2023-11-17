# DB_CVP_Nov2023
Demo repo for CVP Nov 2023

Commands to run playbooks. 

## Cloning this repo

    > cd persist
    > git clone https://github.com/tonybourkesdnpros/DB_CVP_Nov2023.git
    > cd DB_CVP_Nov2023

## Change PW

Change the inventory.yml file to update the password to your local password. You'll need to do this for Arista-CVP and Arista-EOS. 

## Arista-EOS

This is using Arista and the arista.eos collection, which are for "supplemental automation". 

    > cd Arista-EOS
    > ansible-playbook add_vlan.yml

## Arista-CVP

Change directory t the Arista-CVP directory. 

    > cd Arista-CVP
    > ansible-playbook playbooks/upload_configlets.yml
    

  
