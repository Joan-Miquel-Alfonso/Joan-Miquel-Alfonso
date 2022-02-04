import zipfile as zf
import pandas as pd
import time
import re
import math
import numpy as np
import csv
import requests
import concurrent.futures


def descomprimir(zipfile, directory):
    """funció que descomprimexi un arxiu zip

    Arguments:
        zipfile: Fitxer que volem descomprimir.
        directory: carpeta on volem que es descomprmeixen els arxius.

    Returns:
        ----------
    """
    with zf.ZipFile(zipfile, "r") as zip_f:
        # Descomprimim tot el contingut del zip
        zip_f.extractall(directory)


def marging(file1, file2, file3):
    """funció que junta tres arxius csv en un sol. 
        A més posa majúscules a la primera lletra de la columna
        name_artist i replena valors buits de la columna popularity
        per la mitjana de la columna

    Arguments:
        file1: Fitxer que volem juntar.
        file2: Fitxer que volem juntar.
        file3: Fitxer que volem juntar.

    Returns:
        Retorna el dataset ja juntat i modificat.
    """
    # creem la variable global df
    global df
    # creem una variable per a cadascun dels
    # csv llegits
    data1 = pd.read_csv(file1, sep=";")
    data2 = pd.read_csv(file2, sep=";")
    data3 = pd.read_csv(file3, sep=";")

    # fem el primer merge que ho farem de la columna artist_id
    # emprem outer per unir totes les files estiguen en els dos
    # csv o no
    output1 = pd.merge(data1, data3, on="artist_id", how="outer")
    # fem el segon merge que és el primer merge més el segon arxiu
    # ho fem amb la columna album_id perquè volem que cada cançó
    # tinga informació sobre
    output2 = pd.merge(output1, data2, on="album_id", how="outer")
    # eliminem la columna artist_id_y ja que aquesta està duplicada
    df = output2.drop(columns=["artist_id_y"])
    # la columna artist_id_x la renombrem com artist_id
    df.rename({"artist_id_x": "artist_id"}, axis=1, inplace=True)
    # creem la variable a que té el nombre de cada columna
    a = df.columns
    # creem un diccionari
    dictionary = {}
    # fem un bucle de la variable a
    for x in a:
        # si una columna acaba en x, ho supstituïm per track
        # ja que correspon al csv de tracks
        if x[-1] == "x":
            dictionary[x] = x[0 : (len(x) - 1)] + "track"
        elif x[-2:] == "_y":
            dictionary[x] = x[0 : (len(x) - 1)] + "artist"
    # substituim les columnes per els nou noms
    for k, v in dictionary.items():
        df.rename({k: v}, axis=1, inplace=True)
    # posem majúscules a la primera lletra de totes les paraules
    # de la columna name_artist
    df.name_artist = df.name_artist.str.title()
    # replenem les columnes de popularity_track sense valor per la mitjana de tots els valors.
    df["popularity_track"].fillna(value=df["popularity_track"].mean(), inplace=True)
    # guardem el nou csv com a trackfinals.csv
    df.to_csv("data/trackfinals.csv", sep=";", index=False)
    # retornem el dataframe
    return df


def summary(dataframe, arg1, arg2):
    """funció que ens diu quantes cançons té el Dataframe
        en una columna concreta, quantes columnes i quants
        valors nuls hi ha a la columna seleccionada.

    Arguments:
        dataframe: Dataframe que volem emprar.
        arg1: Columna que volem seleccionar.
        arg2: Columna que volem seleccionar.

    Returns:
        Nombre de cançons, columnes i valors nuls.
    """
    # contem el nombre de línies d'una columna en concret
    # ens valen per a totes
    rows = "Hi ha {} tracks".format(dataframe[arg1].count())
    # agafem totes les columnes i les comptem
    columns = "{} columnes".format(len(dataframe.columns))
    # mirem quantes valors buits té una columna en concret
    nulls = "A la columna {} hi ha {} tracks sense valor".format(
        arg2, dataframe[arg2].isnull().sum()
    )
    return rows, columns, nulls


