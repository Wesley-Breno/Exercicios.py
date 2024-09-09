import socket


def scan(targets, ports):
    for port in range(1, ports):
        scan_port(targets, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port opened: " + str(port))
        sock.close()
    except:
        ...


if __name__ == "__main__":
    targets_input = input("[*] Enter targets to scan (split them by ,): ")
    port_input = int(input("[*] Enter how many ports you want to scan: "))

    if ',' in targets_input:
        print("[*] Scanning multiple targets")
        for ip_addr in targets_input.split(','):
            print()
            print(ip_addr.strip(" "))
            scan(ip_addr.strip(" "), port_input)

    else:
        print("[*] Scanning target")
        print()
        print(targets_input)
        scan(targets_input, port_input)