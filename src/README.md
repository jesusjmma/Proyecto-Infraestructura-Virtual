# Representación de modelo
En este documento se refleja la representación del modelo implementada, así como su justificación.

### Análisis del dominio

Lo primero que requería tras concretar el lenguaje de programación, fue considerar las clases que contrendrán unidad mínima de información, por lo que analizando las Historias de Usuario, consideré que se debían definir las clases **usuario** y **deuda**, que serían objetos valor pues únicamente contendrían datos.

Para modelar correctamente el objeto valor **deuda**, se creó un *issue* atendiendo a la historia de usuario correspondiente, para solucionar ciertos aspectos con la gestión individualizada de las deudas y un único usuario (ejemplo: filtrado por concepto, control personal de deudas...).

Después, se plantea un *issue* acerca de la relación que tendrían estas clases y de cómo se debería abordar correctamente. La solución que acabé planteando era una entidad denominada **gastoCompartido**, en la que se contempla una serie de usuarios participantes de ese gasto, y una serie de gastos individuales realizados por un subconjunto de participantes, con la idea de analizar dichos datos y extraer las deudas generadas entre todos los usuarios.

Paralelamente al desarrollo de la entidad anterior, se optó por descomponer el objeto valor **usuario** en una entidad, y un objeto valor, denominados **usuario** e **infoUsuario**, con la idea de poder mantener un registro individualizado de las deudas dentro del ámbito de un usuario, y además asignar la información de los usuarios implicados en la deuda, con los datos únicamente importantes (nick, nombre y apellidos). También, se vio necesario definir un objeto valor **gasto** para el ámbito de la entidad *gastoCompartido*, totalmente diferente de una **deuda**, pues en un gasto sólo participa un único usuario.

### Desglose y descripción de clases

***Objetos Valor***: Todas las clases en esta lista se consideran objetos valor porque su única función es el almacenamiento de datos.

* *infoUsuario*: Objeto valor que representa la información identificativa de un usuario de la aplicación. Un  usuario se distingue de otro a través de un nickname.
* *deuda*: Objeto valor que representa la información de la deuda de un usuario frente a otro.
* *gasto*: Objeto valor que representa el gasto realizado por un único usuario, identificado dentro de un contexto en el que participan varios usuarios.

***Entidades***: Todas las clases en esta lista se consideran entidades porque los algoritmos de la lógica de negocio las utilizarán para generar los datos de interés.

* *usuario*: Entidad que representa a un usuario de la aplicación. Se identifica con la información del usuario, y una lista de deudas pendientes de pagar.
* *gastoCompartido*: Entidad que representa un gasto común entre una serie de usuarios participantes. Los usuarios realizan gastos individuales dentro de este contexto, y tras el análisis del algoritmo, se generan las deudas entre los mismos.
