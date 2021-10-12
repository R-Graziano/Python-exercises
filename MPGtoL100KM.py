def l100kmtompg(liters):
#
# coloca tu código aqui
#
    gal = liters / 3.785411784
    return (100000 / 1609.344) / gal

def mpgtol100km(miles):
#
# coloca tu código aqui
#
    km = miles * 1609.344 / 1000
    return 3.785411784 * 100 / km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))