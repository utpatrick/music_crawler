import os
from collections import Counter
import math
import datetime

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)


def checking_duplicate():
    kkbox_path = os.path.join('kkbox', 'data', 'results')
    mymusic_path = os.path.join('myMusic', 'data', 'results')
    spotify_path = os.path.join('spotify', 'data', 'results')
    kathy_data_path = os.path.join('data_manual_clean', 'singers_union.txt')

    singer_path = 'singers_ALL_2011-01-01_2017-12-31'
    singer_path_s = 'singers_ALL_2017-01-01_2018-03-01'

    song_path = 'songs_ALL_2011-01-01_2017-12-31'
    singer_song_pair_path = 'singer_song_pairs_ALL_2011-01-01_2017-12-31'

    with open(kathy_data_path) as data:
        cathy_singers = Counter(data.read().splitlines())
    with open(os.path.join(kkbox_path, singer_path)) as data:
        kkbox_singers = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, singer_path)) as data:
        mymusic_singers = Counter(data.read().splitlines())
    with open(os.path.join(spotify_path, singer_path_s)) as data:
        spotify_singers = Counter(data.read().splitlines())

    with open(os.path.join(kkbox_path, song_path)) as data:
        kkbox_songs = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, song_path)) as data:
        mymusic_songs = Counter(data.read().splitlines())

    with open(os.path.join(kkbox_path, singer_song_pair_path)) as data:
        kkbox_singer_song_pairs = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, singer_song_pair_path)) as data:
        mymusic_singer_song_pairs = Counter(data.read().splitlines())


    count_singers = len(list(((set(kkbox_singers) | set(spotify_singers)) & set(cathy_singers))))
    count_songs = len(list((set(kkbox_songs) & set(mymusic_songs))))
    count_singer_song_pairs = len(list((set(kkbox_singer_song_pairs) & set(mymusic_singer_song_pairs))))

    # print(counter_cosine_similarity(kkbox_singers, mymusic_singers))
    # print(counter_cosine_similarity(kkbox_songs, mymusic_songs))
    # print(counter_cosine_similarity(kkbox_singer_song_pairs, mymusic_singer_song_pairs))

    print(len(set(cathy_singers)))
    print(len(set(kkbox_singers)))

    print(count_singers)
    # print(count_songs)
    # print(count_singer_song_pairs)


checking_duplicate()

