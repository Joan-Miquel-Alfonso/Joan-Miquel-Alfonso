import matplotlib.pyplot as plt
import seaborn as sns


def scatter(dicti1, dicti2, x="Nombre de línies", y="Temps d'execucció en ms"):
    """funció que ens fa una gràfica de punts.

    Arguments:
        dict1: diccionari amb temps d'execucció.
        dict2: diccionari amb temps d'execucció.
        x (opcional): nom eix x
        y (opcional): nom eix y

    Returns:
        Gràfica de punts.
    """
    # creem la figura
    plt.figure()
    # fem un bucle agafant els dos diccionaris,
    # i creem el nostre scatter on l'eix x són les claus
    # i les y són els valors del diccionari
    for k in [dicti1, dicti2]:
        plt.scatter(k.keys(), k.values())
    # posem la llegenda
    plt.legend(["get_column_readline", "get_column_pandas"])
    # Nombrem l'eix x
    plt.xlabel(x)
    # Nombrem l'eix y
    plt.ylabel(y)
    # Mostrem la gràfica
    plt.show()


def plot_maker(dictionary, x, y):
    """funció que ens fa un gràfic de barres.

    Arguments:
        dictionary: diccionari (en aquest cas amb una feature per àlbum).
        x: nom eix x
        y: nom eix y

    Returns:
        Gràfica de barres.
    """
    # ceem la nostra figura
    plt.figure()
    # Creem un gràfic de barres amb les claus del diccionari com a eix X
    # i els values com a eix y
    plt.bar(dictionary.keys(), dictionary.values())
    # rotem les etiquetes de l'eix de les x per a què siguen llegibles
    plt.xticks(rotation=90)
    # Nombrem l'eix x
    plt.xlabel(x)
    # Nombrem l'eix y
    plt.ylabel(y)
    # Mostrem la gràfica
    plt.show()


def hist_maker(information, artists, x, y):
    """funció que ens fa un histograma de densitat.

    Arguments:
        information: columna del dataframe amb dades d'una feature .
        artists (llista): artistes que hem extret les dades.
        x (opcional): nom eix x
        y (opcional): nom eix y

    Returns:
        Histograma de densitat.
    """
    # Creem la nostra figura
    fig, ax = plt.subplots()
    # fem un bucle en k és la informació i v
    # són els artistes, ho fem com a zip per a
    # què vagen emparellats.
    # Després posem density = True per a que la
    # gràfica siga donada per la densitat.
    # posem alpha per a que aquestes es superposen
    # en cas de tenir més d'un artista.
    for k, v in zip(information, artists):
        k.hist(alpha=0.3, ax=ax, density=True, label=v)
    # mostrem la llegenda
    ax.legend()
    # rotem l'etiqueta de l'eix de les x
    plt.xticks(rotation=90)
    # Nombrem l'eix x
    plt.xlabel(x)
    # Nombrem l'eix y
    plt.ylabel(y)
    # Mostrem la gràfica
    plt.show()


def heat_map(matrix, artists):
    """funció que ens fa un heatmap.

    Arguments:
        matrix: matriu amb les similituds per artista .
        artists (llista): artistes que hem extret les dades.

    Returns:
        Heatmap
    """
    # Creem amb seaborn el heatmap, on la intensitat del color
    # ve donada pels nombres de la matriu, les etiquetes dels
    # eixos venen donades pels artistes
    ax = sns.heatmap(matrix, xticklabels=artists, yticklabels=artists)
    # mostrem la gràfica
    plt.show()
