from gensim.models import KeyedVectors
from huggingface_hub import snapshot_download
model = KeyedVectors.load_word2vec_format("model.bin", binary=True, unicode_errors="ignore")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/similarity")
def hello_world():
    content = request.json
    word1 = content['word1']
    word2 = content['word2']
    print(model.similarity(word1, word2))
    if(model.similarity(word1, word2) > 0.9999998):
        return jsonify({"result":1})
    similarity = float(model.similarity(word1, word2))
    return jsonify({"result":similarity})

if __name__ == '__main__':
    port=3456
    ip="127.0.0.1"
    
    userPort = input("port (3456): ")
    userIp = input("port (127.0.0.1): ")

    if userPort:
        port=userPort

    if userIp:
        ip=userIp
    
    app.run(host=ip, port=port)