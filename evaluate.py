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

def get_bf_parameters(n, p):

def evaluate_bloom_filter_with_stats(bf, seed_file, dictionary_file):
    """
    Evaluate the Bloom filter based on true/false positives and negatives.

    Args:
        bf (BloomFilter): The Bloom filter instance.
        seed_file (str): Path to the rockyou.txt file (positive values).
        dictionary_file (str): Path to the dictionary.txt file (test values).

    Returns:
        dict: A dictionary with TP, TN, FP, FN statistics.
    """
    # Read the rockyou.txt (positive set) into both Bloom filter and a set for validation
    positive_set = set()
    with open(seed_file, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            item = line.strip()
            positive_set.add(item)
            bf.add(item)

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0  # must be zero!

    # Read the dictionary.txt (test set) and evaluate each item
    with open(dictionary_file, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            item = line.strip()
            in_bloom_filter = bf.check(item)
            in_positive_set = item in positive_set

            if in_positive_set:
                # Should be in both the positive set and Bloom filter
                if in_bloom_filter:
                    true_positive += 1  # Correctly identified as present
                else:
                    false_negative += 1  # Should not happen in a proper Bloom filter
            else:
                # Should not be in the positive set
                if in_bloom_filter:
                    false_positive += 1  # Incorrectly identified as present
                else:
                    true_negative += 1  # Correctly identified as not present

    # Return the statistics
    return {
        "True Positive": true_positive,
        "True Negative": true_negative,
        "False Positive": false_positive,
        "False Negative": false_negative
    }

def main():

    seed_file_path = 'templates/rockyou.ISO-8859-1.txt'

    # given a the amount of items in file
    line_count = count_lines_in_file(seed_file_path)

    # given our desired false positive rate (1%)
    false_positive_rate = 0.01

    # calculate m (bit array size) and k (number of hash functions)
    size, hash_count = BloomFilterCalculator().get_parameters(
        n=line_count,
        p=false_positive_rate)

    # create BloomFilter with optimal m, and k
    bf = BloomFilter(size, hash_count)

    dictionary_file_path = 'templates/dictionary.txt'

    # TODO: verify bf is an instance of BloomFilter class
    results = evaluate_bloom_filter_with_stats(
        bf,
        seed_file_path,
        dictionary_file_path)

    # show results of bloom filter's accuracy test
    print(f"True Positive: {results['True Positive']}")
    print(f"True Negative: {results['True Negative']}")
    print(f"False Positive: {results['False Positive']}")
    print(f"False Negative: {results['False Negative']}")

if __name__ == "__main__":
    main()