class Port:

    def __init__(self, port_id, name, tcp, udp):
        self.id = port_id
        self.name = name
        self.tcp = tcp
        self.udp = udp

    def __str__(self):
        return f'{self.id}, {self.name}, TCP: ({self.tcp}), UDP: ({self.udp})'

    def get_id(self):
        return self.id

    def set_id(self, port_id):
        self.id = port_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_tcp(self):
        return self.tcp

    def set_tcp(self, tcp):
        self.tcp = tcp

    def get_udp(self):
        return self.udp

    def set_udp(self, udp):
        self.udp = udp
