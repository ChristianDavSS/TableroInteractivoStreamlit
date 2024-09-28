import streamlit as st

def saludar(nombre):
    return f"¡Hola, {nombre}!"


def sumar(a:float, b:float)->float:
    return a+b


def calcular_area_triangulo(base, altura):
    return (base*altura)/2


def calcular_precio_final(precio:float, descuento=10, impuesto=16)->float:
    precioConDescuento = precio - (precio * (descuento/100))
    return precioConDescuento + (precioConDescuento * (impuesto/100))


def sumar_lista(n:list)->int:
    s = 0
    for val in n:
        s += val
    return s


def producto(nombre:str, cantidad:int = 1, precioxunidad = 10):
    return f"Producto {nombre}  -  Precio final: {precioxunidad * cantidad}"


def numeros_pares_e_impares(n:list)-> list:
    lista_pares = []
    lista_impares = []
    for val in n:
        if val % 2 == 0:
            lista_pares.append(val)
        else:
            lista_impares.append(val)
    return lista_pares, lista_impares


def multiplicar_todos(*n):
    producto = 1
    for val in n:
        producto *= val
    return producto


def informacion_personal(**kwargs):
    for clave, val in kwargs.items():
        st.write(f"{clave}: {val}")
        
        
def calculadora_flexible(num1:float, num2:float, operacion="suma")->float:
    operacion = operacion.lower()
    match operacion:
        case "suma":
            return num1 + num2
        case "resta":
            return num1 - num2
        case "multiplicacion":
            return num1 * num2
        case "division":
            return num1 / num2
        case _:
            return "No valido"