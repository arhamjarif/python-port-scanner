import socket
import time
import datetime

#User Input
host = input("Enter IP: ")
while True:
    try:
        start_port = int(input("Enter first port: "))
        end_port = int(input("Enter last port: "))
        if not 1 <= start_port <= 65535 or not 1 <= end_port <= 65535 or start_port > end_port:
            print('Invalid start and/or end ports.Please try again.')
        else:
            break
    except(ValueError):
        print("Please input numbers")


#Required variables
start_time = time.perf_counter()
open_ports = []
closed_ports = []
filtered_ports = []


#Port scanning
for i in range(start_port,end_port+1):
    print(f'Scanning port: {i}...')
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((host,i))
            open_ports.append(i)
    except(ConnectionRefusedError):    
        closed_ports.append(i)
    except(TimeoutError):
        filtered_ports.append(i)
    except(OSError,socket.gaierror):
        print('Could not establish connection to target host')
        break


#Printing to console
print('Open ports:')
for i in open_ports:
    try:
        print(f'{i} {socket.getservbyport(i)}')
    except(OSError):
        print(f'{i} Unknown')
print("\nClosed ports:")
for i in closed_ports:
    try:
        print(f'{i} {socket.getservbyport(i)}')
    except(OSError):
        print(f'{i} Unknown')
print('\nFiltered ports:')
for i in filtered_ports:
    try:
        print(f'{i} {socket.getservbyport(i)}')
    except(OSError):
        print(f'{i} Unknown')
end_time = time.perf_counter()
print(f'Execution time: {end_time - start_time:.2f} seconds')


#Save functionalilty to 'report.txt'
save_action = input('Would you like to save this scan report?\n1. Yes\n2. No\nYour choice: ')
if save_action == '1':
    now = datetime.datetime.now()
    fnow = now.strftime('%Y-%m-%d %H:%M:%S')
    with open("report.txt","wt") as file:
        file.write(f'PORT SCAN REPORT\n\nTarget: {host}\nTime: {fnow}\nPort Range: {start_port}-{end_port}\n\nOpen Ports:\n')
        for i in open_ports:
            try:
                file.write(f'{i} {socket.getservbyport(i)}\n')
            except(OSError):
                file.write(f'{i} Unknown\n')
        file.write('\n\nClosed Ports:\n')
        for i in closed_ports:
            try:
                file.write(f'{i} {socket.getservbyport(i)}\n')
            except(OSError):
                file.write(f'{i} Unknown\n')
        file.write('\n\nFiltered Ports:\n')
        for i in filtered_ports:
            try:
                file.write(f'{i} {socket.getservbyport(i)}\n')
            except(OSError):
                file.write(f'{i} Unknown\n')
        file.write(f'\n\nScan Duration: {end_time - start_time:.2f} seconds')

