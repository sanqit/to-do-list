def tracklist(**kwargs):
    for track_list_name, track_list in kwargs.items():
        print(track_list_name)
        for album, track in track_list.items():
            print(f"ALBUM: {album} TRACK: {track}")
