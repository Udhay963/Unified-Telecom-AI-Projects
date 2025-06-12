from datetime import datetime, timedelta

class DHCPServer:
    def __init__(self, ip_pool, lease_time=60):
        self.ip_pool = ip_pool
        self.lease_time = lease_time  # seconds
        self.leases = {}  # client_id -> {ip, expiry}

    def assign_ip(self, client_id):
        now = datetime.now()

        # Check existing lease
        if client_id in self.leases:
            lease = self.leases[client_id]
            if lease["expiry"] > now:
                return lease["ip"], "Lease Active"
            else:
                # Lease expired, release IP
                self._release_ip(lease["ip"])

        # Assign new IP
        available_ips = set(self.ip_pool) - {lease["ip"] for lease in self.leases.values()}
        if not available_ips:
            return None, "No IP Available"

        assigned_ip = sorted(available_ips)[0]
        expiry = now + timedelta(seconds=self.lease_time)
        self.leases[client_id] = {"ip": assigned_ip, "expiry": expiry}
        return assigned_ip, "New Lease Assigned"

    def _release_ip(self, ip):
        for cid, lease in list(self.leases.items()):
            if lease["ip"] == ip:
                del self.leases[cid]
                break


class ClientDevice:
    def __init__(self, device_id):
        self.device_id = device_id
