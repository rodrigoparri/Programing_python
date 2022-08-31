# bob = dict(name="Bob", age="42", pay=40000, dep="edificación")
# carlos = dict(name="Carlos", age="32",pay=50000, dep="dirección")
# pili = dict(name="Maria Pilar", age="32",pay=50000,dep="bim")
# ines = dict(name="Ines",age="25",pay=35000, dep="i+d+i")
# rodro = dict(name="Rodro", age="23",pay=18000,dep="it")
# base_emp = dict(bob=bob,carlos=carlos,pili=pili,ines=ines,rodro=rodro)

# def flexionSimpleRect():
#      return "elegida flexión simple"
#
# def flexionSimpleT():
#     return "elegida flexión simple sección en T"
#
# def flexionCompuestaRect():
#     return "elegida flexión compuesta rectangular"
#
# def flexionCompuestaCir():
#     return "elegida flexión compuesta circular"
#
# def cortante():
#     return "elegido cortante"


# def intersec(n,m):
#     res = [x for x in n if x in m]
#     res = sorted([x for x in res if res.count(x) = 1])
##    for i in res:
##        if res.count(i) > 1:
##            res.remove(i)
#     return res

# def cambioglobal(a):
#     global n
#     n = 3+a
#     return n


from imports import import_functions




if __name__ == "__main__":

    # salarios = list()
    # for key in base_emp:
    #     salarios.append(base_emp[key]["pay"])
    # print(salarios)
    #
    # for key in base_emp:
    #     print(key, "=>", base_emp[key], "\r")

    # selección = input("seleciona el cálculo a ejecutar\n")
    # calculos = {"flexión simple":flexionSimpleRect(),
    #             "flexión simple sección en T":flexionSimpleT(),
    #             "flexión compuesta rectangular":flexionSimpleRect(),
    #             "flexión compuesta circular":flexionCompuestaCir(),
    #             "cortante":cortante()
    #             }
    # calc_sel = calculos[selección]
    # print(calc_sel)

    # l = [0,1,2,3,4,5]
    # m = ["a","b","c","d","e"]
    # n ={}
    # for (k,v) in list(zip(l,m)): #recorre una lista en la que se guardan tuplas (clave, valor)
    #     n[k] = v
    # print(n)
    #
    # n = dict(zip(l,m))

    # l = [1,2,3,4,5]
    # m = ["a","b","c","d","e"]
    # n = [x for i in zip(l,m) for x in i]
    # a = 1
    # m = [m[:a] + l + m[a:] for i in m if i == m[a]]
    # m = [x for i in m for x in i ]
    # for i in l:
    #     if i == 2:
    #         l = l[:2] + m + l[2:]

    # print(m)
    # print(n)
    # n = [c for c in list(zip(l,m))]
    # d = dict(zip(l,m))
    # e = list(zip(l,m))
    # print(n)
    # print(d)
    # print(e)
    # x= []
    # for i,j in enumerate(m):
    #     x.append(i)
    #     x.append(j)
    # print(x)

    # for i,l in enumerate(m):
    #     print("%s) %s" % (i, l.rstrip()))
    #     print("{}) {}".format(i, l.rstrip()))

    # f = open("arch_test/test.txt")
    # for line in f:
    #     print(line.upper(), end="")
    # a = [2,35,4,5,2,8,3,

    # n = 7
    # b = 1
    # print(n)
    #  despues de llamar a cambio global se redefine b de forma global.
    # cambioglobal(b)
    # print(n)
    # r = [2,13,5,5,4,6,5]
    # # p = dict(enumerate(r))
    # i = enumerate(r).__iter__()
    # print(i.__next__())
    # print(i.__next__())
    # print(i.__next__())
    # print(i.__next__())
    # print(i.__next__())
    #
    # for t in enumerate(r):
    #     print(t)

    # podemos acceder a las variables globales del módulo importado y podemos cambiarlas tanto de forma explícita
    # como a través de una función para ello
    # print(import_functions.x)
    # import_functions.chgvarx(6)
    # import_functions.x = 7
    # print(import_functions.x)
    #
    # l = list(globals())
    # print(l)


    import_functions.test()

    print(import_functions.var)



