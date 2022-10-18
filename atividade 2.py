#--------------------------------Real para binário--------------------------

def intby(m):
    
    a = str()
    n = int(m) 

    if n == 0:
        a += '0'

    else:
        while n != 0: 
            if n % 2 == 0:
                a += '0'
            else:
                a += '1'
            n = n//2

    bi = a[::-1]
    return bi
    
def decby(m): 
      
    a = str()
    b = intby (m)
    n = m-int(m) 

    if b == '0':

        for i in range (0, 31):

        
            x = 2 * n 
            y = int(x) 

            if y == 1:
                a+= '1'
            else:
                a+='0'
            n = x-y
            i -= 1

    else:
        
        for i in range (len(b), 24):

            
            x = 2 * n 
            y = int(x) 

            if y == 1:
                a+= '1'
            else:
                a+='0'
            n = x-y
            i -= 1
      
    return(a)



def bi(m): 
      
    
    
    a = intby(m) 
    b = decby(m) 
    c =str() 
    c += a
    c += '.'
    c += b

    return c

#-------------------------------Real para binário 64 bits-------------------------------

def decby64(m): 
      
    a = str()
    b = intby (m)
    n = m-int(m)

    if b == '0':

        for i in range (0, 60):

        
            x = 2 * n 
            y = int(x) 

            if y == 1:
                a+= '1'
            else:
                a+='0'
            n = x-y
            i -= 1

    else:
        
        for i in range (len(b), 53):  
             
                x = 2 * n 
                y = int(x) 
                if y == 1:
                    a+= '1'
                else:
                    a+='0'
                n = x-y
                i -= 1
      
    return(a)

def bi64(m): 
      
    
    
    a = intby(m) 
    b = decby64(m) 
    c =str() 
    c += a
    c += '.'
    c += b

    return c

#----------------------------------------Binário para hexa-------------------------

def hexa (m):
    num = int(m, 2)
      
    
    hex_num = format(num, 'X')
    return hex_num


#------------------------------------Expoente do bias---------------------------------
def expbia (m):
    num = float(m)

    exp = format(num, '.1E')
    exp = exp[4:]
    exp_num = int(exp)

    return exp_num

#------------------------------------Normaização de mantissa--------------------------------

def norm_mant (m):
    num = int(m)

    mant = str(num)
    mant = mant[:1] + '.' + mant[1:]   
    
    return (mant)
        
#---------------------------------------------Bias em binario----------------------------
def biatriz(m):

    a = str()
    n = int(m)

    for i in range(0, 8):

        if n % 2 == 0:
            a += '0'
        else:
            a += '1'
        n = n//2

    bi = a[::-1]
    return bi

#---------------------------------------------Bias em binario 64 bits----------------------------
def biatriz64(m):

    a = str()
    n = int(m)

    for i in range(0, 11):

        if n % 2 == 0:
            a += '0'
        else:
            a += '1'
        n = n//2

    bi = a[::-1]
    return bi

print('Nome do Projeto: Conversor de números reais para IEEE 754\n')
print('Integrantes:\n' 'Lucas Bernardino dos Santos\n''Alan Soares Lima\n''Icaro Henrique\n')
n =  float(input('Dado de entrada: '))
print('Resultado\n')

#------------------------------------------------Para positivos---------------------------------------------------------

if n > 0:
    print('Padrão IEEE-754 de 32 bits')
    print('Sinal = Positivo -> 0')
    
    b = bi (n)
    print('Mantissa não normalizada =', b)

    mant = intby (n) + decby (n)
    exp = expbia (b)
    mantn = norm_mant(mant)
    print('Mantissa normalizada = {} x 2^{}'.format(mantn, exp))

    bias = 127 + exp
    biasby = biatriz (bias)
    print('Expoente = {} -> Com bias(127) = {} -> Em binário = {}\n'.format(exp, bias, biasby))

    totby = mantn[2:25]
    total = '0'
    total += biasby
    total += totby

    toth = hexa(total)
    print('Representação no padrão: Hexadecimal = {}'.format(toth))

    for i in range (4, 36, 5):
        total = total[:i] + ' ' + total[i:]
    print('Binário = {}\n'.format(total))
    

#----------------------64-bits--------------------------------------------------------


    print('Padrão IEEE-754 de 64 bits')
    print('Sinal = Positivo -> 0')

    b64 = bi64 (n)
    print('Mantissa não normalizada =', b64)

    mant64 = intby (n) + decby64 (n)
    exp64 = expbia (b64)
    mantn64 = norm_mant(mant64)
    print('Mantissa normalizada = {} x 2^{}'.format(mantn64, exp64))    
        
    
    bias64 = 1023 + exp
    biasby64 = biatriz64 (bias64)
    print('Expoente = {} -> Com bias(1023) = {} -> Em binário = {}\n'.format(exp64, bias64, biasby64))

    totby64 = mantn64[2:54]
    total64 = '0'
    total64 += biasby64
    total64 += totby64
    
    toth64 = hexa(total64)
    print('Representação no padrão: Hexadecimal = {}'.format(toth64))

    for j in range (4, 76, 5):
        total64 = total64[:j] + ' ' + total64[j:]
    print('Binário = {}\n'.format(total64))

#-----------------------------------------------------------Para negativos-------------------------------------------    

else:
    print('Padrão IEEE-754 de 32 bits')
    print('Sinal = Positivo -> 1')

    n *= -1
    b = bi (n)
    print('Mantissa não normalizada =', b)

    exp = expbia (b)
    

    mant = intby(n) + decby(n)
    mantn = norm_mant(mant) 
    print('Mantissa normalizada = {} x 2^{}'.format(mantn, exp))

    bias = 127 + exp
    biasby = biatriz (bias)
    print('Expoente = {} -> Com bias(127) = {} -> Em binário = {}\n'.format(exp, bias, biasby))

    totby = mantn[2:25]
    total = '1'
    total += biasby
    total += totby

    toth = hexa(total)
    print('Representação no padrão: Hexadecimal = {}'.format(toth))

    for i in range (4, 36, 5):
        total = total[:i] + ' ' + total[i:]
    print('Binário = {}\n'.format(total))


#-----------------------------------------64 bits---------------------------------------------------

    print('Padrão IEEE-754 de 64 bits')
    print('Sinal = Positivo -> 1')

    
    b64 = bi64 (n)
    print('Mantissa não normalizada =', b64)

    exp64 = expbia (b64)
    

    mant64 = intby(n) + decby64(n)
    mantn64 = norm_mant(mant64) 
    print('Mantissa normalizada = {} x 2^{}'.format(mantn64, exp64))

    bias64 = 1023 + exp
    biasby64 = biatriz64 (bias64)
    print('Expoente = {} -> Com bias(1023) = {} -> Em binário = {}\n'.format(exp, bias64, biasby64))

    totby64 = mantn64[2:54]
    total64 = '1'
    total64 += biasby64
    total64 += totby64

    toth64 = hexa(total64)
    print('Representação no padrão: Hexadecimal = {}'.format(toth64))

    for j in range (4, 76, 5):
        total64 = total64[:j] + ' ' + total64[j:]
    print('Binário = {}\n'.format(total64))

