def variavel(txt):
    letra = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if txt[0] in letra:
        return variavel_f(txt[1:])
    if txt[0] == '':
        return 0
    return 1

def variavel_f(txt):
    letra = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if txt[0] in letra:
        return variavel_f(txt[1:])
    if txt[0] == '':
        return 0
    return 1
    
