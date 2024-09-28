# Explicación del código
## Tablero interactivo utilizando funciones en Streamlit. Hecho con Python.
### Christian David Sánchez Sánchez 3°B
Este código nos permitió realizar un tablero interactivo para los usuarios en Streamlit, para que estos puedan realizar distintos cálculos de manera rápida y eficiente.
El código fue realizado con las funciones hechas móduladas o hechas en archivos .py diferentes para tener más control y claridad en nuestro código. Solo tuvimos que importarlas, asi como la libreria Streamlit.
```python
import streamlit as st
import FuncionesEnArchivo as funcion
option_menu = ["Inicio", "Saludo", "Suma de dos números", "Área de un triangulo", "Calculadora de descuento", "Suma de una lista de números",
               "Funciones con valores predeterminados", "Pares e impares", "Multiplicación con *args", "Información de una persona con **kwargs", "Calculadora flexible"]
```

Como podemos darnos cuenta, importamos desde nuestro directorio FuncionesProgramaSL todos nuestros archivos con las funciones a utilizar en el programa y, además, creamos una lista con todas las opciones que va a tener disponibles para el uso del usuario. para que el usuario la seleccione, utilizamos:
```python
selected_option = st.sidebar.selectbox("Opciones: ", option_menu)
```

Una vez hecho esto, hacemos pattern matching a las opciones para que el usuario ingrese a la funcionalidad que desea.
```python
case "Inicio":
    st.markdown("# Bienvenidos al programa de Christian\n## Selecciona una opción en la parte izquierda de la pantalla.")
```
Esta opción es la de la pantalla principal y solo nos da una bienvenida.

```python
case "Saludo":
    nombre = st.text_input("Ingresa tu nombre: ")
    if nombre:
        st.markdown(f"### {funcion.saludar(nombre)}!") #Se saluda con el nombre personalizado.
```
Esta otra opción primero debes ingresar tu nombre y, al ingresarlo, se desplegará un mensaje saludandote.

```python
case "Suma de dos números":
    lista = []
    for i in range(1, 3): #Se pediran dos números.
        n:float = st.number_input(f"Ingresa el número {i}", step=1.0, format="%.4f")
        lista.append(n) #Se agregan los números a una lista
    st.markdown(f"Suma: {funcion.sumar(*lista)}") #Se envia la lista como *args.
```
En esta opción se crea una lista vacia y un ciclo for el cual creará dos cuadros para pedir números y, al momento en el que el usuario los ingrese, se agregarán a una lista para ser mandados como argumento a nuestra función.

```python
case "Área de un triangulo":
    base = st.number_input(f"Ingresa la base", step=1.0, format="%.2f")
    altura = st.number_input(f"Ingresa la altura", step=1.0, format="%.2f")
    st.write(f"El área es {funcion.calcular_area_triangulo(base, altura)}")
```
En esta opción le pedimos al usuario que nos ingrese la altura y la base del triangulo para poder pasarlos a nuestra funcion, la cual aplica la formula del área del triangulo y nos retorna el resultado.

```python
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
```
En este case primero se le pide al usuario que ingrese el precio original del producto y, haciendo uso de una lista con opciones y una selectbox, se le da a elegir si quiere utilizar los valores predeterminados de descuento e impuesto o quiere usar valores personalizados. Si elige que quiere los predeterminados, hacemos la llamada a la función dentro de un print pasandole de argumento solo el precio original del producto pero, si elige los valores personalizados, se abriran dos lineas para que el usuario ingrese el descuento y el impuesto para aplicarle al producto y se le pasan 3 arguemntos a la función.

```python
case "Suma de una lista de números":
    try:
        lista = st.text_input("Ingresa la lista separando los valores con comas: ")
        if lista:
            lista = lista.split(",") # Se crea una lista que separe las strings por comas.
            lista_enteros = [int(val) for val in lista] #Se crea una lista que haga todo el contenido de la otra lista a entero.
            st.write(f"El resultado de la suma es: {funcion.sumar_lista(lista_enteros)}") #Se envía la lista como argumento.
    except ValueError:
        st.error("Hubo un error de sintaxis")
```
En este case se pide que el usuario en un bloque de texto ingrese la lista con los valores que quiere separados por comas para que, una vez los haya ingresado, se cree una lista separando los valores del string con las comas usando .split(). Una vez realizado esto, creamos una lista de enteros en la que convertiremos todos los valores de la lista pasada (los cuales son string) en enteros utilizando compresión y, para finalizar, se manda esta lista como argumento de nuestra función. El except entra en acción cuando el usuario ingresa los números separados por cualquier cosa menos comas.

```python
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
```
En este case se le pide al usuario que ingrese el nombre del producto y, con ayuda de una lista y una selectbox() se le pide que indique si quiere utilzar valores predeterminados o no. En caso de que si quiera, solo se enviará como argumento el nombre pero si no quiere entonces pediremos que ingrese la cantidad de productos y el precio por unidad para mandarlos también como argumentos.

```python
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
```
En este case se le pide al usuario que ingrese la lista separada por comas para nosotros utilizar el metodo split() y hacer una lista de subcadenas. Estas subcadenas de números van a ser convertidas a enteros con la compresión y asignadas a una nueva variable llamada lista_enteros para ser enviada como argumento en nuestra función. El except entra en acción cuando el usuario separa los datos con todo menos comas.

```python
case "Multiplicación con *args":
    argumento_variadico = st.text_input("Ingresa el argumento para la función (separado por comas): ")
    if argumento_variadico:
        argumento_variadico = argumento_variadico.split(",") #Se separa el contenido de la string por comas, creando una lista.
        argumento_enteros = [int(val) for val in argumento_variadico] #Se hacen enteros los elementos de la lista.
        st.write(f"El producto de todos los números es: {funcion.multiplicar_todos(*argumento_enteros)}")
    else:
        st.write(f"El producto de todos los números es: 1")
```
En esta función se pide que se ingresen los valores enteros como una string para nosotros poder usar el metodo split() para separar nuestra cadena en subcadenas con las comas y, con la compresión de listas, hacer los valores enteros añadiendolos a una lista nueva. Esta nueva lista se pasa como argumento a nuestra función pero descomprimida (ya que es una lista).

```python
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
```
En este case se le pide al usuario que ingrese una cantidad de datos n a leer y, dependiendo la cantidad seleccionada, se abriran n pares de cajas de texto para que el usuario ingrese las clave-valor que desea para que estos sean agregados a un diccionario inicializado anteriormente. Una vez haya ingresado todos los que quiere, puede presionar el botón para imprimir los valores y, al presionarlo, se pasa el diccionario descompactado como argumento a nuestra función.

```python
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
```
En este case se pide que se ingrese el número 1 y el número 2 para despues, con una selectbox, preguntar al usuario si quiere trabajr con la operación por defecto (suma) o quiere una personalizada. Si ingresa que quiere trabajar con la predeterminada entonces se mandan como argumentos a la función solo los números ya que se toma como predeterminada la suma pero, si elegimos personalizado, entonces nos pedirá que ingresemos que operación queremos trabajar para tambien mandarla como argumento.
