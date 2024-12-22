i = 1
a = 0
b = 1
with open('IP_loopback.txt', 'w') as file:
    while i < 1025:
        file.write(f'interface loopback {i} \n')
        file.write(f'ip address 20.0.{a}.{b} 255.255.255.255 \n')
        file.write('exit \n')
        i = i+1
        b = b+1
        if b == 256:
            b = 0
            a = a+1
file.close()
