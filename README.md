# Topical Chatbot Experiments

This repository contains an early TensorFlow transformer-encoder notebook and a runnable TF-IDF response-retrieval baseline added during AI-assisted portfolio maintenance.

## Run the working baseline

With Python 3.12, install `python -m pip install -r requirements.txt`, then run:

```sh
python chat.py --message "What can you tell me about libraries?"
```

The included `data/demo.csv` is a tiny synthetic fixture, not the Topical-Chat benchmark. Supply `--data PATH` for a CSV with `conversation_id,message` columns. The script pairs adjacent messages within each conversation and retrieves the response to the closest matching prompt. Low-similarity queries receive a fallback response.

## Original notebook

The notebook preprocesses conversation data and constructs an encoder. It does not implement a complete trained generative chatbot: a decoder, training objective, training loop and generation loop are absent. A local name-shadowing error is corrected, but the missing training dataset and historical TensorFlow environment prevent an end-to-end reproduction claim. Do not present the retrieval baseline as a trained transformer.

## Attribution and limitations

The original notebook expects an external `topical_chat.csv`; its exact source, permissions and tutorial attribution need confirmation before redistributing it. The maintained baseline is AI-assisted work added during this review. No external service, API key, pretrained weights, deployment or conversational quality benchmark is included. Retrieval can repeat unsuitable dataset text; use only data you have permission to use and avoid private conversations.

## Official dataset route

The [Amazon Topical-Chat repository](https://github.com/alexa/Topical-Chat) provides the source conversation JSON and its [data terms](https://github.com/alexa/Topical-Chat/blob/master/DATALICENSE). Read those terms before use. No third-party dataset is redistributed here and no project license is added by this maintenance change.

Download `conversations/train.json` from upstream revision `7c939229cbcf6f55f6977b341a5a2f2fe982d53f`, then:

```sh
python prepare_data.py data/train.json data/topical_train.csv
python chat.py --data data/topical_train.csv --message "What do you like about music?"
```

The converter preserves conversation order and boundaries. Keep upstream validation/test splits separate when evaluating retrieval; do not index held-out responses and report that as generalisation. The historical CSV's exact provenance remains unknown.
`prepare_data.py` was verified against the official training split (188,378 turns), and retrieval inference completed. This checks execution, not conversational quality.
