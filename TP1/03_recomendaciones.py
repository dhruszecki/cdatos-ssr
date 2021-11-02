import pickle
import csv
import gzip

with open('data_new/pid_track_uris.pickle', 'rb') as f:
    pid_track_uris = pickle.load(f)

# calculo el ranking de tracks
top_all = {}
with open("data_new/interactions.csv", "r") as f_interactions:
    reader = csv.DictReader(f_interactions)
    for row in reader:
        #top_all[row['track_uri']] = top_all.get(row['track_uri'], 0) + int(row['pos'])
        top_all[row['track_uri']] = top_all.get(row['track_uri'], 0) + 1

#top_tracks = [pid for (_, pid) in sorted([(top_all[k], k) for k in top_all], reverse=True)]
top_tracks = [pid for (_, pid) in sorted([(top_all[k], k) for k in top_all])]


with gzip.open('envio.csv.gz', 'wt') as f:
    _ = f.write("team_info,Roberto,rabalde@gmail.com\n")

    for pid in pid_track_uris:
        tracks_recomendados = []
        for tt in top_tracks:
            if tt in pid_track_uris[pid]:
                continue
            tracks_recomendados.append("spotify:track:" + tt)

            if len(tracks_recomendados) == 500:
                break
        _ = f.write(f"{pid},{','.join(tracks_recomendados)}\n")
