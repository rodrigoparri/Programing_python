var = 99




def local():
    var = 0

def var1():
    global var
    var += 1

def var2():
    var = 0
    from imports import import_functions
    import_functions.var += 1

# def var3():
#     var =0
#     import sys
#     glob = sys.modules
#     glob.var += 1

def test():
    print(var)
    local();var1();var2() #;var3()       #llama a varias funciones en una línea ??
    print(var)

if __name__ == "__main__":

    var3()
    print(var)
