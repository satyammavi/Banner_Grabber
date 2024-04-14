import socket

def grab_banner(ip_address, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        #banner = s.recv(1024)
        banner = (str(s.recv(1024)).strip('b'))
        s.close()
        return banner
    except Exception as e:
        print(f"Error: {e}")
        return ''

def main():
    port = int(input("Enter your port no.: "))
    ip = input("Enter IP: ")
    print(grab_banner(ip, port))

if __name__ == '__main__':
  main()
