from bloom_filter import BloomFilter
from bloom_filter_calculator import BloomFilterCalculator

def load_file_into_bloom(bf, file_path):
    """
    Load each line of a text file into the Bloom filter.

    Args:
        bf: The instance of the BloomFilter class
        file_path: Path to the text file
    """
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                bf.add(line.strip())
        print(f"Loaded file: {file_path} into the Bloom filter.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_lines_in_file(filepath):
    """
    Count the lines in a file at the given path.
    """
    try:
        with open(filepath, 'r', encoding='ISO-8859-1') as file:
            return file.read().count('\n')
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():

    filepath = 'templates/rockyou.ISO-8859-1.txt'

    # given a the amount of items in file
    line_count = count_lines_in_file(filepath)

    # given our desired false positive rate (1%)
    false_positive_rate = 0.01

    # calculate m (bit array size) and k (number of hash functions)
    size, hash_count = BloomFilterCalculator().get_parameters(
        n=line_count,
        p=false_positive_rate)

    # create BloomFilter with optimal m, and k
    bf = BloomFilter(size, hash_count)

    # load items
    load_file_into_bloom(
        bf, 'templates/rockyou.ISO-8859-1.txt')

    # check if items are in the filter
    print(bf.check('qwerty')), # expected "maybe"
    print(bf.check('jcanepa')), # expected "no"

if __name__ == "__main__":
    main()