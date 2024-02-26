# иморт scv модуля
from csv import reader, writer

#открываем файл scv
with open("songs.csv", encoding="utf-8") as data_file:
    scv_data = reader(data_file, delimiter=",")
    for song_data in scv_data:
        song_name = song_data[2]
        artist_name = song_data[1]
        song_count = song_data[0]
        song_time = song_data[3].split('.')
