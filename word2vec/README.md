## How to setup first time

```
wget -O model.bin "https://huggingface.co/Word2vec/fauconnier_frWac_no_postag_phrase_500_cbow_cut100/resolve/main/frWac_no_postag_phrase_500_cbow_cut100.bin?download=true"
python3 -m venv dojo
source dojo/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

## How to launch 

```
python3 app.py
```

## Default usage

- ip: 127.0.0.1
- port: 3456

### Requests

POST /similarity

```
{
    "word1": "mot1",
    "word2": "mot2"
}
```

Result :

```
{
    "result": 0.16244417428970337
}
```

A number between 0 (very far) to 1 (the same word)

## Error

No error handling, give 500 if words are unknown or a sentence is sent instead of a word
