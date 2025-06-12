class ClientDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.assigned_ip = None

    def request_ip(self, dhcp_server):
        ip, status = dhcp_server.assign_ip(self.device_id)
        self.assigned_ip = ip
        print(f"Device {self.device_id} assigned IP: {ip} ({status})")