def get_column_pandas(file, column):
    """Lector d'arxius csv utilitzant pandas.

    Arguments:
        file: Arxiu que volem llegir.
        column: Columna que volem seleccionar.

    Returns:
        Nombre de línies de l'arxiu.
    """
    # llegim l'arxiu amb pd.read_csv
    df = pd.read_csv(file, sep=";")
    # seleccionem una columna
    a = df[column]
    # comptem el nombre de línies
    count = a.count()
    # retornem el nombre de línies
    return count


def get_column_readline(file, column):
    """Lector d'arxius csv.

    Arguments:
        file: Arxiu que volem llegir.
        column: Columna que volem seleccionar.

    Returns:
        Nombre de línies de l'arxiu.
    """
    # creem una llista buida
    lista = []
    # creem la variable count
    count = 0
    # Obrim amb with l'arxiu
    with open(file) as f:
        # llegim la primera línia de l'arxiu
        headers = f.readline()
        # dividim per columnes
        header = headers.split(";")
        # fem un bucle pel nombre de columnes
        for x in range(len(header)):
            # si coincideix amb el nom de la columna
            # donada a l'argument guardem la posició de la columna
            if header[x] == column:
                clau = x
        # llegim la resta de les línies
        data = f.readlines()
        # fem un bucle per llegir línia per línia
        for line in data:
            # seleccionem la columna que volem
            c = line.split(";")[clau]
            # l'afegim a la llista
            lista.append(c)
            # sumem un a la variable count
            count += 1
        # retornem el nombre de línies
        return count


def time_(dicc, function):
    """Retorna temps d'execucció d'una funció.

    Arguments:
        dicc (diccionari): diccionari amb l'arxiu i columna que volem llegir.
        function: funció que volem executar.

    Returns:
        diccionari amb el nombre de línies de l'arxiu llegit i el temps d'execucció.
    """
    # creem un diccionari
    ex_time = {}
    # fem un bucle del diccionari de l'argument
    for k, v in dicc.items():
        # iniciem el temps
        start = time.time()
        # Executem la funció
        count = function(k, v)
        # guradem el temps d'execució en un diccionari
        ex_time[count] = time.time() - start
    # Retornem el diccionari
    return ex_time


def artist_track_counter(dataframe, artist):
    """funció que ens conta les cançons que té un artista en concret.

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist: artista que volem analitzar.

    Returns:
        Nombre de cançons de l'artista seleccionat.
    """
    # comptem el nombre de cançons de l'artista en concret
    count = dataframe[dataframe.name_artist == artist].count()
    string = "L'artista {} té {} cançons".format(artist, count["name_track"])
    return string


def word_in_track(dataframe, word):
    """funció que ens conta les cançons que tenen una paraula en concret.

    Arguments:
        dataframe: Dataframe que volem emprar.
        word: paraula que volem veure si està.

    Returns:
        Nombre de cançons amb una paraula en concret.
    """
    # seleccionem la columna name_track
    track = dataframe["name_track"]
    # busquem i posem en la llista les paraules que tinguen la paraula
    # en concret, amb re.ignorecase ignorem que estiga en majúscula o
    # minúscula
    searcher = [x for x in track if re.search(word, x, re.IGNORECASE)]
    string = "El nombre de cançons amb la paraula {} és de {}".format(
        word, len(searcher)
    )
    return string


def decade_searcher(dataframe, decade):
    """funció que ens diu quantes cançons hi ha publicades en una decada en concret.

    Arguments:
        dataframe: Dataframe que volem emprar.
        decade: dècada que volem seleccionara, haurà de ser en format yyyy.

    Returns:
        Nombre de cançons d'una dècada en concret.
    """
    # comptem el nombre de cançons publicades en una dècada en concret
    count = dataframe[
        (dataframe.release_year >= decade) & (dataframe.release_year < decade + 10)
    ].count()
    string = "Hi ha {} cançons publicades a la dècada de {}".format(
        count["name_track"], decade
    )
    return string


