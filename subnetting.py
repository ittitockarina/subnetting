import ipaddress

def get_ip_binary(ip):
  ip_binary = ''

  for octet in ip.split('.'):
    binary_octet = format(int(octet), 'b')
    ip_binary += f"{binary_octet}."

  return ip_binary[:-1]

values = [
  {
    'type': 'A',
    'prefix': '8'
  },
  {
    'type': 'B',
    'prefix': '16'
  },
  {
    'type': 'C',
    'prefix': '24'
  }
]

ip = '218.35.50.0'

print("Alumna: Isabel Karina Ttito Campos")
print(f"IPv4: {ip}")

for value in values:
  print('\n\n')

  network = f"{ip}/{value.get('prefix')}"
  net = ipaddress.ip_network(network, strict = False)
  hosts = list(net.hosts())
  
  print("Alumna: Isabel Karina Ttito Campos")
  print(f"Network Address: {net.network_address}")
  print(f"Usable Host IP Range: {hosts[0]} ———————————— {hosts[-1]}")
  print(f"Broadcast Address: {net.broadcast_address}")
  print(f"Total Number of Hosts: {net.num_addresses}")
  print(f"Number of Usable Hosts: {len(hosts)}")
  print(f"Subnet Mask: {net.netmask}")
  print(f"Wildcard Mask: {net.hostmask}")
  print(f"Binary Subnet Mask: {get_ip_binary(net.netmask.__str__())}")
  print(f"IP Class: {value.get('type')}")
  print(f"IP Type: {'public' if net.is_global else 'private'}")
