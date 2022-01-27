#import random
# from random import random # by saying from random import random we only import the nedded module
#
# import math as maths # can give a package an alias
# print(random())
# print(random())
# print(random())
# print(random())
#
# print(maths.pi)
# import functions.os_functions
# print(functions.os_functions.work_dir)
#
# print(f.work_dir)
# PIP -> PIP Installs Packages (Auto- acronym)

import requests

r = requests.get("https://www.bbc.co.uk")
print(r,type(r))

print(r.status_code)
# print(r.content)



