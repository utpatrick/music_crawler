import os
from collections import Counter
import math
import datetime
from crawlerhelpers import *
from languagecodeclasses import *


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
    kathy_singers_data_path = os.path.join('data_manual_clean', 'singers_union.txt')
    kathy_songs_data_path = os.path.join('data_manual_clean', 'songs_union.txt')
    kathy_pairs_data_path = os.path.join('data_manual_clean', 'pairs_union.txt')

    singer_path = 'singers_ALL_2011-01-01_2018-03-01'
    singer_path_s = 'singers_ALL_2017-01-01_2018-03-01'

    song_path = 'songs_ALL_2011-01-01_2018-03-01'
    song_path_s = 'songs_ALL_2017-01-01_2018-03-01'

    singer_song_pair_path = 'singer_song_pairs_ALL_2011-01-01_2018-03-01'
    singer_song_pair_path_s = 'singer_song_pairs_ALL_2017-01-01_2018-03-01'

    with open(kathy_singers_data_path) as data:
        cathy_singers = Counter(data.read().splitlines())
    with open(os.path.join(kkbox_path, singer_path)) as data:
        kkbox_singers = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, singer_path)) as data:
        mymusic_singers = Counter(data.read().splitlines())
    with open(os.path.join(spotify_path, singer_path_s)) as data:
        spotify_singers = Counter(data.read().splitlines())

    with open(kathy_songs_data_path) as data:
        cathy_songs = Counter(data.read().splitlines())
    with open(os.path.join(kkbox_path, song_path)) as data:
        kkbox_songs = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, song_path)) as data:
        mymusic_songs = Counter(data.read().splitlines())
    with open(os.path.join(spotify_path, song_path_s)) as data:
        spotify_songs = Counter(data.read().splitlines())

    with open(kathy_pairs_data_path) as data:
        cathy_singer_song_pairs = Counter(data.read().splitlines())
    with open(os.path.join(kkbox_path, singer_song_pair_path)) as data:
        kkbox_singer_song_pairs = Counter(data.read().splitlines())
    with open(os.path.join(mymusic_path, singer_song_pair_path)) as data:
        mymusic_singer_song_pairs = Counter(data.read().splitlines())
    with open(os.path.join(spotify_path, singer_song_pair_path_s)) as data:
        spotify_singer_song_pairs = Counter(data.read().splitlines())

    all_singers = []
    all_singers_set = list(set(mymusic_singers) | set(kkbox_singers) | set(spotify_singers) | set(cathy_singers))
    temp_singers = []
    singer_dup_count = 0
    for singer in all_singers_set:
        if len(singer) == 0:
            continue
        temp_singers.append(singer)
        keep_this = True

        # if singer.lower() not in all_singers and singer != "":
        #     for j in range(0, len(temp_singers)):
        #         if (temp_singers[j] in singer or singer in temp_singers[j]) and len(singer) != len(temp_singers[j]):
        #             print("singer_stored: {}".format(temp_singers[j]))
        #             keep_this = False
        #
        #     if not keep_this:
        #         print("-----current entry-----")
        #         print("singer_now: {}".format(singer))
        #         answer = input("wanna keep this data? (Y/n)")
        #         keep_this = (answer == "y" or answer == "")
        #         if answer == "gg":
        #             break
        #         print("")
        # else:
        #     singer_dup_count += 1
        #     keep_this = False

        if keep_this:
            all_singers.append(singer.lower())

    all_songs = []
    temp_songs = []
    all_songs_set = list(set(mymusic_songs) | set(kkbox_songs) | set(spotify_songs) | set(cathy_songs))
    song_dup_count = 0
    for song in all_songs_set:
        if len(song) == 0:
            continue
        temp_songs.append(song)
        keep_this = True

        # if song.lower() not in all_songs and song != "":
        #     for j in range(0, len(temp_songs)):
        #         if (temp_songs[j] in song or song in temp_songs[j]) and len(song) != len(temp_songs[j]):
        #             print("song_stored: {}".format(temp_songs[j]))
        #             keep_this = False
        #
        #     if not keep_this:
        #         print("-----current entry-----")
        #         print("song_now: {}".format(song))
        #         answer = input("wanna keep this data? (Y/n)")
        #         keep_this = (answer == "y" or answer == "")
        #         if answer == "gg":
        #             break
        #         print("")
        # else:
        #     song_dup_count += 1
        #     keep_this = False

        if keep_this:
            all_songs.append(song.lower())

    all_pairs = []
    temp_singers = []
    temp_songs = []
    all_pairs_set = list(set(mymusic_singer_song_pairs) | set(kkbox_singer_song_pairs) |
                         set(spotify_singer_song_pairs) | set(cathy_singer_song_pairs))
    pair_dup_count = 0
    counter = 0
    global this_pair
    for i in range(0, len(all_pairs_set)):
        this_pair = all_pairs_set[i].replace("\t\t", "\t")
        if len(this_pair) == 0:
            continue
        singer = this_pair.lower().split("\t")[0]
        temp_singers.append(singer)
        song = this_pair.lower().split("\t")[1]
        temp_songs.append(song)
        keep_this = True
        replace_this = False
        final_pair = []
        final_pair.append(this_pair)
        selection = 0

        if this_pair.lower() not in all_pairs and this_pair != "":
            for j in range(0, len(temp_songs)):
                if temp_songs[j] == song and \
                        ((temp_singers[j] in singer or singer in temp_singers[j]) and
                         len(temp_singers[j]) != len(singer)):
                    print("")
                    print("#{}: singer = {}, song = {}".format(len(final_pair),
                                                               temp_singers[j], song))
                    final_pair.append(temp_singers[j] + "\t" + song)
                    keep_this = False

            if not keep_this:
                print("-----current entry-----")
                print("#{}: singer = {}, song = {}".format(len(final_pair), singer, song))
                answer = input("wanna keep this data? (Y/n)")
                answer = ""
                keep_this = (answer != "n")
                range_list = []
                for k in range(1, len(final_pair)):
                    range_list.append(str(k))
                if answer == "gg":
                    break
                elif answer in range_list:
                    keep_this = False
                    replace_this = True
                    selection = int(answer)
                else:
                    keep_this = False
                    replace_this = False
                print("")
                counter += 1
        else:
            pair_dup_count += 1
            keep_this = False

        if keep_this:
            all_pairs.append(this_pair.lower())
        elif replace_this:
            if final_pair[selection].lower() not in all_pairs:
                all_pairs.append(this_pair.lower())
            else:
                all_pairs[all_pairs.index(final_pair[selection].lower())] = this_pair.lower()

    paths = ['data_manual_clean', 'results']
    start_date = datetime.datetime(2011, 1, 1)
    end_date = datetime.datetime(2018, 3, 1)
    file_writer(Language.ALL, start_date, end_date, all_singers, all_songs, [], all_pairs, paths)

    print("singer_dup_count: {}".format(singer_dup_count))
    print("song_dup_count: {}".format(song_dup_count))
    print("pair_dup_count: {}".format(pair_dup_count))

    # count_singers = len(list(((set(kkbox_singers) | set(spotify_singers)) & set(cathy_singers))))
    # count_songs = len(list((set(kkbox_songs) & set(mymusic_songs))))
    # count_singer_song_pairs = len(list((set(kkbox_singer_song_pairs) & set(mymusic_singer_song_pairs))))

    # print(counter_cosine_similarity(kkbox_singers, mymusic_singers))
    # print(counter_cosine_similarity(kkbox_songs, mymusic_songs))
    # print(counter_cosine_similarity(kkbox_singer_song_pairs, mymusic_singer_song_pairs))


checking_duplicate()