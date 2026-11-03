from ipaddress import *

net = ip_network("192.168.155.15/255.255.224.0", strict=False) # Задаём сеть. Сначала адрес, затем маска
# strict - параметр, который показывает, является ли этот адрес адресом сети (True) или адресом узла (False)

network_list = list(net)
print(network_list[0]) # адрес сети
print(network_list[1]) # наименьший возможный адрес узла
print(network_list[-2]) # наибольший возможный адрес узла
print(network_list[-1]) # широковещательный адрес

print(net.network_address) # адрес сети
print(net.broadcast_address) # широковещательный адрес
print(net.hosts()) # возвращает все возможные адреса устройств (итерируемый объект). Объекты типа IPv4adress
print(net.netmask) # возвращает маску сети

for ip in net:
    print(f"{ip:b}") # ПЕРЕВОД АДРЕСА В ДВОИЧНУЮ СИСТЕМУ СЧИСЛЕНИЯ! ВЕРНЕТ СТРОКУ ИЗ 32 БИТ!
