from pymongo import MongoClient

def find_missing_ids(collection, start_id, end_id, threshold=100_0000):
    print(f"Checking range {start_id} - {end_id}")
    expected_count = end_id - start_id
    actual_count = collection.count_documents({"_id": {"$gte": start_id, "$lt": end_id}})
    if expected_count == actual_count:
        return []
    if expected_count <= threshold:
        existing_ids = collection.find({"_id": {"$gte": start_id, "$lt": end_id}}, {"_id": 1})
        existing_ids = set(doc["_id"] for doc in existing_ids)
        return [i for i in range(start_id, end_id) if i not in existing_ids]
    else:
        mid_id = start_id + (end_id - start_id) // 2
        missing_left = find_missing_ids(collection, start_id, mid_id, threshold)
        missing_right = find_missing_ids(collection, mid_id, end_id, threshold)
        return missing_left + missing_right

with MongoClient("mongodb://localhost:27017/") as client:
    collection = client['bili']['meta']
    missing_ids = find_missing_ids(collection, 0, 1_000_000_000)
    print(missing_ids)
    print(f"{len(missing_ids)=}")