def popularity_last_years(dataframe, last_n_years):
    """funció que ens diu la cançó més popular publicada en x anys anteriors fins ara.

    Arguments:
        dataframe: Dataframe que volem emprar.
        last_n_years: des de quins últims anys volem seleccionar les cançons a analitzar.

    Returns:
        Cançó més popular.
    """
    # seleccionem les cançons publicades des del 2022 fins a que diga la variable
    release = dataframe[(dataframe.release_year >= 2022 - last_n_years)]
    # Agafem quin és el màxim en la columna popularitat
    max_popularity = release["popularity_track"].max()
    # Seleccionem la cançó amb el màxim de popularitat, es seleccionaran
    # més en cas d'empat es mostraran totes les cançons empatades
    popularity = release[release.popularity_track == max_popularity]
    string = "La cançó més popular és {} de l'artista {} amb un {} de popularitat".format(
        set(popularity["name_track"]), set(popularity["name_artist"]), max_popularity
    )
    return string


def track(dataframe, decade):
    """funció que ens diu quins artistes han aparegut des d'una època en concret
        fins ara.

    Arguments:
        dataframe: Dataframe que volem emprar.
        decade: dècada que volem seleccionara, haurà de ser en format yyyy.

    Returns:
        Artistes que tenen almenys una publicació
        en cada dècada, de la dècada seleccionada fins ara.
    """
    # creem la llista decades
    decades = []
    # fem un bucle que busque per dècades
    for x in range(decade, 2023, 10):
        # Afegim a la llista els artistses que han publicat alguna cançó
        # en la dècada en concret
        x = df[(df.release_year >= x) & (df.release_year < x + 10)]
        decades.append(set(x["name_artist"]))
    # Fem una intersecció de les llistes dins d'una llista per fer-ho emprem *map
    # Així ens mostra els artistes que estan dins de totes les llistes
    string = "Els artistes que apareixen en cada dècada des de la dècada de {} són {}".format(
        decade, set.intersection(*map(set, decades))
    )
    return string


def feature_stats(dataframe, artist, feature):
    """funció que ens diu el valor mínim, mitjana i major d'una
        feature d'un artista en concret.

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist: artista que volem analitzar.
        feature: feature que volem analitzar.

    Returns:
        Mínim, màxim i mitjana d'una feature i artista en concret.
    """
    # seleccionem l'artista
    art = dataframe[dataframe.name_artist == artist]
    # agafem el mínim, mitjana i màxim de la feature seleccionada
    minimum = art[feature].min()
    average = art[feature].mean()
    maximum = art[feature].max()
    string = "El màxim és {}, la mitjana és {} i el mínim és {}. Artista: {}".format(
        maximum, average, minimum, artist
    )
    return string


def feature_by_album(dataframe, artist, feature):
    """funció que ens diu la mitjana d'una feature de cada
        àlbum que té l'artista.

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist: artista que volem analitzar.
        feature: feature que volem analitzar.

    Returns:
        Diccionari amb la mitjana d'una feature de cada àlbum.
    """
    # seleccionem un artista en concret
    art = dataframe[dataframe.name_artist == artist]
    # fem una variable global
    global dance_dict
    # agrupem la mitjana de cada àlbum per la feature en concret
    # i la fem diccionari
    dance_dict = art.groupby("name")[feature].mean().to_dict()
    # retornem el diccionari
    return dance_dict


def extract_feature(dataframe, artist, feature):
    """funció que ens retorna la columna d'una feature i artista en concret

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist: artista que volem analitzar.
        feature: feature que volem analitzar.

    Returns:
        columna de la feature i artista seleccionats.
    """
    # seleccionem un artista en concret
    art = dataframe[dataframe.name_artist == artist]
    # fem una variable global
    global density
    # agafem la columna de la feature en concret
    density = art[feature]
    return density


