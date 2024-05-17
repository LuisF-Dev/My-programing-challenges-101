"""/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */"""
def r_order(expression):
    r_list = []
    p2 = expression.find(")")
    if p2 == -1:
        p2=100
    k2 = expression.find("}") #? las funciones r_order y l_order recolectan los parentesis,corchetes
    if k2 == -1:              #? y llaves y ven el orden y ademas comprueban si estan todos
        k2=100
    s2 = expression.find("]")
    if s2 == -1:
        s2=100
    if p2 > k2 and p2 > s2:
        p_s2 = "pthird"
        if k2 > s2:
            k_s2 = "ksecond"
            s_s2 = "sfirst"
        else:
            k_s2 = "kfirst"
            s_s2 = "ssecond"
    else:
        if k2 > s2:
            k_s2 = "kthird"
            if p2 > s2:
                p_s2 = "psecond"
                s_s2 = "sfirst"
            else:
                p_s2 = "pfirst"
                s_s2 = "ssecond"
        else:
            s_s2 = "sthird"
            if k2 > p2:
                k_s2 = "ksecond"
                p_s2 = "pfirst"
            else:
                k_s2 = "kfirst"
                p_s2 = "psecond"
    if not s2 == 100:
        r_list.append(s_s2)
    if not k2 == 100:
        r_list.append(k_s2)
    if not p2 == 100:               # !  { [ a * ( c + d ) ] - 5 }
        r_list.append(p_s2)
    r_list.sort()
    return r_list

def l_order(expression):
    l_list = []
    p = expression.find("(")
    k = expression.find("{")
    s = expression.find("[")
    if p > k and p > s:
        p_s = "pfirst"
        if k > s:
            k_s = "ksecond"
            s_s = "sthird"
        else:
            k_s = "kthird"
            s_s = "ssecond"
    else:
        if k > s:
            k_s = "kfirst"
            if p > s:
                p_s = "psecond"
                s_s = "sthird"
            else:
                p_s = "pthird"
                s_s = "ssecond"
        else:
            s_s = "sfirst"
            if k > p:
                k_s = "ksecond"
                p_s = "pthird"
            else:
                k_s = "kthird"
                p_s = "psecond"
    if not s == -1:
        l_list.append(s_s)
    if not k == -1:
        l_list.append(k_s)
    if not p == -1:               # !  { [ a * ( c + d ) ] - 5 }
        l_list.append(p_s)
    l_list.sort()
    
    return l_list

def equilibrator(expression):
    if not l_order(expression) == r_order(expression):
        return False
    c = 0
    e = 0
    c +=expression.count(")") + expression.count("(")
    c +=expression.count("]") + expression.count("[")   #? luego aqui se hacen operaciones matematicas basicas
    c +=expression.count("{") + expression.count("}")    #? para comprobar si no falta algun parentesis o etc
    for i in str(c):
        if int(i) % 2 == 0:
            e += 2
        else:
            e += 0.3
    if e % 2 == 0:
        return True
        
    else:
        return False
    
if equilibrator(" { [ a * ( c + d )  - 5 } ") == False:
    print("la expresion no esta equilibrada")
else: 
    print("la expresion si esta equilibrada")

