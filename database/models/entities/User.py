class User:

    def __init__(self, user_id, name, surname, isic, email, room_name, state):
        self.id = user_id
        self.name = name
        self.surname = surname
        self.isic = isic
        self.email = email
        self.room_name = room_name
        self.state = state
        self.mac_address = None
        self.ipv4_address = None
        self.games = None

    def __str__(self):
        return f'{self.id}, {self.name} {self.surname}, isic: {self.isic}, email: {self.email}, state: {self.state}, ' \
               f'room: {self.room_name}, MAC: {self.mac_address}, IPv4: {self.ipv4_address}, Games: {self.games} '

    def get_id(self):
        return self.id

    def set_id(self, user_id):
        self.id = user_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_isic(self):
        return self.isic

    def set_isic(self, isic):
        self.isic = isic

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_room_name(self):
        return self.room_name

    def set_room_name(self, room_name):
        self.room_name = room_name

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_mac_address(self):
        return self.mac_address

    def set_mac_address(self, mac_address):
        self.mac_address = mac_address

    def get_ipv4_address(self):
        return self.ipv4_address

    def set_ipv4_address(self, ipv4_address):
        self.ipv4_address = ipv4_address

    def get_games(self):
        return self.games

    def set_games(self, games):
        self.games = games
