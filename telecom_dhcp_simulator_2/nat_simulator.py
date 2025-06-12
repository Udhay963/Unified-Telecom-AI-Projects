import random

class NATSimulator:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.mapping = {}  # private_ip:private_port -> public_port
        self.used_ports = set()

    def translate(self, private_ip, private_port):
        key = (private_ip, private_port)
        if key in self.mapping:
            return self.public_ip, self.mapping[key]

        # Find an unused public port
        public_port = random.randint(3000, 9000)
        while public_port in self.used_ports:
            public_port = random.randint(3000, 9000)

        self.mapping[key] = public_port
        self.used_ports.add(public_port)
        return self.public_ip, public_port
