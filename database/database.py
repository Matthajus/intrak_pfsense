import mysql.connector
from mysql.connector import Error

from database.models.entities.Port import Port
from database.models.entities.User import User


def parse_users(request):
    result = list()
    for row in request:
        result.append(User(row[0], row[1], row[2], row[5], row[6], row[17], row[11]))

    return result


def parse_ports(request):
    result = list()
    for row in request:
        result.append(Port(row[0], row[2], row[3], row[4]))

    return result


class Database:

    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      database=self.database,
                                                      user=self.user,
                                                      password=self.password,
                                                      port=self.port)
            print(f'Successfully connected to: {self.host} database!')
            self.cursor = self.connection.cursor()
            return self.connection, self.cursor
        except Error as e:
            print("Error while connecting to database", e)

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print(f'Database connection: {self.host} is closed!')

    def get_all_users(self):
        query = "select * from users"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        users = parse_users(records)
        for user in users:
            query = f'select pc.mac_pc, pc.IPv4_pc from pc as pc ' \
                    f'join users as u on pc.users_id_user=u.id_user ' \
                    f'where u.id_user={user.get_id()}'
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            user.set_mac_address(records[0][0])
            user.set_ipv4_address(records[0][1])

            query1 = f'select description from shorewall_tcp ' \
                     f'where id_user = {user.get_id()}'
            self.cursor.execute(query1)
            records1 = self.cursor.fetchall()
            if records1:
                user.set_games(records1[0])

        return users

    def get_all_ports(self):
        query = "select * from ports"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return parse_ports(records)
