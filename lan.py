from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and receive responses
    result = srp(packet, timeout=2, verbose=0)[0]

    # Extract IP and MAC addresses from the responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Adjust this range based on your network
    devices = scan_network(ip_range)
    print(f"Number of devices connected: {len(devices)}")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")