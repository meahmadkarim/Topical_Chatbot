"""TF-IDF response retrieval baseline; not a generative language model."""
import argparse,csv
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_pairs(path):
    with open(path,encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if not rows or not {'conversation_id','message'}.issubset(rows[0]): raise ValueError('CSV must contain conversation_id and message')
    return [(a['message'],b['message']) for a,b in zip(rows,rows[1:]) if a['conversation_id']==b['conversation_id'] and a['message'].strip() and b['message'].strip()]

def respond(pairs,message,threshold=.15):
    if not pairs: raise ValueError('No adjacent conversation pairs found')
    vectorizer=TfidfVectorizer(ngram_range=(1,2))
    matrix=vectorizer.fit_transform([p[0] for p in pairs])
    scores=cosine_similarity(vectorizer.transform([message]),matrix)[0]
    best=int(scores.argmax())
    return pairs[best][1] if scores[best]>=threshold else 'I do not have a matching response in this dataset.'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',default='data/demo.csv');p.add_argument('--message',required=True);args=p.parse_args()
    print(respond(load_pairs(args.data),args.message))
