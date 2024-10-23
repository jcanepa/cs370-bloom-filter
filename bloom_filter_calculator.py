import math

class BloomFilterCalculator:
    """
    A static class to calculate the optimal size and number of hash functions for a Bloom filter.
    """

    @staticmethod
    def calculate_m(n, p):
        """
        Calculate the optimal bit-size for the Bloom filter, m.

        Args:
            n (int): The expected number of items to be stored in the Bloom filter.
            p (float): The desired false positive rate (e.g., 0.01 for 1%).

        Returns:
            int: The optimal size (m) of the Bloom filter in bits.
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)  # integer (rounds down)

    @staticmethod
    def calculate_k(m, n):
        """
        Calculate the optimal number of hash functions for the Bloom filter, k.

        Args:
            m (int): The size of the bit array (in bits).
            n (int): The expected number of items to be stored in the Bloom filter.

        Returns:
            int: The optimal number of hash functions (k).
        """
        k = (m / n) * math.log(2)
        return int(k)  # integer (rounds down)

    @staticmethod
    def get_parameters(n, p):
        """
        Get both the optimal size and hash count for the Bloom filter.

        Args:
            n (int): The expected number of items to be stored in the Bloom filter.
            p (float): The desired false positive rate.

        Returns:
            tuple: A tuple containing (size_in_bits, number_of_hash_functions).
        """
        size = BloomFilterCalculator.calculate_m(n, p)
        hashes = BloomFilterCalculator.calculate_k(size, n)
        return size, hashes