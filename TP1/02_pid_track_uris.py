import json
import pickle

pid_track_uris = {}

with open("challenge_set.json", "r") as f:
    cs = json.load(f)
    for pl in cs["playlists"]:        
        
        list_tracks = []
        for t in pl['tracks']:
            list_tracks.append(t['track_uri'].replace('spotify:track:', ''))

        pid_track_uris[pl["pid"]] = list_tracks

with open('data_new/pid_track_uris.pickle', 'wb') as f:
    pickle.dump(pid_track_uris, f)
