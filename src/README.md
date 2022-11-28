# Representación de modelo
### Análisis del dominio

He seguido principalmente la historia de usuario [HU3](https://github.com/jesusjmma/Proyecto-Infraestructura-Virtual/issues/4), y su respectivo user-journey para la representación del modelo. En ella se comenta los problemas que tiene Jose Antonio para poder identificar los gastos compartidos que tiene para poder saber qué cantidad debe pagar a sus amigos y con qué motivo.

Para ello, primero se ha definido el *issue* [#11](#11) en el que se abordan los problemas con los gastos, que son:

1. *Identificar quién ha pagado el gasto*: Se menciona que un gasto compartido es definido por una persona.
2. *Identificar quiénes son las personas participantes:* Se menciona que un gasto puede aplicar a varias personas.
3. *Clarificar el motivo del gasto:* Jose Antonio especifica que quiere conocer los conceptos por los que debe dinero a una persona.

Después, se ha definido el *issue* [#13](#13) en el que se abordan los problemas con las personas implicadas en un gasto, que son:

1. *Identificar claramente a la persona*: Se necesita para saber qué rol tiene qué determinada persona (si inicia el gasto, si participa, o ambas).
2. *Asignar los gastos que debe pagar el usuario*: José Antonio necesita saber a quien tiene que pagar y qué cantidad.



### Desglose y descripción de clases

***Objetos Valor***: Todas las clases en esta lista se consideran objetos valor porque su única función es el almacenamiento de datos.

* **gasto**: Resuelve el problema del primer issue con un objeto valor, ya que simplemente se necesita de una estructura que contenga datos. Se representa con los siguientes atributos:
  - *nickPagador*: Identificación de la persona que define el gasto.
  - *concepto*: Descripción del gasto.
  - *importe*: Cantidad a pagar.
  - *nicksParticipantes*: Identificación de las personas participantes en dicho gasto.

***Entidades***: Todas las clases en esta lista se consideran entidades porque los algoritmos de la lógica de negocio las utilizarán para generar los datos de interés.

* **usuario**: Resuelve el problema del segundo issue con una entidad, ya que una persona puede tener una cantidad variable de gastos pendientes de pagar, que crecerá o disminuirá en función de si efectivamente los paga o no. Se representa con los siguientes atributos:
  * *nickname* : Identificador único del usuario.
  * *gastos*: Listado de gastos en los que el usuario participa y debe pagar.
