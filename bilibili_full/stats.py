import zstandard as zstd
import bson
from tqdm import tqdm
from elasticsearch import Elasticsearch, helpers
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


es = Elasticsearch('https://localhost:9200/', basic_auth=('elastic', 'phwQXCtxEc0L6mNFcYD9'), verify_certs=False)

es.indices.create(index='bilibili', ignore=400)

dctx = zstd.ZstdDecompressor()
with dctx.stream_reader(sys.stdin.buffer) as reader:
    def to_action(x):
        _id = x['_id']
        del x['_id']
        return {'_index': 'bilibili', '_id': _id, '_source': x}
    for i in tqdm(helpers.streaming_bulk(es, map(to_action, bson.decode_file_iter(reader))), total=1_3000_0000):
        pass
