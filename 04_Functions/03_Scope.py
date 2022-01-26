x = 1
y = 2
print(x, y)
def local_scope():
    a = 500
    b = 700
    return a, b


x, y = local_scope()
print(x, y)
