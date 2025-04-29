import tiktoken
from embedder import *


def get_embedder(vocabulary_size, context_length):
    path = '../data/primes.txt'
    return Embedder(vocabulary_size, context_length, path)

if __name__ == "__main__":
    # load tokenizer and extract relevant hyperparameters
    tokenizer = tiktoken.get_encoding('cl100k_base')
    vocabulary_size = tokenizer.n_vocab
    context_length = 1000

    # generate tokenizer hyperparameters from corpus
    embedder = get_embedder(vocabulary_size, context_length)
    print("finished loading embedder")

    # encode and decode a test string
    print(
        tokenizer.decode(
            embedder.decode(
                embedder.embed(
                    tokenizer.encode("this is a test, hello world!"))))
    )
