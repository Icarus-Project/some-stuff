def str_xor():
    res = list()
    str1 = input('Inserire la prima stringa (notazione 0x): ')
    str2 = input('Inserire la seconda stringa (notazione 0x): ')

    str1 = int(str1, base=16)
    str1 = bin(str1)

    str2 = int(str2, base=16)
    str2 = bin(str2)

    str1 = '0' + str1[2:]
    str2 = '0' + str2[2:]

    res_binario = allinea_xor(str1, str2)
    res_binario = int(res_binario, base=2)
    print(hex(res_binario))

def xor_bin(a, b):
    res = ''
    for i in range(len(a)):
        if int(a[i])^int(b[i]) == 1:
            res = res + '1'
        else:
            res = res + '0'
    return res
    
def allinea_xor(a,b):
    diff = len(a) - len(b)
    val = abs(diff)

    if diff > 0:
        b = '0' * val + b
    else:
        a = '0' * val + a

    res = xor_bin(a,b)
    return res