def features_by_artist(dataframe, artists, feature):
    """Crea una llista d'una feature per artista

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist (llista): llista dels artistes que volem anlitzar.
        feature: feature que volem analitzar.

    Returns:
        Llista amb la feature per artista
    """
    # creem una variable global
    global list_artists
    # creem una llista buida
    list_artists = []
    # fem un bucle de la llista artists
    for k in artists:
        # seleccionem l'artista
        art = dataframe[dataframe.name_artist == k]
        # agafem la columna d'una feature en concret
        f = art[feature]
        # l'afegim a la llista
        list_artists.append(f)
    return list_artists


def features_mean_by_artists(dataframe, artists, features):
    """funció que retorna una llista de la mitjana de les features per artista

    Arguments:
        dataframe: Dataframe que volem emprar.
        artist (llista): llista dels artistes que volem anlitzar.
        feature (llista): llista de les feature que volem analitzar.

    Returns:
        Llista amb la mitjana de les features per artista.
    """
    # aquesta funció és igual que l'anterior però agafem la mitjana
    # en comptes de tota la columna
    global list_artists
    list_artists = []
    for k in artists:
        # ací està l'únic canvi
        art = dataframe[dataframe.name_artist == k].mean()
        k = art[features].values
        list_artists.append(k)
    return list_artists


def eucladian(arrays):
    """funció que ens retorna la similitud eucladiana de cada artista
        segons les seues features.

    Arguments:
        arrays: array de les features dels artistes

    Returns:
        matriu amb la similitud eucladiana.
    """
    # creem una llista buida
    f1 = []
    # fem un bucle de tantes vegades com vectors hi ha
    for z in range(len(arrays)):
        # fem altra vegada el mateix
        for l in range(len(arrays)):
            # creem una llista nova
            d = []
            # Agafem cada dimensió de cadascún de les dimensions
            # dels vectors.
            for k, v in zip(arrays[z], arrays[l]):
                # apliquem fórmula
                x = math.sqrt((k - v) ** 2)
                # afegim resultat a la llista
                d.append(x)
            # afegim resultat a la llista de la fórmula que està baix
            f1.append(1 / (1 - sum(d)))
    # la llista f1 la passem en format array
    data = np.array(f1)
    # fem una matriu quadrada de tants vectors tinguem a arrays
    matrix = np.reshape(data, (len(arrays), len(arrays)))
    return matrix


def cosinus(arrays):
    """funció que ens retorna la similitud cosenoidal de cada artista
        segons les seues features.

    Arguments:
        arrays: array de les features dels artistes

    Returns:
        matriu amb la similitud cosenoidal.
    """
    # creem una llista buida
    f1 = []
    # fem un bucle de tantes vegades com vectors hi ha
    for z in range(len(arrays)):
        # fem altra vegada el mateix
        for l in range(len(arrays)):
            # Creem tres llistes buides
            AB = []
            A = []
            B = []
            # Agafem cada dimensió de cadascún de les dimensions
            # dels vectors.
            for k, v in zip(arrays[z], arrays[l]):
                # Apliquem fórmules i les afegim a les llistes anteriors
                ab = k * v
                a = k ** 2
                b = v ** 2
                AB.append(ab)
                A.append(a)
                B.append(b)
            # Afegim a la llista f1 el resultat de la següent fórmula
            f1.append(sum(AB) / math.sqrt(sum(A) * sum(B)))
    # la llista f1 la passem en format array
    data = np.array(f1)
    # fem una matriu quadrada de tants vectors tinguem a arrays
    matrix = np.reshape(data, (len(arrays), len(arrays)))
    return matrix


