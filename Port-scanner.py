import socket

def scan_port(target, port, timeout=1):
    """Try to connect to a port. Returns True if open, False if closed."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def port_scanner():
    print("=== Python Port Scanner ===")

    target = input("Enter target IP or domain (example: scanme.nmap.org): ").strip()

    start_port = int(input("Enter start port (example: 20): ").strip())
    end_port = int(input("Enter end port (example: 1024): ").strip())

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

    print("\n=== Scan Complete ===")
    if open_ports:
        print("Open ports found:", open_ports)
    else:
        print("No open ports found in that range.")

if __name__ == "__main__":
    port_scanner()
