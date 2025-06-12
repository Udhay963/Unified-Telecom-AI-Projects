from dhcp_server import DHCPServer
from client_device import ClientDevice
from utils import generate_ipv4_pool, generate_ipv6_pool
import time

# Toggle between 'ipv4' and 'ipv6'
MODE = 'ipv4'

if MODE == 'ipv4':
    ip_pool = generate_ipv4_pool("192.168.0.100", 20)
else:
    ip_pool = generate_ipv6_pool("2001:db8:abcd", 20)

server = DHCPServer(ip_pool, lease_time=30)

clients = [ClientDevice(f"Device_{i}") for i in range(1, 11)]

for client in clients:
    client.request_ip(server)
    time.sleep(1)

print("\nCurrent Lease Table:")
server.show_leases()
