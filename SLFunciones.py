import streamlit as st
import FuncionesEnArchivo as funcion

option_menu = ["Inicio", "Saludo", "Suma de dos números", "Área de un triangulo", "Calculadora de descuento", "Suma de una lista de números",
               "Funciones con valores predeterminados", "Pares e impares", "Multiplicación con *args", "Información de una persona con **kwargs", "Calculadora flexible"]
selected_option = st.sidebar.selectbox("Opciones: ", option_menu)
match selected_option:
    case "Inicio":
        st.markdown("# Bienvenidos al programa de Christian\n## Selecciona una opción en la parte izquierda de la pantalla.")
        
    case "Saludo":
        nombre = st.text_input("Ingresa tu nombre: ")
        if nombre:
            st.markdown(f"### {funcion.saludar(nombre)}!") #Se saluda con el nombre personalizado.
            
    case "Suma de dos números":
        lista = []
        for i in range(1, 3): #Se pediran dos números.
            n:float = st.number_input(f"Ingresa el número {i}", step=1.0, format="%.4f")
            lista.append(n) #Se agregan los números a una lista
        st.markdown(f"Suma: {funcion.sumar(*lista)}") #Se envia la lista como *args.
        
    case "Área de un triangulo":
        base = st.number_input(f"Ingresa la base", step=1.0, format="%.2f")
        altura = st.number_input(f"Ingresa la altura", step=1.0, format="%.2f")
        st.write(f"El área es {funcion.calcular_area_triangulo(base, altura)}")
        
    case "Calculadora de descuento":
        precio_original:float = st.number_input("Ingresa el precio original del producto", step=20.0, min_value=0.0)
        st.write("Impuesto predeterminado: 16%\nDescuento predeterminado: 10%")
        #Lista de opciones para el usuario
        lista = ["Calcular con descuento e impuesto predeterminado", "Calcular con descuento e impuesto personalizado"]
        opcion = st.selectbox("Selecciona una opción", lista) #El usuario selecciona una opción de la lista.
        match opcion:
            case "Calcular con descuento e impuesto predeterminado":
                #Se envia solo el precio y se usan valores predeterminados
                st.write(f"El precio final es de {funcion.calcular_precio_final(precio=precio_original):.4f}")
            case "Calcular con descuento e impuesto personalizado":
                #Se usan valores personalizados.
                descuento:int = st.number_input("Ingresa el descuento (%)", step = 2, min_value=0, max_value=100)
                impuesto:int = st.number_input("Ingresa el impuesto(%)", step = 2, min_value=0, max_value=100)
                st.write(f"El precio final es de {funcion.calcular_precio_final(precio_original, descuento, impuesto):.4f}")
                
    case "Suma de una lista de números":
        try:
            lista = st.text_input("Ingresa la lista separando los valores con comas: ")
            if lista:
                lista = lista.split(",") # Se crea una lista que separe las strings por comas.
                lista_enteros = [int(val) for val in lista] #Se crea una lista que haga todo el contenido de la otra lista a entero.
                st.write(f"El resultado de la suma es: {funcion.sumar_lista(lista_enteros)}") #Se envía la lista como argumento.
        except ValueError:
            st.error("Hubo un error de sintaxis")
            
    case "Funciones con valores predeterminados":
        nombre = st.text_input("Ingresa el nombre del producto: ")
        lista = ["Calcular con descuento e impuesto predeterminado", "Calcular con descuento e impuesto personalizado"] #Lista de opciones para el usuario.
        opcion = st.selectbox("Ingresa una opcion", lista)
        match opcion:
            case "Calcular con descuento e impuesto predeterminado":
                st.write(funcion.producto(nombre)) #Se envía solo el nombre y se usan valores predeterminados.
            case "Calcular con descuento e impuesto personalizado":
                cantidad = st.number_input("Ingresa la cantidad de productos: ", step = 2, format="%d", min_value=1)
                precio = st.number_input("Ingresa el precio del producto: ", step=2.0, format="%.2f", min_value=0.0)
                st.write(funcion.producto(nombre, cantidad=cantidad, precioxunidad=precio)) #Se usan valores personalizados.

    case "Pares e impares":
        try:
            lista = st.text_input("Ingresa los valores de la lista separados por comas: ")
            if lista:
                lista = lista.split(",") #Se separan los elementos del string por comas, creando una lista
                lista_enteros = [int(val) for val in lista] #Se hacen enteros los elementos de la lista
                listapar, listaimp = funcion.numeros_pares_e_impares(lista_enteros) #Se asigna el resultado de la funcion a dos variables.
                st.write(f"#### La lista con pares es: {listapar}\n#### La lista con impares es {listaimp}") #Se imprimen los resultados.
        except ValueError:
            st.error("Hubo un error en la sintaxis")

    case "Multiplicación con *args":
        argumento_variadico = st.text_input("Ingresa el argumento para la función (separado por comas): ")
        if argumento_variadico:
            argumento_variadico = argumento_variadico.split(",") #Se separa el contenido de la string por comas, creando una lista.
            argumento_enteros = [int(val) for val in argumento_variadico] #Se hacen enteros los elementos de la lista.
            st.write(f"El producto de todos los números es: {funcion.multiplicar_todos(*argumento_enteros)}")
        else:
            st.write(f"El producto de todos los números es: 1")

    case "Información de una persona con **kwargs":
        mi_diccionario:dict = {}
        numero_datos = st.number_input("Ingresa el número de datos a leer: ", step = 1, min_value=1, format="%d") #Se pide n cantidad de datos
        for i in range(1, numero_datos+1): #Se crean n pares de casillas para lectura de datos
            clave = st.text_input(f"Ingresa la clave {i}: ")
            valor = st.text_input(f"Ingresa el valor {i}: ")
            if clave and valor:
                mi_diccionario[clave] = valor #Se añaden a un diccionario

        if st.button("Imprimir los valores:"):
            funcion.informacion_personal(**mi_diccionario) #Se envia el diccionario descompactado.

    case "Calculadora flexible":
        lista = ["Realizar operacion por defecto (suma)", "Seleccionar operacion"] #Opciones para el usuario.
        numero1 = st.number_input("Ingresa el número 1: ", step=2.0)
        numero2 = st.number_input("Ingresa el número 2: ", step=2.0)
        opc = st.selectbox("Seleccionar opción: ", lista) #Se le da a elegir al usuario si usar valores predeterminados o no.
        match opc:
            case "Realizar operacion por defecto (suma)":
                st.write(f"{funcion.calculadora_flexible(numero1, numero2)}") #Se usa "suma" como predeterminado.
            case "Seleccionar operacion":
                operacion = st.text_input("Ingresa la operacion a realizar: ")
                st.write(f"{funcion.calculadora_flexible(numero1, numero2, operacion)}") #Se manda x operacion disponible.