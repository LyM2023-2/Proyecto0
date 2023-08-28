import re



def split_line(line):
    # Utiliza una expresión regular para dividir la línea por espacios y paréntesis
    parts = re.split(r'([(\s,)]+)', line)
    
    # Elimina espacios en blanco vacíos y comas de la lista
    parts = [part.strip() for part in parts if part.strip() not in ['', ',']]
    
    return parts



simple_condition= ["jump", "walk", "leap"]
dir = ["front","right","left","back"]
ori = ["north","south","west","east"]
rot = ["left","right","around"]
vars = []
proc = []


def comDefVar(linea):
    correcto = True
    if (linea[0] == 'defVar'):
        if len(linea) != 3:
            correcto = False
        elif linea[1].isdigit():
            correcto = False
        elif not linea[2].isdigit():
            correcto = False
        else:
             vars.append(linea[1])
        print(vars)
    return correcto

def condicionSimple2(linea):
    correcto = True
    
    if linea[0] in simple_condition:
        expected_length = 4 if len(linea) == 4 else 5
        
        if len(linea) != expected_length:
            
            correcto = False
        elif linea[1] != "(" or linea[-1] != ")":
            correcto = False
        else:
            arg_index = 2 if expected_length == 4 else 3
            argument = linea[arg_index]
            
            if argument not in vars and not argument.isdigit():
                print("xd")
                correcto = False
                
            if expected_length == 5 and argument not in dir + ori:
                print("xdd")
                correcto = False
    
    else:
        correcto = False
    
    return correcto


def condicionSimple(linea):
    correcto = True
    if linea[0] == "jump":
        if len(linea) != 5:
            correcto = False
        elif not linea[2].isdigit() and linea[2] not in vars:
            correcto = False
        elif not linea[3].isdigit() and linea[3] not in vars:
            correcto = False
        elif linea[1] != "(" or linea[4] != ")":
             correcto = False
    elif linea[0] == "walk":
        if len(linea) == 4:
            if linea[2] not in vars and not linea[2].isdigit():
                print("jskd")
                correcto = False
            elif linea[1] != "(" or linea[3] != ")":
                correcto = False
        elif len(linea) == 5:
            if linea[2] not in vars and not linea[2].isdigit():
                correcto = False
            elif linea[1] != "(" or linea[4] != ")":
                correcto = False
            elif linea[3] not in dir and linea[3] not in ori:
                print("5 elementos")
                correcto = False
        else:
             correcto = False
    elif linea[0] == "leap":
        if len(linea) == 4:
            if not linea[2].isdigit() and linea[2] not in vars:
                correcto = False
            elif linea[1] != "(" or linea[3] != ")":
                correcto = False
        elif len(linea) == 5:
            if not linea[2].isdigit() and linea[2] not in vars:
                correcto = False
            elif linea[1] != "(" or linea[4] != ")":
                correcto = False
            elif linea[3] not in dir and linea[3] not in ori:
                correcto = False
        else:
                correcto = False
    elif linea[0] == "turn":
          pass
    elif linea[0] == "turnto":
          pass
    elif linea[0] == "drop":
          pass
    elif linea[0] == "get":
          pass
    elif linea[0] == "grab":
          pass
    elif linea[0] == "letGo":
          pass
    elif linea[0] == "nop":
          pass
     
    elif linea[0] in vars:
            if len(linea) != 3:
                correcto = False
            elif not linea[2].isdigit():
                correcto = False
            elif linea[1] != "=":
                correcto = False

     
    
    return correcto
     



def comDefProc(linea):
    correcto = True
    if (linea[0] == 'defProc'):
        if len(linea) < 3:
            correcto = False
        elif len(linea) == 3:
            if not (linea[2][0] == "(" and linea[2][-1] == ")"):
                correcto = False
        else:
            if not (linea[2] == "(" and linea[-1] == ")"):
                correcto = False
        if correcto:
            if linea[1].isdigit():
                correcto = False
            for i in range(3,len(linea)-1):
                print(i)
                if linea[i].isdigit():
                    correcto = False
                    break
                else:
                    vars.append(linea[i])
    return correcto
            
        




esBloque = False
conteoLlaves = 0



def validar(linea):
    global conteoLlaves
    global esBloque
    if len(linea) == 0:
        print("ERROR")
    if linea[0] == "{" and len(linea) == 1:
        esBloque = True
        conteoLlaves += 1
    if linea[0] == "}" and len(linea) == 1:
        conteoLlaves -= 1
        if conteoLlaves == 0:
            esBloque = False
        if conteoLlaves < 0:
            print("ERROR")
    if linea[len(linea)-1] == ";":
        if esBloque:
            linea = linea[:-1]
        else:
            print("ERROR")
    
    if not comDefVar(linea):
        print("ERROR")
    if not condicionSimple2(linea):
        print("ERROR")
    if not comDefProc(linea):
        print("ERROR")
    
   
        
    
        
    print(linea)















file_path = "prueba.txt"
with open(file_path, 'r') as file:
            line_number = 0
            stack = []
            for line in file:
                line_number += 1
                line = split_line(line)
                validar(line)