#!/usr/bin/env /usr/bin/python3

from difflib import SequenceMatcher
import subprocess
import re
import hashlib

def run_cmd(cmd, get_output=True, timeout=35, stop_on_error=True):

        "Run cmd logging input and output"
        output = ""
        try : 
            if get_output: 
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True )
                output, err = p.communicate(timeout=timeout)
                rc = p.returncode
            else:
                result = subprocess.check_call(cmd, stderr=subprocess.STDOUT, shell=True, timeout=timeout)
        except subprocess.CalledProcessError as e: 
            if stop_on_error:
                msg = 'Failed sudo_cmd: %s' % str(e)
        return output

#proc = lambda x: subprocess.Popen(x, stdout=subprocess.PIPE, stderr=/dev/null)

#Valid chars , a-z 0-9
def check(test_str):
    pattern = r'[^\.acflst*\-\s]'
    if re.search(pattern, test_str):
        print('Caracter inválido en comando %r, carácteres en corchetes permitidos: [.acflst*- ]\n' % (test_str, ))
        print ('caracter no permitido o incorrecto')

    else:
        try: 
            output = run_cmd(cmd, get_output=True, stop_on_error=True)
            print (output)
        except OSError: 
            print ('ERROR')

while True: 
    try: 
        s = input('J A I L')
    except: 
        break
    if s.strip() == "ls":
        print("¿Deseas comenzar? (s/n)")
        try:
            response = input("Respuesta: ").strip().lower()
        except KeyboardInterrupt:
            print("\n¡BYE!")
            break
        
        if response == "s":
            puntos = 0
            try:
                print("1. Capital del estado de Morelos ")
                response = input("Respuesta: ").strip().lower()
                if response == "cuernavaca":
                    print("¡Correcto!")
                    puntos += 1
                else:
                    print("Incorrecto :(.")
                
                print("2. Frase conocida por muchos programadores ")
                response = input("Respuesta: ").strip().lower()
                if response == "hola mundo":
                    print("¡Correcto!")
                    puntos += 1
                else:
                    print("Incorrecto :c")

                print("3. Año en el que salió el GTA V ")
                response = input("Respuesta: ").strip().lower()
                if response == "2013":
                    print("¡Correcto!")
                    puntos += 1
                else:
                    print("Incorrecto :c")

                print("4. Proceso de reduccion de vulnerabilidades del sistema a traves de herramientas y procesos en la red")
                response = input("Respuesta: ").strip().lower()
                if response == "hardening":
                    print("¡Correcto!")
                    puntos += 1
                else:
                    print("Incorrecto :c")

                print("5- Comando utilizado en bash para crear directorios")
                response = input("Respuesta: ").strip().lower()
                if response == "mkdir":
                    print("¡Correcto!")
                    puntos += 1
                else:
                    print("Incorrecto :c")

                
            except KeyboardInterrupt:
                print("\nRetirada")
                break
        elif response == "n":
            print("¿Mas opciones?")
        else:
            print("Responde 'S' o 'N'.")
            
    elif s.strip() == "d3598d9fa1f79559db82ef3ecf536f28ef7264f5492953cd883f94a46b7a3989":
        print("Lograste escapar con exito, ¡Se libre!")
        break
    else:
        print("¡Lastima! No pudiste escapar :C")

    print(f"Puntos acumulados: ({puntos}/2)\nContinúa hacia adelante")

    if puntos == 5:
        print("(5/5) Has completado tu escape exitosamente")
      
        key = "llave"
        encrypted_key = hashlib.sha256(key.encode()).hexdigest()
        print("Llave:", encrypted_key)
