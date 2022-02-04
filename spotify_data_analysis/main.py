# importem de utils i plots totes les funcions necessàries
from utils import (
    descomprimir,
    marging,
    summary,
    get_column_pandas,
    get_column_readline,
    time_,
    artist_track_counter,
    word_in_track,
    decade_searcher,
    popularity_last_years,
    track,
    feature_stats,
    feature_by_album,
    extract_feature,
    features_by_artist,
    features_mean_by_artists,
    eucladian,
    cosinus,
    api_to_csv,
    api,
    multithreads,
)

from plots import scatter, plot_maker, hist_maker, heat_map

# creem una funció que conté totes les funcions de utils i plolts
def main(zip):
    """Exercici 1"""
    print("EXERCICI 1")
    # assignem data a directory per descomprimir
    # el zip en aquest directori
    directory = "data"
    # cridem la funció descomprimir
    descomprimir(zip, directory)
    # assignem els tres arxius csv
    file1 = "data/tracks_norm.csv"
    file2 = "data/albums_norm.csv"
    file3 = "data/artists_norm.csv"
    # assignem a df el resultat de la funció
    df = marging(file1, file2, file3)
    # assignem df a la variable dataframe
    dataframe = df
    # assignem les variables arg1 i arg2
    arg1 = "artist_id"
    arg2 = "popularity_track"
    # mostrem per pantalla els resultats de la funció summary
    print(summary(dataframe, arg1, arg2))
    """Exercici 2"""
    # fem un diccionari amb el csv i la columna que volem
    dicc = {
        "data/tracks_norm.csv": "track_id",
        "data/artists_norm.csv": "artist_id",
        "data/albums_norm.csv": "album_id",
    }
    # fem una variable i executem la funció time per a cadascuna del lectors
    ex_time_readline = time_(dicc, get_column_readline)
    ex_time_pandas = time_(dicc, get_column_pandas)
    # cridem la funció scatter per fer el gràfic
    scatter(ex_time_readline, ex_time_pandas)
    """Exercici 3"""
    print("EXERCICI 3")
    # seleccionem l'artista
    artist = "Radiohead"
    # mostrem per pantalla la funció
    print(artist_track_counter(dataframe, artist))
    # seleccionem la paraula
    word = "police"
    # mostrem per pantalla la funció
    print(word_in_track(dataframe, word))
    # seleccionem la dècada
    decade = 1990
    # mostrem per pantalla la funció
    print(decade_searcher(dataframe, decade))
    # seleccionem els 10 últims anys
    last_n_years = 10
    # mostrem per pantalla la funció
    print(popularity_last_years(dataframe, last_n_years))
    # seleccionem la dècada
    decade = 1960
    # mostrem per pantalla la funció
    print(track(dataframe, decade))
    """Exercici 4"""
    print("EXERCICI 4")
    # seleccionem l'artista i la feature
    artist = "Metallica"
    feature = "energy"
    # mostrem per pantalla la funció
    print(feature_stats(dataframe, artist, feature))
    # seleccionem l'artista i la feature
    artist = "Coldplay"
    feature = "danceability"
    # creem la variable diccionari executant la funció
    dictionary = feature_by_album(dataframe, artist, feature)
    # posem nom a l'eix x i y de la gràfica
    x = "Àlbum"
    y = "Danceability"
    # cridem la funció per fer la gràfica
    plot_maker(dictionary, x, y)
    """Exercici 5"""
    # seleccionem artista i feature
    artist = "Ed Sheeran"
    feature = "acousticness"
    # extraem la informació (ha de ser en format llista)
    information = [extract_feature(dataframe, artist, feature)]
    # assignem l'artista (ha de ser en format llista)
    artists = ["Ed Sheeran"]
    # posem nom a l'eix x i y de la gràfica
    x = "Acousticness"
    y = "density"
    # cridem la funció per fer la gràfica
    hist_maker(information, artists, x, y)
    """Exercici 6"""
    # seleccionem artistes i la feature
    artists = ["Adele", "Extremoduro"]
    feature = "energy"
    # extraem la informació amb la funció
    information = features_by_artist(dataframe, artists, feature)
    # posen nom a l'eix x
    x = "Energy"
    # cridem la funció per fer la gràfica
    hist_maker(information, artists, x, y)
    """Exercici 7"""
    # seleccionem artistes i les 12 features
    artists = ["Metallica", "Extremoduro", "Ac/Dc", "Hans Zimmer"]
    features = [
        "danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "time_signature",
    ]
    # assignem a arrays el vector de 12 dimensions de cada artista
    arrays = features_mean_by_artists(dataframe, artists, features)
    # assignem a matrix la matriu amb la similitud eucladiana
    matrix = eucladian(arrays)
    # cridem la funció per fer la gràfica
    heat_map(matrix, artists)
    # assignem a matrix la matriu amb la similitud cosinus
    matrix = cosinus(arrays)
    # cridem la funció per fer la gràfica
    heat_map(matrix, artists)
    print("EXERCICI 8")
    # nomenem els artistes
    artists = ["Radiohead", "David_Bowie", "Måneskin"]
    # cridem la funció
    api_to_csv(artists)
    # agafem tots els artistes del dataframe i els passem a una llista sense repeticions
    artists = df["name_artist"].unique().tolist()
    # executem la funció
    multithreads(artists, 4)


# protegim el codi amb aquest condicional
if __name__ == "__main__":
    # assignem a zip l'arxiu que volem descomprimir
    zip = "data/data.zip"
    # executem la nostra funció main
    main(zip)
