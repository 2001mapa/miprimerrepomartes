#Datos en Python
userDB = "hidrotech123"
passwordDB = "admin123*"

print('Software tech hidroituango')
print('**************************')
userName = input('Digita tu usuario: ')
userPassword = input('Dijita tu contraseña: ')

if userDB == userName and passwordDB == userPassword:
    print("Exito en su usuario")
else:
    print("Fallaste")
    
""" print("Exito en su usuario") if userDB == userName and passwordDB == userPassword else print("Fallaste") """ #Este es un Operador ternario
    