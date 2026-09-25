preguntas = [
    {
        "nivel": "Facil",
        "pregunta": "¿Qué gas absorben las plantas durante la fotosíntesis?",
        "opciones": {"A": "Oxígeno", "B": "Dióxido de carbono", "C": "Nitrógeno", "D": "Hidrógeno"},
        "correcta": "B"
    },
    {
        "nivel": "Facil",
        "pregunta": "¿Cuál es la capital de Colombia?",
        "opciones": {"A": "Cali", "B": "Medellín", "C": "Bogotá", "D": "Cartagena"},
        "correcta": "C"
    },
    {
        "nivel": "Facil",
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": {"A": "Venus", "B": "Marte", "C": "Mercurio", "D": "Tierra"},
        "correcta": "C"
    },
    {
        "nivel": "Medio",
        "pregunta": "¿Cuál es el país más pequeño del mundo?",
        "opciones": {"A": "Mónaco", "B": "Luxemburgo", "C": "Malta", "D": "Ciudad del Vaticano"},
        "correcta": "D"
    },
    {
        "nivel": "Medio",
        "pregunta": "¿Cuál es el mamífero que posee la lengua mas larga en relacion con el tammaño de su cuerpo?",
        "opciones": {"A": "Elefante", "B": "Jirafa", "C": "Murciélago", "D": "Oso hormiguero"},
        "correcta": "C"
    },
    {
        "nivel": "Medio",
        "pregunta": "¿Cuál es el tratado que puso fin oficial a la Primera Guerra Mundial en 1919?",
        "opciones": {"A": "Tratado de Utrecht", "B": "Tratado de Versalles", "C": "Tratado de Tordesillas", "D": "Paz de Westfalia"},
        "correcta": "B"
    },
    {
        "nivel": "Medio",
        "pregunta": "¿Quién fue el primer ser humano en viajar al espacio?",
        "opciones": {"A": "Neil Armstrong", "B": "Yuri Gagarin", "C": "John Glenn", "D": "Buzz Aldrin"},
        "correcta": "B"
    },
    {
        "nivel": "Dificil",
        "pregunta": "¿Qué estrecho marino separa a la península ibérica del continente africano?",
        "opciones": {"A": "Estrecho de Gibraltar", "B": "Estrecho del Bósforo", "C": "Estrecho de Ormuz", "D": "Estrecho de Magallanes"},
        "correcta": "A"
    },
    {
        "nivel": "Dificil",
        "pregunta": "¿En qué continente se encuentra el desierto del Kalahari?",
        "opciones": {"A": "Asia", "B": "África", "C": "Oceanía", "D": "América"},
        "correcta": "B"
    },
    {
        "nivel": "Dificil",
        "pregunta": "¿Cuál científico recibió dos premios Nobel en diferentes disciplinas científicas?",
        "opciones": {"A": "Albert Einstein", "B": "Niels Bohr", "C": "Marie Curie", "D": "Max Planck"},
        "correcta": "C"
    }
]

respaldo = {
    "Facil": {
        "nivel": "Facil (Respaldo)",
        "pregunta": "¿Cuál es el planeta conocido como el planeta rojo?",
        "opciones": {"A": "Venus", "B": "Marte", "C": "Júpiter", "D": "Saturno"},
        "correcta": "B"
    },
    "Medio": {
        "nivel": "Medio (Respaldo)",
        "pregunta": "¿Cuál es el país más grande de África por superficie territorial?",
        "opciones": {"A": "Nigeria", "B": "Sudáfrica", "C": "Argelia", "D": "Egipto"},
        "correcta": "C"
    },
    "Dificil": {
        "nivel": "Dificil (Respaldo)",
        "pregunta": "¿Cuál es la única ave conocida que tiene la capacidad biológica demostrada de volar hacia atrás?",
        "opciones": {"A": "Vencejo común", "B": "Colibrí", "C": "Martín pescador", "D": "Pájaro carpintero"},
        "correcta": "B"
    }
}
ayudas = {
    "1": "50/50",
    "2": "Llamar a un amigo",
    "3": "Cambiar la pregunta"
}

premios = [
    100000, 200000, 300000, 500000, 1000000,
    2000000, 5000000, 10000000, 20000000, 50000000
]
def usar_5050(opciones, correcta):
    eliminadas = 0
    for letra in ("A", "B", "C", "D"):
        if letra in opciones and letra != correcta:
            del opciones[letra]
            eliminadas += 1
            if eliminadas == 2:
                break
                
    print("\n[50/50]: Se quitaron dos respuestas erróneas.")
    
def usar_amigo(correcta):
    print(f"\n[AMIGO]: 'Creo que la respuesta correcta es la {correcta}'.")
    
def usar_cambio(actual):
    nivel = actual["nivel"]
    if nivel in respaldo:
        nueva = respaldo.pop(nivel)
        print(f"\n[CAMBIO]: Se cambió la pregunta por una de nivel {nivel}.")
        return nueva
    print("\nYa no hay preguntas de respaldo para este nivel.")
    return actual

dinero = 0
numeroPregunta = 1
    
for actual in preguntas:
    opcionesActuales = actual["opciones"].copy()
    while True:
        print("=" * 50)
        print(f"| Pregunta {numeroPregunta}/10 ({actual['nivel']}) | Acumulado: ${dinero:,}          |")
        print("=" * 50)
        print(actual["pregunta"] + "\n")
        
        for letra in ("A", "B", "C", "D"):
            if letra in opcionesActuales:
                print(f" {letra}. {opcionesActuales[letra]}")
                
        if ayudas:
            print("\nRecuerde que tiene ayudas: ")
            for clave, valor in ayudas.items():
                print(f" {clave}. {valor}")
                
        respuesta = input("\nIndique su respuesta o comodín: ").upper()
        
        if respuesta in ayudas:
            if respuesta == "1":
                usar_5050(opcionesActuales, actual["correcta"])
                del ayudas["1"]
            elif respuesta == "2":
                usar_amigo(actual["correcta"])
                del ayudas["2"]
            elif respuesta == "3":
                nueva = usar_cambio(actual)
                if nueva != actual:
                    actual = nueva
                    #opcionesActuales = actual["opciones"].copy()
                    del ayudas["3"]
            continue
        if respuesta in ("A", "B", "C", "D"):
            if respuesta == actual["correcta"]:
                dinero = premios[numeroPregunta - 1]
                print(f"\nCorrecto!! Ha ganado ${dinero:,}")
                numeroPregunta += 1
                break
            else:
                textoCorrecto = actual["opciones"][actual["correcta"]]
                print(f"\nIncorrecto. La respuesta correcta era {actual['correcta']}: {textoCorrecto}")
                print(f"Gracias por jugar. Te retiras con: ${dinero:,}")
                exit()
        else:
            print("\nOpción no válida \nIngrese A - B - C - D o el número disponible de la ayuda.")
            
print("*"* 50)
print(f"FELICITACIONES! ERES MILLONARIO: ${dinero:,}")
print("*"* 50)