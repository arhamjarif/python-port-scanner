import socket

host = input("Enter IP: ")
start_port = int(input("Enter first port: "))
end_port = int(input("Enter last port: "))
open_ports = []
closed_ports = []

for i in range(start_port,end_port+1):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((host,i))
            open_ports.append(i)
    except(ConnectionRefusedError):    
        closed_ports.append(i)

print('Open ports:')
for i in open_ports:
    print(i, end = ", ")
print("\nClosed ports:")
for i in closed_ports:
    print(i, end = ', ')

