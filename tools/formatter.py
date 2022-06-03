CHAR_TO_REPLACE = {' ': '_',
                   '-': '_',
                   '/': '_',
                   ':': '_',
                   '+': '_',
                   '(': '_',
                   ')': '_',
                   '.': '_'}


def formate_port_name(name):
    name = name.translate(str.maketrans(CHAR_TO_REPLACE))
    return name


def split_ports(ports):
    ports = ports.replace(' ', '').replace('\n', '')
    return ports.split(",")


def tuple_to_string(t):
    s = str(t).replace('(', '').replace(')', '').replace('\'', '')[:-1]
    return s
