# importem les llibreries necessàries
import unittest
import pandas as pd
import numpy as np

# importem les nostres funcions de utils
from utils import (
    descomprimir,
    marging,
    summary,
    get_column_pandas,
    get_column_readline,
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
)

# creem la classe TestDataExpl per fer els unittest
class TestDataExpl(unittest.TestCase):

    # comprovem que el retorn de marging és pandas dataframe
    def test_marging(self):
        self.assertIsInstance(
            marging(
                "data/tracks_norm.csv", "data/albums_norm.csv", "data/artists_norm.csv"
            ),
            pd.DataFrame,
        )

    # comprovem que la resposta de la funció summary és correcta
    def test_summary(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        rows, columns, nulls = summary(df, "artist_id", "popularity_track")
        self.assertEqual(rows, "Hi ha 35574 tracks")
        self.assertEqual(columns, "32 columnes")
        self.assertEqual(
            nulls, "A la columna popularity_track hi ha 0 tracks sense valor"
        )

    # comprovem que la resposta de la funció get_column_pandas siga correcta
    def test_pandas(self):
        self.assertEqual(get_column_pandas("data/tracks_norm.csv", "track_id"), 35574)
        self.assertEqual(get_column_pandas("data/tracks_norm.csv", "name"), 35574)

    # comprovem que la resposta de la funció get_column_readline siga correcta
    def test_with_open(self):
        self.assertEqual(get_column_readline("data/tracks_norm.csv", "track_id"), 35574)
        self.assertEqual(get_column_readline("data/tracks_norm.csv", "name"), 35574)

    # comprovem que la resposta de la funció artist_track_counter siga correcta
    def test_artist_track_counter(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        self.assertEqual(
            artist_track_counter(df, "Radiohead"), "L'artista Radiohead té 159 cançons"
        )

    # comprovem que la resposta de la funció feature_stats siga correcta
    def test_feature_stats(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        self.assertEqual(
            feature_stats(df, "Metallica", "energy"),
            "El màxim és 0.998, la mitjana és 0.8462655384615385 i el mínim és 0.0533. Artista: Metallica",
        )

    # comprovem que la resposta de la funció extract_feature retorne una columna de pandas
    def test_extract_feature(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        self.assertIsInstance(
            extract_feature(df, "Ed Sheeran", "acousticness"), pd.core.series.Series
        )

    # comprovem que la resposta de la funció features_by_artist retorne una llista
    def test_features_by_artist(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        self.assertIsInstance(
            features_by_artist(df, ["Adele", "Extremoduro"], "energy"), list
        )

    # comprovem que la resposta de la funció features_mean_by_artists retorne una llista
    def test_features_mean_by_artists(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        self.assertIsInstance(
            features_mean_by_artists(
                df,
                ["Metallica", "Extremoduro", "AC/DC", "Hans Zimmer"],
                [
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
                ],
            ),
            list,
        )

    # comprovem que la resposta de la funció eucladian retorne una matriu
    def test_eucladian(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        list_artists = features_mean_by_artists(
            df,
            ["Metallica", "Extremoduro", "AC/DC", "Hans Zimmer"],
            [
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
            ],
        )
        self.assertIsInstance(eucladian(list_artists), np.ndarray)

    # comprovem que la resposta de la funció cosinus retorne una matriu
    def test_cosinus(self):
        df = pd.read_csv("data/trackfinals.csv", sep=";")
        list_artists = features_mean_by_artists(
            df,
            ["Metallica", "Extremoduro", "AC/DC", "Hans Zimmer"],
            [
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
            ],
        )
        self.assertIsInstance(cosinus(list_artists), np.ndarray)


if __name__ == "__main__":
    # fem funcionar el nostre unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataExpl)
    unittest.TextTestRunner(verbosity=2).run(suite)
