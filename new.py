# Create a testbed for the DevNet Always On NX-OS Sandbox
from genie.libs.conf.interface import Interface
from genie.libs.conf.vlan import Vlan
from genie.testbed import load

device_details = {'devices': {'sbx-n9kv-ao': {
    'protocol': 'ssh',
    'ip': 'devnetsandbox-usw1-reservation.cisco.com',
    'port': '20203',
    'username': 'admin',
    'password': 'Cisco123',
    'os': 'nxos'}
}
}

testbed = load(device_details)

# Connect to the switch and create variable called device
device = testbed.devices['sbx-n9kv-ao']
device.connect(learn_hostname=True)


# Using genie.conf to configure vlans

# Create new Vlan object
vlan_names = ["HR", "Finance", "IT"]
vlan_numbers = [2, 3, 4]
for number, name in zip(vlan_numbers, vlan_names):
    new_vlan = Vlan(vlan_id=number, name=name)
# Add new vlan to device as a feature
    device.add_feature(new_vlan)
    new_vlan.devices


# Build and send the configuration to devices
output = new_vlan.build_config(apply=True)
print(output)

# Disconnect from the device
device.disconnect()
