"""manejo de re."""
import re

my_string = "luis_r@cisco.com"
my_regex = re.search("(.+)@(.+)", my_string)
my_r = re.compile("(.+)@(.+)")
if my_r:
    result = my_r.search(my_string)
    print(result.group(2))
    if len(result.groups()) > 0:
        print(result.groups())

'''
No serie
modelo
MAC
Version de soft
uptime
ubicacion del sistema
IP management'''
