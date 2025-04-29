import gmpy2


class PrimeOps:
    def __init__(self, primes_path, load_until_checkpoint=1000):
        self.primes_path = primes_path
        self._primes = PrimeOps.read_line_by_line(self.primes_path, load_until_checkpoint)

    def get(self, idx):
        return self._primes[idx]

    @staticmethod
    def read_line_by_line(path, stop_at_line_n):
        # read the first N lines of the .txt file provided in input
        # There is a prime number on every line, store each as a gmpy2.mpz(p) variable
        # return a list of primes until stop_at_line_n
        result = []
        with open(path) as f:
            counter = 0
            for line in f:
                if counter == stop_at_line_n:
                    break

                result.append(gmpy2.mpz(int(line)))
                counter += 1

        return result

    def find_divisible_prime_idx(self, N):
        # we assume N is in gmpy2 format
        return [i for i, prime in enumerate(self._primes) if N % prime == 0]

if __name__ == '__main__':
    # just a few simple tests
    path = '../data/primes.txt'
    pops = PrimeOps(path, load_until_checkpoint=10000000)

    print(pops._primes[:10])
    print(len(pops._primes))

    test_N = gmpy2.mpz(pops._primes[-1]) * gmpy2.mpz(pops._primes[-2]) * gmpy2.mpz(pops._primes[-3])
    print(pops.find_divisible_prime_idx(test_N))