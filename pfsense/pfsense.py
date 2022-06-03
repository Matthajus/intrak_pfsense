import http.client
import json
import ssl
import pfsense_vshell
from pfsense_vshell import PFError
from tools.formatter import *


def handle_request(conn, http_method, url, headers, payload):
    conn.request(http_method, url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    obj = json.loads(data.decode("utf-8"))
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)


class Pfsense:

    def __init__(self, host, username, password, verify, port=443):
        self.host = host
        self.username = username
        self.password = password
        self.verify = verify
        self.port = port
        self.vshell = None

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

    def connect(self):
        try:
            self.vshell = pfsense_vshell.PFClient(host=self.host,
                                                  username=self.username,
                                                  password=self.password,
                                                  verify=self.verify,
                                                  port=self.port)
            print(f'Successfully connected to: {self.host}')
            return self.vshell
        except PFError as e:
            print("Error while connecting to pfsense", e)

    def get_all_static_mapping(self):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password,
            "interface": "lan"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "GET", "/api/v1/services/dhcpd/static_mapping", headers, payload)

    def delete_static_mapping(self, st_mp_id):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password,
            "id": st_mp_id,
            "interface": "lan"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "DELETE", "/api/v1/services/dhcpd/static_mapping", headers, payload)

    def create_static_mapping(self, user):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password,
            "interface": "lan",
            "mac": user.get_mac_address(),
            "ipaddr": user.get_ipv4_address(),
            "descr": f'{user.get_email()} {user.get_room_name()} {user.get_isic()}',
            "hostname": f'{user.get_name()}-{user.get_surname()}'
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "POST", "/api/v1/services/dhcpd/static_mapping", headers, payload)

    def update_static_mapping(self, user):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password,
            "id": user.get_id(),
            "interface": "lan",
            "mac": user.get_mac_address(),
            "ipaddr": user.get_ipv4_address(),
            "descr": f'{user.get_email()} {user.get_room_name()} {user.get_isic()}',
            "hostname": f'{user.get_name()}-{user.get_surname()}'
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "PUT", "/api/v1/services/dhcpd/static_mapping", headers, payload)

    def get_all_firewall_aliases(self):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "GET", "/api/v1/firewall/alias", headers, payload)

    def delete_firewall_alias(self, alias_id):
        conn = http.client.HTTPSConnection(self.host)
        payload = json.dumps({
            "client-id": self.username,
            "client-token": self.password,
            "id": alias_id
        })
        headers = {
            'Content-Type': 'application/json'
        }
        handle_request(conn, "DELETE", "/api/v1/firewall/alias", headers, payload)

    def create_firewall_alias(self, port):
        conn = http.client.HTTPSConnection(self.host)
        port_name = formate_port_name(port.get_name())
        if port.get_tcp():
            payload = json.dumps({
                "client-id": self.username,
                "client-token": self.password,
                "name": port_name + "_TCP",
                "type": "port",
                "address": split_ports(port.get_tcp()),
            })
            headers = {
                'Content-Type': 'application/json'
            }
            handle_request(conn, "POST", "/api/v1/firewall/alias", headers, payload)

        if port.get_udp():
            payload = json.dumps({
                "client-id": self.username,
                "client-token": self.password,
                "name": port_name + "_UDP",
                "type": "port",
                "address": split_ports(port.get_udp()),
            })
            headers = {
                'Content-Type': 'application/json'
            }
            handle_request(conn, "POST", "/api/v1/firewall/alias", headers, payload)

    def update_firewall_alias(self, port):
        conn = http.client.HTTPSConnection(self.host)
        port_name = formate_port_name(port.get_name())
        if port.get_tcp():
            payload = json.dumps({
                "client-id": self.username,
                "client-token": self.password,
                "id": port_name + "_TCP",
                "name": port_name + "_TCP",
                "type": "port",
                "address": split_ports(port.get_tcp()),
            })
            headers = {
                'Content-Type': 'application/json'
            }
            handle_request(conn, "POST", "/api/v1/firewall/alias", headers, payload)

        if port.get_udp():
            payload = json.dumps({
                "client-id": self.username,
                "client-token": self.password,
                "id": port_name + "_UDP",
                "name": port_name + "_UDP",
                "type": "port",
                "address": split_ports(port.get_udp()),
            })
            headers = {
                'Content-Type': 'application/json'
            }
            handle_request(conn, "POST", "/api/v1/firewall/alias", headers, payload)

