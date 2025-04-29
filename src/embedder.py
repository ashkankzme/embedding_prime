from prime_ops import *
import gmpy2
import random

class Embedder:
    def __init__(self, vocabulary_size, context_length, primes_path):
        self.vocabulary_size = vocabulary_size
        self.context_length = context_length
        self.pops = PrimeOps(primes_path, load_until_checkpoint=vocabulary_size*context_length)

    def get_prime_encoding(self, position_idx, token_id):
        # we assume pairs of position and token (<i, token_id>) are assigned to the idx-th prime
        row = position_idx
        column = token_id
        idx = (row * self.vocabulary_size) + column
        return self.pops.get(idx)

    def embed(self, tokens):
        result = gmpy2.mpz(1) # denotes empty string/operator
        for i, token_id in enumerate(tokens):
            result *= self.get_prime_encoding(i, token_id)
        return result

    def assemble_tokens(self, parts, ordered_tokens):
        for part in parts:
            position = part // self.vocabulary_size
            token_id = part % self.vocabulary_size
            ordered_tokens[position] = token_id
        return ordered_tokens

    def decode(self, prime_embedding):
        parts = self.pops.find_divisible_prime_idx(prime_embedding)
        ordered_tokens = [None for _ in range(len(parts))]
        return self.assemble_tokens(parts, ordered_tokens)


if __name__ == "__main__":
    # simple test of functionality
    random.seed(42)
    primes_path = '../data/primes.txt'

    e = Embedder(32, 16, primes_path)
    test_input = [random.randint(0, 31) for _ in range(random.randint(1, 16))]

    print(test_input)
    encoded = e.embed(test_input)
    print(encoded)
    decoded = e.decode(encoded)
    print(decoded)