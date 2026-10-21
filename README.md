# Cemantix – Serverless Edition

A small Cemantix-style word guessing game: type a word, and find out how semantically close it is to a secret word.

The project is split into three parts that talk to each other over HTTP:

```
Angular front-end  ──GET /?word=chat──▶  Deno serverless function  ──POST /similarity──▶  word2vec API
                   ◀──── {"value": 42} ──                         ◀──── {"result": 0.42} ──
```

## Architecture

| Part | Location | Role |
|------|----------|------|
| Front-end | `dojo-cs-cemantics/` | Angular + PrimeNG UI: input field, send button, progress bar and a hint message |
| Serverless function | `index.ts` | Deno function deployed on Deno Deploy. Reads the word from the URL, compares it to the secret word and returns a score |
| Similarity API | `word2vec/` | Python service that computes word similarity with a French word2vec model (`POST /similarity`) |

### How it works

1. The user types a word in the Angular app and clicks **Send**.
2. `ApiClientService` calls the serverless function with the word as a query parameter: `GET <function-url>/?word=chat`.
3. The `handler` in `index.ts` extracts `word` from the request URL and calls the word2vec API with `{ "word1": "<word>", "word2": "<secret word>" }`.
4. The API returns a similarity between 0 and 1. The function converts it into a score from 0 to 100: `{ "value": 42 }`.
5. The front-end shows the score on a progress bar with a message (from "T'es loin là ! 🥶" to "Félicitations ! 🎉"). Unknown words return a 404 and display "Mot inconnu... 🫠".

The function also answers CORS preflight (`OPTIONS`) requests so the browser can call it from another origin.

## Running it

### Serverless function (Deno)

```bash
deno run --allow-net index.ts
# Listening on http://localhost:8000
curl "http://localhost:8000/?word=chat"
```

The function is deployed on Deno Deploy; the front-end calls its public URL (see `functionUrl` in `api-client.service.ts`).

### Front-end (Angular)

```bash
cd dojo-cs-cemantics
npm install
ng serve
# open http://localhost:4200
```

To use a locally running function, change `functionUrl` in `src/app/service/api-client.service.ts` to `http://localhost:8000/`.

### word2vec API (optional)

A hosted instance is already used by the function. To run it yourself, see `word2vec/README.md`.

## Tech stack

Angular, PrimeNG, RxJS, TypeScript, Deno / Deno Deploy, Python (word2vec).
