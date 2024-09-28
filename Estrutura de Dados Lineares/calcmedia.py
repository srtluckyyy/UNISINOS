
# volume piramide triangular = 1/3 * area da base * altura
def volume_piramide_triang(base, altura):
    return (1/3) * (base * altura)

# area da base = (base * altura) / 2
def area_base(base, altura):
    return (base * altura) / 2

# area face lateral = (comprimento_base * altura_inclinada) / 2    
def area_face_lateral(base, altura):
    return (base * altura) / 2

def area_face_lateral_equilatero(altura, comprimento_base):
    comprimento_base /= 2
    triangulo1 = (altura * comprimento_base) / 2
    triangulo2 = (altura * comprimento_base) / 2
    return triangulo1 + triangulo2

# area da superficie = area da base + 3 * area face lateral
def area_superficie(area_base, area_face_lateral, area_face_lateral_equilatero):
    return area_base + 2 * area_face_lateral + area_face_lateral_equilatero

# piramide triangular:
# face 1: base = 12, altura = 12, hipotenusa = x
# face 2: base = 12, altura = 12, hipotenusa = x
# face 3: comprimento_base = hipotenusa, altura = 12, diagonal = y
# calcular a area total e o volume
base = 12
altura = 12
comprimento_base = base ** 2 + altura ** 2
altura_equilatero = ((3 ** 0.5) * altura) / 2
apotema_base = comprimento_base / 2
altura_inclinada = altura_equilatero ** 2 + apotema_base ** 2

areaBase = area_base(base, altura)
areaFaceLateral = area_face_lateral(base, altura)
areaFaceLateralEquilatero = area_face_lateral_equilatero(altura, comprimento_base)
areaSuperficie = area_superficie(areaBase, areaFaceLateral, areaFaceLateralEquilatero)
volume = volume_piramide_triang(base, altura)

print(f'Area da base: {areaBase}cm²')
print(f'Area da face lateral: {areaFaceLateral}cm²')
print(f'Area da superficie: {areaSuperficie}cm²')
print(f'Volume: {volume}cm³')

