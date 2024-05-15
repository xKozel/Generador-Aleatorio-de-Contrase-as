import string
import random

def generar_contrasena(longitud=12, complejidad="fuerte", incluir_numeros=True, incluir_mayusculas=True, incluir_minusculas=True, incluir_especiales=True):
    caracteres = ''
    
    if incluir_numeros:
        caracteres += string.digits
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiales:
        caracteres += string.punctuation

    if complejidad == "debil":
        longitud = max(8, longitud)  # Mínimo de 8 caracteres para contraseñas débiles
    elif complejidad == "media":
        longitud = max(10, longitud)  # Mínimo de 10 caracteres para contraseñas medias

    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    
    # Verificar seguridad de la contraseña
    seguridad = "Débil" if longitud < 10 else "Media" if longitud < 14 else "Fuerte"
    
    return contrasena, seguridad

def main():
    longitud = int(input("Ingrese el tamaño deseado de la contraseña (presione Enter para usar el tamaño predeterminado de 12): ") or 12)
    complejidad = input("Ingrese la complejidad deseada de la contraseña (debil/media/fuerte, presione Enter para usar fuerte): ") or "fuerte"
    incluir_numeros = input("¿Incluir números? (s/n, presione Enter para sí): ").lower() == 's'
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n, presione Enter para sí): ").lower() == 's'
    incluir_minusculas = input("¿Incluir letras minúsculas? (s/n, presione Enter para sí): ").lower() == 's'
    incluir_especiales = input("¿Incluir caracteres especiales? (s/n, presione Enter para sí): ").lower() == 's'

    contrasena, seguridad = generar_contrasena(longitud, complejidad, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales)

    print(f"La contraseña generada es: {contrasena}")
    print(f"Seguridad de la contraseña: {seguridad}")

if __name__ == "__main__":
    main()
