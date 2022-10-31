def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def main():
    l_si = ['-10', '0', '100']
    l_si_i = [int(s) for s in l_si]
    print(l_si_i)
    # [-10, 0, 100]

    l_sf = ['.123', '1.23', '123']

    l_sf_f = [float(s) for s in l_sf]
    print(l_sf_f)
    # [0.123, 1.23, 123.0]
    return l_si_i

"""
l_multi = ['-100', '100', '1.23', '1.23e2', 'one']
print(type(l_multi))

l_multi_i = [int(s) for s in l_multi if is_int(s)]
print(l_multi_i)
print(type(l_multi_i))

l_multi_f = [float(s) for s in l_multi if is_float(s)]
print(l_multi_f)
"""

a = main()
print(type(a))
