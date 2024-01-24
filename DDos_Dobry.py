import socket

def send_large_packets(target_ip, target_port, num_packets, packet_size):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
        message = "A" * packet_size  
        data = message.encode('utf-8')

        
        for _ in range(num_packets):
            s.sendto(data, (target_ip, target_port))

        print(f"Wysłano {num_packets} pakietów o rozmiarze {packet_size} bajtów na {target_ip}:{target_port}")

    except socket.error as e:
        print(f"Błąd podczas wysyłania pakietów: {e}")

    finally:
        
        s.close()

if __name__ == "__main__":
    
    target_ip = input("IP routera: ")
    target_port = int(input("Port: "))
    num_packets = int(input("Liczba Pakietów: "))
    packet_size = int(input("Rozmiar pakietu (Bajty): "))

    
    send_large_packets(target_ip, target_port, num_packets, packet_size)