def api_to_csv(artists):
    """Funció per a extreure informació d'una api i guardar-la a un arxiu csv.

    Paràmetres:
    artists (llista): llista d'artistes que volem executar

    Rerturn:
    Retorna la informació que requerim de les api i crea un arxiu csv
    """
    # creem una llista
    data = []
    # fem un bucle en els artistes
    for x in artists:
        # fem la url per al api
        url = "https://www.theaudiodb.com/api/v1/json/2/search.php?s=" + x
        # cridem al api
        response = requests.get(url)
        # fem el if, i el try per veure si hi ha error de connexió no ens done error"
        if response.status_code != 204 and response.headers[
            "content-type"
        ].strip().startswith("application/json"):
            try:
                # aconseguim l'arxiu json, s'extreu la informació necessària
                info = response.json()
                artist_name = info["artists"][0]["strArtist"]
                formed_year = info["artists"][0]["intFormedYear"]
                country = info["artists"][0]["strCountry"]
                # afegim aquesta informació a la llista
                data.append([artist_name, formed_year, country])
            except ValueError:
                print("error")

    # creem el header
    header = ["artist_name", "formed_year", "country"]
    # creem i escrivim la nostra csv
    with open("data/artists_audiodb.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # escrivim el header
        writer.writerow(header)

        # fem un bucle per escriure línia per línia les dades
        for x in data:
            writer.writerow(x)
    # llegim i mostrem per pantalla l'arxiu creat
    with open("data/artists_audiodb.csv") as f:
        for line in f:
            print(line)


def api(artists):
    """Funció per a extreure informació d'una api.

    Paràmetres:
    artists (llista): llista d'artistes que volem executar

    Rerturn:
    Retorna la informació extreta de l'api
    """
    # imprimim el header
    print(["artist_name", "formed_year", "country"])
    for x in artists:
        # fem la url per al api
        url = "https://www.theaudiodb.com/api/v1/json/2/search.php?s=" + x
        # cridem al api
        response = requests.get(url)
        # fem el if, i el try per veure si hi ha error de connexió no ens done error"
        if response.status_code != 204 and response.headers[
            "content-type"
        ].strip().startswith("application/json"):
            try:
                info = response.json()
                # fem un if per si l'arxiu json està buit
                if info == {"artists": None}:
                    print("no info", x)
                else:
                    # extreiem la infomació que volem i la mostrem per pantalla
                    artist_name = info["artists"][0]["strArtist"]
                    formed_year = info["artists"][0]["intFormedYear"]
                    country = info["artists"][0]["strCountry"]
                    print([artist_name, formed_year, country])
            except ValueError:
                # Repetim el mateix procés dues vegades ja que la connexió amb la api a vegades falla
                if response.status_code != 204 and response.headers[
                    "content-type"
                ].strip().startswith("application/json"):
                    try:
                        info = response.json()
                        if info == {"artists": None}:
                            print("no info", x)
                        else:
                            artist_name = info["artists"][0]["strArtist"]
                            formed_year = info["artists"][0]["intFormedYear"]
                            country = info["artists"][0]["strCountry"]
                            print([artist_name, formed_year, country])
                    except ValueError:
                        if response.status_code != 204 and response.headers[
                            "content-type"
                        ].strip().startswith("application/json"):
                            try:
                                info = response.json()
                                if info == {"artists": None}:
                                    print("no info", x)
                                else:
                                    artist_name = info["artists"][0]["strArtist"]
                                    formed_year = info["artists"][0]["intFormedYear"]
                                    country = info["artists"][0]["strCountry"]
                                    print([artist_name, formed_year, country])
                            except ValueError:
                                print("Not found")


def multithreads(artists, num_of_threads):
    """Funció per executar altres funcions de forma
    multithreaded.

    Paràmetres:
    artists (llista): llista d'artistes que volem executar
    num_of_process: nombre de threads que volem utilitzar.

    Rerturn:
    Retorna la informació que requerim de les api
    """
    # Obrim amb la funció per fer threads de la llibreria
    # concurrent.futures. assignem quans threads volem emprar
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
        # Creem una llista anomenada futures
        futures = []
        # executem la nostra funció
        futures.append(executor.submit(api, artists=artists))
    print(
        "Per fer més eficient la cridada de les api, emprarem un multithread ja que podem treballar en diversos cridades de api mentre esperem la resposta i així anem més ràpidament."
    )
    print(
        "Per altra banda a vegades falla la connexió per això s'ha creat el try. La funció no és 100% fiable"
    )
