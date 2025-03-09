import socket
import threading

# Globaali muuttuja ensimmäiselle arvolle ja lukko thread-turvallisuuteen
_first_value = None
_value_lock = threading.Lock()

def fetch_number(IP, p):
    #Write your code here!
    # Luo UDP-soketti
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    global _first_value
    try:
        # Lähetä pyyntö palvelimelle
        message = "Anna luku!"
        udp_socket.sendto(message.encode(), (IP, p))
        
        # Vastaanota vastaus palvelimelta
        data, _ = udp_socket.recvfrom(1024)
        value = int(data.decode().strip())
        
        # Tarkista ja aseta ensimmäinen arvo, jos ei vielä asetettu
        with _value_lock:
            if _first_value is None:
                _first_value = value
            return _first_value
    
    except Exception as e:
        print(f"Error fetching number: {e}")
        raise
    finally:
        udp_socket.close()
    pass


if __name__=='__main__':
    pass
    #Write test code here
    # Testikoodi paikallista testausta varten
    for _ in range(5):
        result = fetch_number("127.0.0.1", 7938)
        print(f"Received: {result}")

