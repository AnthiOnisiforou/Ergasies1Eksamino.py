arithmos= raw_input("dwse arithmos apo 1 - 1000:")
dekada=["I","II","III","IV","V","VI","VII","VIII","IX"]
ekatontada=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
xiliada=["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
dekadesxiliades=["M","MM","MMM","M-V","-V","-VM","-VMM","-VMMM","M-X"]
ekatontadesxiliades=["-X","-X-X","-X-X-X","-X-L","-L","-L-X","-L-X-X","-L-X-X-X","-X-C"]
ekatomirio=["-C","-C-C","-C-C-C","-C-D","-D","-D-C","-D-C-C","-D-C-C-C","-C-M"]
arith= int(arithmos)
def mik1000(num):
    if (monades != 0 and dekades != 0 and ekatontades != 0):
        return xiliada[ekatontades - 1] + ekatontada[dekades - 1] + dekada[monades - 1]
    elif (monades == 0 and dekades != 0 and ekatontades != 0):
        return xiliada[ekatontades - 1] + ekatontada[dekades - 1]
    elif (dekades == 0 and monades != 0 and ekatontades != 0):
        return xiliada[ekatontades - 1] + dekada[monades - 1]
    elif (ekatontades == 0 and dekades != 0 and monades != 0):
        return ekatontada[dekades - 1] + dekada[monades - 1]
    elif (ekatontades == 0 and monades == 0 and dekades != 0):
        return ekatontada[dekades - 1]
    elif (ekatontades == 0 and dekades == 0 and monades != 0):
        return dekada[monades - 1]
    elif (monades == 0 and dekades == 0 and ekatontades != 0):
        return xiliada[ekatontades - 1]
    elif (monades == 0 and dekades == 0 and ekatontades != 0):
        return xiliada[ekatontades - 1]
    elif(monades == 0 and dekades == 0 and ekatontades == 0):
        return ""
def meg1000(num):
    if (xiliades != 0 and dekxil != 0 and ekxil != 0):
        return ekatomirio[ekxil - 1] + ekatontadesxiliades[dekxil - 1] + dekadesxiliades[xiliades - 1]
    elif (xiliades == 0 and dekxil != 0 and ekxil != 0):
        return ekatomirio[ekxil - 1] + ekatontadesxiliades[dekxil - 1]
    elif (dekxil == 0 and xiliades != 0 and ekxil != 0):
        return ekatomirio[ekxil - 1] + dekadesxiliades[xiliades - 1]
    elif (ekxil == 0 and dekxil != 0 and xiliades != 0):
        return ekatontadesxiliades[dekxil - 1] + dekadesxiliades[xiliades - 1]
    elif (ekxil == 0 and xiliades == 0 and dekxil != 0):
        return ekatontadesxiliades[dekxil - 1]
    elif (ekxil == 0 and dekxil == 0 and xiliades != 0):
        return dekadesxiliades[xiliades - 1]
    elif (xiliades == 0 and dekxil == 0 and ekxil != 0):
        return ekatomirio[ekxil - 1]
    elif (xiliades == 0 and dekxil == 0 and ekxil != 0):
        return ekatomirio[ekxil - 1]

ekatontades= ((arith//10)//10)%10

dekades = (arith//10)%10

monades = arith%10
xiliades=(arith//1000)%10
dekxil=(arith//1000)//10%10
ekxil=(arith//10000)//10
if(arith<1000):
    latin = mik1000(arith)
elif(arith>1000 and arith<=999999):
    latin= str(meg1000(arith))+str(mik1000(arith))
else:
    print ("o arithmos den einai mesa sta oria")

print monades
print dekades
print ekatontades
print xiliades
print dekxil
print ekxil

print latin