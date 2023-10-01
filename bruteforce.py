import threading
import hashlib
import queue
import pymongo
mongo_client = pymongo.MongoClient("mongodb+srv://sagibarkai7080:S1a2g3i4@cluster0.zl0ospo.mongodb.net/")
db = mongo_client["common_passwords"]
collection = db["passwords"]

def md5_hash(password):
    result = hashlib.md5(password.encode())
    return result.hexdigest()


def get_wordlist_from_mongodb():
    wordlist = []
    for doc in collection.find({}, projection={"text": 1}):
        wordlist.append(doc['text'])
    return wordlist


def bruteforce(wordlist, password, result_queue):
    for guess_password in wordlist:
        if md5_hash(guess_password) == password:
            result_queue.put(guess_password)


def decrypt(encrypted_password):
    wordlist = get_wordlist_from_mongodb()
    result_queue = queue.Queue()
    t = threading.Thread(target=bruteforce, args=(wordlist, encrypted_password, result_queue))
    t.start()
    t.join()

    if not result_queue.empty():
        return result_queue.get()
    else:
        return "sorry,cant decrypt this passsword"
