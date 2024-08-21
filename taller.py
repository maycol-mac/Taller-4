"""Punto 1"""
def imprimir_valores_por_tipo(diccionario):
    
    tipos = {type(valor) for valor in diccionario.values()}
    
    
    for tipo in tipos:
        valores_del_tipo = [valor for valor in diccionario.values() if isinstance(valor, tipo)]
        
        if valores_del_tipo:
            
            valores_ordenados = sorted(valores_del_tipo)
            print(f"Valores de tipo {tipo.__name__}:")
            for valor in valores_ordenados:
                print(valor)


diccionario = {'a': 3,'b': 1.5,'c': 2,'d': 4.2,'e': 'texto'}

imprimir_valores_por_tipo(diccionario)



"""Punto 2"""

def verificar_claves_valores(diccionario1, diccionario2):
   
    for clave, valor in diccionario1.items():
        if clave  in diccionario2: 
            if diccionario2[clave] == valor:
                print(clave,"Esta en el diccionario",True)
            else:
                print(clave,"No esta en el diccionario",False)
        else:
            print(clave,"No esta en el diccionario",False)


diccionario1 = {'a': "Hola", 'b': 2,'c': 3}

diccionario2 = {'a': "Hola",'b': 2,'c': 3,'d': 4}

diccionario3 = {'a': "Text",'b': 5, 'c': 9}

print(verificar_claves_valores(diccionario1, diccionario2)) 
print(verificar_claves_valores(diccionario1, diccionario3))




"""Punto 3"""

def mezclar_diccionarios(dic1, dic2):
    dic_mezclado = dic2.copy()
    dic_mezclado.update(dic1)
    print(dic_mezclado)


diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'd': 5}
resultado = mezclar_diccionarios(diccionario1, diccionario2)

"""Punto 4"""

def filtrar_por_rango_edad(personas):
    personas_filtradas = {}
    edad_min = 20
    edad_max = 25

    for persona in personas:
        nombre, apellido, edad = persona
        
        if edad_min <= edad <= edad_max:
            personas_filtradas[f"{nombre} {apellido}"] = edad

    for nombre_completo, edad in personas_filtradas.items():
        print(f"{nombre_completo}: {edad} años")

lista_personas = [("Juan", "Perez", 25),("Ana", "Gomez", 30),("Luis", "Rodriguez", 22),("Pedro", "García", 35)]

filtrar_por_rango_edad(lista_personas)

