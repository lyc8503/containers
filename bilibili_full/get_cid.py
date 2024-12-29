import bson
import sys
import tqdm
import math

collected = 0
total = 0

with open(sys.argv[1], 'wb') as out:
    for doc in tqdm.tqdm(bson.decode_file_iter(sys.stdin.buffer)):
        if 'data' not in doc:
            continue

        doc = doc['data']

        if 'pages' not in doc:
            continue
        
        total += 1

        if doc['stat']['view'] < 1000 or doc['stat']['danmaku'] < 20:
            continue

        collected += 1

        for p in doc['pages']:
            cid = p['cid']
            cid_bytes = cid.to_bytes(7, byteorder='big')
            out.write(cid_bytes)
            dur = math.ceil(p['duration'] / 6 / 60) # 6 min per segment
            if dur > 255:
                dur = 255
            dur_bytes = dur.to_bytes(1, byteorder='big')
            out.write(dur_bytes)

        if total % 100000 == 0:
            print(f'{collected}/{total} {collected/total:.2%}')