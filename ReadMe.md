VyOS Configuration Script

    This script will help configuring VyOS router. 

What can this script do?

    Change Interface Descriptions: It can label different parts of the router (like 'eth0', 'eth1' etc.) with names or descriptions.
    Set Up NAT: NAT stands for Network Address Translation. It lets devices on a local network use one public IP address. This script can set the rules for how this works.
    Organize DHCP: DHCP stands for Dynamic Host Configuration Protocol. It gives out IP addresses to devices on the network. This script can set up where these IP addresses start and end, how long they last, and which device acts as the gateway.
    Configure DNS Forwarding: DNS stands for Domain Name System. It turns website names into IP addresses. This script can tell the router how to handle these DNS requests.

What do I need to use it?

    1>Python
    2>Netmiko: This module lets this script talk to network devices like VyOS. We can install it using a command like pip install netmiko.
    3>A VyOS Router:A VyOS router and its IP address, username, and password.

How do I use it?

    1>Download this script to your computer.

    2>Open your command prompt or terminal. Navigate to folder where script is downloaded and we can connect to VYos by typing this command

    Example
    ##################
    PS C:\Users\CSAIT\Downloads> python .\module_publish.py -host 192.168.11.3 -username vyos -password vyos
    ##################

    Yours -host, -username, -paswword will be DIFFERENT

    Another Example(Changing Description):
    ###############
    PS C:\Users\CSAIT\Downloads> python .\module_publish.py -host 192.168.11.3 -username vyos -password vyos -interface eth4 -description "changed via script"
    ###############

    Another Example(DHCP Conf):
    ###############
    PS C:\Users\CSAIT\Downloads> python .\module_publish.py -host 192.168.11.3 -username vyos -password vyos -subnet 10.0.0.0/24 -start-ip 10.0.0.100 -end-ip 10.0.0.200 -lease-time 3600 -default-router 192.168.11.3
    ###############

    

Mandatory Options to be supplied to the Script:

    -host: The IP address of VyOS router.
    -username: The username to log into the router.
    -password: The password for the router.
    