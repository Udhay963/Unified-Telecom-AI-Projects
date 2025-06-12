from ipaddress import IPv4Address, IPv6Address

def generate_ipv4_pool(start_ip: str, count: int):
    start = int(IPv4Address(start_ip))
    return [str(IPv4Address(start + i)) for i in range(count)]

def generate_ipv6_pool(start_ip: str, count: int):
    start = int(IPv6Address(start_ip + "::1"))  # minimal suffix for valid IPv6
    return [str(IPv6Address(start + i)) for i in range(count)]
