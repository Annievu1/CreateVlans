# Automate Vlan Creation

## PyATS & Genie
PyATS is the core platform frame work and Genie is the SDK specializing in network device automation & validation.
https://developer.cisco.com/docs/pyats/#!introduction/cisco-pyats-network-test--automation-solution

## Installation 
1. Create a virtual environment 
2. Use pip to install PyATS (https://pypi.org/project/pyats/) and Genie SDK (https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/genie.html)
3. Run the command 'pip install -r requirements.txt' to install all dependencies 

## Use Case 
This allows you to connect to a switch via SSH and automate the creation of vlans by looping through a defined list of desired vlan number(s) and vlan name(s). 
