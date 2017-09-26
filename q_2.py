import re


def check_address(address):
    for s in address:
        s = s.strip()
        if s.find(',') == -1:
            s = s + ','
        print(check_regex(s)+" : "+s.replace(",", "") )


def check_regex(ip):
    if re.match('(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}'
                '([[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]),', ip):
        return "True "
    else:
        return "False"


if __name__ == '__main__':
    with open('address.txt', 'r') as file:
        addresses = file.readlines()

    check_address(addresses)

    exit(0)
