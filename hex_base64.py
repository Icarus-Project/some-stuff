base64 = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',                    #dizionario base64
          12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',
          23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',31:'f',32:'g',33:'h',
          34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',43:'r',44:'s',
          45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',51:'z',52:0,53:1,54:2,55:3,56:4,57:5,
          58:6,59:7,60:8,61:9,62:'+',63:'/'}


def hex_base64():
    numero = input('Inserire il numero esadecimale (notazione 0x): ')
    bit = binario(numero)                   #prima viene convertito in binario...
    divisi = div_str(bit)                   #...stringa binaria suddivisa in blocchi
    convertito = in_base(divisi)            #...convertito in lista base64
    res=unisci(convertito)                  #...caratteri in lista, uniti in una stringa
    
    return res

    
def binario(numero):                                #funzione che retituisce il numero in binario
    numero = int(numero, base=16)
    numero = bin(numero)
    numero = '0' + numero[2:] #numero in binario pulito
    return numero



def div_str(stringa):                           #suddivide la stringa in blocchi da 6 bit
    li = list()
    if len(stringa)%6 != 0:
        r = len(stringa)%6
        stringa = stringa + '0'*(6-r)
        print(stringa)
    while len(stringa) != 6:
        c = stringa[0:6]
        #print(c)
        li.append(c)
        stringa = stringa[6:len(stringa)]
    li.append(stringa)

    return li


def in_base(lista):
    res = list()

    for block in lista:
        c = int(block, base=2)
        res.append(base64[c])

    return res

def unisci(lista):
    a=''
    for c in lista:
        a = str(a) + str(c)
    return a
