this proyect was a practice when i i'd practice the lesson around this framework
and now

the capacities:
    * creations and reading of expensives
    * addition of all the entraces at the data base

state:
    we could tell that this proyect is in process, the next step is add the frontend of the proyect

MODELS:
    using the conection with mysql and ORM native from Django the models are the next
    *users:
            -Perfiles:
                    have a one to one relation with the model User from python

            here have a signal, when a user is created at the view in the same time is creted a profile

    *gasto:
            -Gasto:
                    user: that is specified like a foreing key with the user
                    nombre: is type char and have a max length of 50
                    categoria
                    importe: type integer and is refence to the price of this gasto
                    fecha: the gasto's date
                    descripcio

                    this model have a str method that call the name of themself

for the views, i'd did the better to make the easiest code, the documentacion i'll add letter
