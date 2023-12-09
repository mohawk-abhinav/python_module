import argparse
from netmiko import ConnectHandler

# this function will help establish an SSH connection to the VyOS device
def connect_to_vyos(host, username, password, port=22):
    vyos_router = {
        "device_type": "vyos",
        "host": host,
        "username": username,
        "password": password,
        "port": port,
    }
    return ConnectHandler(**vyos_router)

# this function will configure the description of an interface
def configure_interface_description(net_connect, interface, description):
    command_to_send = [
        f'set interfaces ethernet {interface} description "{description}"'
        ]
    return net_connect.send_config_set(command_to_send)

# this function will configure NAT
def configure_nat(net_connect, outbound_interface, source_address):
    command_to_send = [
        f'set nat source rule 100 outbound-interface "{outbound_interface}"',
        f'set nat source rule 100 source address "{source_address}"',
        'set nat source rule 100 translation address masquerade'
    ]
    return net_connect.send_config_set(command_to_send)

# this function will configure DHCP 
def configure_dhcp(net_connect, subnet, start_ip, end_ip, lease_time, default_router):
    command_to_send = [
        f'set service dhcp-server shared-network-name LAN subnet {subnet} range 0 start "{start_ip}"',
        f'set service dhcp-server shared-network-name LAN subnet {subnet} range 0 stop "{end_ip}"',
        f'set service dhcp-server shared-network-name LAN subnet {subnet} lease "{lease_time}"',
        f'set service dhcp-server shared-network-name LAN subnet {subnet} default-router "{default_router}"'
    ]
    return net_connect.send_config_set(command_to_send)

# this function will configure DNS 
def configure_dns(net_connect, listen_address, allow_from):
    command_to_send = [
        'set service dns forwarding cache-size "0"',
        f'set service dns forwarding listen-address "{listen_address}"',
        f'set service dns forwarding allow-from "{allow_from}"'
    ]
    return net_connect.send_config_set(command_to_send)

# defining parser 
parser = argparse.ArgumentParser(
    description="Configure VyOS Device",
    prefix_chars="-"
    )

# parser arguments for configuration 
parser.add_argument(
    "-host",
    required=True,
    help="IP address of the VyOS device"
    )


parser.add_argument(
    "-username",
    required=True,
    help="Username for the VyOS device"
    )

parser.add_argument(
    "-password",
    required=True,
    help="Password for the VyOS device"
    )

# arguments for specific configurations

parser.add_argument(
    "-interface",
    help="Interface to configure"
    )


parser.add_argument(
    "-description",
    help="Description for the interface"
    )

parser.add_argument(
    "-outbound-interface",
    help="Outbound interface for NAT"
    )

parser.add_argument(
    "-source-address",
    help="Source address for NAT"
    )

parser.add_argument(
    "-subnet",
    help="Subnet for DHCP"
    )

parser.add_argument(
    "-start-ip",
    help="Start IP for DHCP range"
    )

parser.add_argument(
    "-end-ip",
    help="End IP for DHCP range"
    )

parser.add_argument(
    "-lease-time",
    help="Lease time for DHCP"
    )

parser.add_argument(
    "-default-router",
    help="Default router for DHCP"
    )
parser.add_argument(
    "-dns-listen-address",
    help="DNS listen address"
)

parser.add_argument(
    "-dns-allow-from",
    help="Allowed sources for DNS"
)

args = parser.parse_args()

# Connecting to VyOS device using the provided arguments
net_connect = connect_to_vyos(args.host, args.username, args.password)

# Apply configurations based on provided arguments
if args.interface and args.description:
    print(configure_interface_description(net_connect, args.interface, args.description))

if args.outbound_interface and args.source_address:
    print(configure_nat(net_connect, args.outbound_interface, args.source_address))

if args.subnet and args.start_ip and args.end_ip and args.lease_time and args.default_router:
    print(configure_dhcp(net_connect, args.subnet, args.start_ip, args.end_ip, args.lease_time, args.default_router))

if args.dns_listen_address and args.dns_allow_from:
    print(configure_dns(net_connect, args.dns_listen_address, args.dns_allow_from))

# Commiting the configuration changes on the device
print(net_connect.commit())
