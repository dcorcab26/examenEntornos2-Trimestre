tareas=[{"titulo":"Estudiar python", "hecha": False},{"titulo":"Hacer ejercicio", "hecha": True},{"titulo":"Leer 10 páginas", "hecha": False}]

def agregar_tareas(tareas, titulo):
    nuevo_titulo = ""
    tarea_nueva={"titulo": nuevo_titulo, "hecha": False}

    tareas += [tarea_nueva]
    return tareas


def marcar_hecha(tareas, titulo):
    buscador= ""
    tareas["titulo"] = buscador

    for titulo in tareas:
        if titulo == buscador:
                tareas["hecha"]=True
        else:
            print("El titulo no se ha encontrado en las tareas.")
    return tareas


