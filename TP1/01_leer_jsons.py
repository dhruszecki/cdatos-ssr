import json
import csv
import os

path = 'data'
tracks = {}
interactions = []

with open('data_new/playlists.csv', 'w', newline='', encoding='utf-8') as pl_csv:
    fieldnames = ['pid', 'name', 'description', 'collaborative', 'modified_at', 'num_tracks', 'num_albums', 'num_followers', 'num_edits', 'duration', 'num_artists']
    pl_writer = csv.DictWriter(pl_csv, fieldnames)
    _ = pl_writer.writeheader()

    for fn in os.listdir(path):
        print(fn)
        if not fn.startswith("mpd.slice.") or not fn.endswith(".json"):
            continue

        with open(f'data/{fn}', 'rt') as f:
            j = json.load(f)
            for pl in j['playlists']:
                for t in pl.pop('tracks'):
                    t['track_uri'] = t['track_uri'].replace("spotify:track:", "")
                    interactions.append( {'pid': pl['pid'], 'track_uri': t['track_uri'], 'pos': t['pos']} )

                    del t['pos']
                    tracks[t['track_uri']] = t

                pl['duration'] = int(int(pl.pop('duration_ms')) / 1000)      
                pl['collaborative'] = int(pl['collaborative'] == 'true')
                _ = pl_writer.writerow(pl)

# escribo tracks
with open('data_new/tracks.csv', 'w', newline='', encoding='utf-8') as tracks_csv:
    fieldnames = ['track_uri', 'artist_name', 'artist_uri', 'track_name', 'album_uri', 'duration_ms', 'album_name']
    tracks_writer = csv.DictWriter(tracks_csv, fieldnames)
    _ = tracks_writer.writeheader()    
    tracks_writer.writerows(tracks.values())

# escribo interactions
with open('data_new/interactions.csv', 'w', newline='', encoding='utf-8') as interactions_csv:
    fieldnames = ['track_uri', 'pid', 'pos']
    interactions_writer = csv.DictWriter(interactions_csv, fieldnames)
    _ = interactions_writer.writeheader()    
    interactions_writer.writerows(interactions)
