from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"    TCP | Src Port: {tcp_layer.sport} -> Dst Port: {tcp_layer.dport}")
        
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"    UDP | Src Port: {udp_layer.sport} -> Dst Port: {udp_layer.dport}")

print("[*] Starting network sniffer...")
sniff(prn=packet_callback, store=False)

