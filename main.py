from database.database import Database
from pfsense.pfsense import Pfsense
from database.models.entities.User import User
from database.models.entities.Port import Port
from tools.formatter import *

if __name__ == '__main__':
    user = User(2, 'Generated', 'user', '0000000000000000', 'api_user@upjs.sk', '40A', 2)
    user.set_ipv4_address('10.0.0.199')
    user.set_mac_address('01:23:45:67:89:ab')
    user.set_games('League of Legends, Steam, Dota 2, left4dead 2,Borderlands2, CS:GO, Valorant, Bloodhunt (Vampire: '
                   'The Masquerade)')

    port1 = Port(5, 'Anno 2070', '13000,13005,13200:13999', '')
    port2 = Port(5, 'Armoured Warfare', '5050,5055', '61090:61154')

    db = Database('admin.intrak.upjs.sk', 'pfsense', 'KwKde04ZYxwBP5hUjeSB', 'pfsense_test')
    db_connection, cursor = db.connect()

    users = db.get_all_users()
    for user in users:
        print(user)
        print('User name type: ', type(user.get_name()))
        print('User surname type: ', type(user.get_surname()))
        print('User games type: ', type(user.get_games()), ' value: ', tuple_to_string(user.get_games()))

    print()

    ports = db.get_all_ports()
    for port in ports:
        print(port)

    db.disconnect()

    print("\n")
    print("Pfsense connection")
    pf = Pfsense('test-pfsense.sd.upjs.sk', 'admin', 'KwKde04ZYxwBP5hUjeSB', False)
    pf_vshell = pf.connect()

    # print("\n")
    # print("****************")
    # print("\n")
    #
    # pf.get_all_static_mapping()
    # pf.delete_static_mapping(2)
    #
    # print("\n")
    # print("****************")
    # print("\n")
    #
    # pf.create_static_mapping(user)
    #
    # print("\n")
    # print("****************")
    # print("\n")
    #
    # user.set_surname('user-updated')

    # pf.get_all_firewall_aliases()
    # pf.delete_firewall_alias("Albion_online_UDP")
    # pf.create_firewall_alias(port1)
    # pf.get_all_firewall_aliases()
    #
    # port1.set_udp([1, 2])
    # pf.update_firewall_alias(port1)
    # pf.get_all_firewall_aliases()
