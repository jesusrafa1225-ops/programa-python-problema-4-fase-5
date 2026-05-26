#  NOMBRE : JESUS RAFAEL PADILLA NAVARRO
#  PROGRAMA: INGERNIERIA DE SISTEMAS
#  GRUPO: 213022A_2201
#  PROBLEMA: #4 FASE 5
# CODIGO FUENTE: AUTORIA PROPIA


"""Cada fila tiene el formato:[titulo,año,calificacion,genero]."""


def videoteca_digital():
    videoteca = [
                ["El Codigo Da Vinci",2006,6.6,"Thriller"],
                ["La huerfana 1",2009,7,"Terror"],
                ["Chiquito pero peligroso",2006,4.5,"Comedia"],
                ["Matilda",1996,7,"Familiar"],
                ["Charlie y la fabrica de chocolate",2005,6.6,"Fantasia"],
                ["El cadaver de la novia",2005,7.3,"Fantasia"],
                ["El extraño mundo de Jack",1993,8,"Fantasia"],
                 ]
    

    peliculas = 0


    # Recorre cada película y verifica si cumple:
    # - Calificación >= 6.6
    # - Año >= 2005

    for pelicula in videoteca:
        if pelicula[2] >= 6.6 and pelicula[1] >= 2005:
           peliculas += 1

    return peliculas


resultado = videoteca_digital()
print("El numero de peliculas que cumplen con los criterios de calificacion y año es:", resultado)