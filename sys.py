#####
# modulo del sistema
#####

import sys

print(sys.path)

print(sys.platform)

for argumento in sys.argv:
	print(argumento)

print(sys.getrecursionlimit())

sys.setrecursionlimit(1500)

print(sys.getrecursionlimit())