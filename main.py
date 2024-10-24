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

def evaluate_bloom_filter(bloom_filter, test_items, positive_set, negative_set):
    """
    Evaluate the Bloom filter and compute TP, TN, FP, FN statistics.

    Args:
        bloom_filter (BloomFilter): The Bloom filter instance.
        test_items (list): A list of test items to check against the Bloom filter.
        positive_set (set): The set of items that are known to be in the Bloom filter.
        negative_set (set): The set of items that are known to be outside the Bloom filter.

    Returns:
        dict: A dictionary with TP, TN, FP, FN counts.
    """
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0  # Should be zero in a correct Bloom filter implementation

    for item in test_items:
        in_bloom_filter = bloom_filter.check(item)

        if item in positive_set:
            if in_bloom_filter:
                true_positive += 1  # Correctly identified as present
            else:
                false_negative += 1  # Should not happen in a proper Bloom filter
        elif item in negative_set:
            if in_bloom_filter:
                false_positive += 1  # Incorrectly identified as present
            else:
                true_negative += 1  # Correctly identified as not present

    # Return the statistics as a dictionary
    return {
        "True Positive": true_positive,
        "True Negative": true_negative,
        "False Positive": false_positive,
        "False Negative": false_negative
    }

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

    # Example usage
    # positive_set = {"apple", "banana", "grape"}  # Items added to the Bloom filter
    # negative_set = {"orange", "kiwi", "mango"}  # Items not in the Bloom filter
    # test_items = ["apple", "orange", "banana", "mango", "kiwi", "grape", "pineapple"]  # Test file items

    # # Assume bloom is an instance of your BloomFilter class and is already loaded
    # results = evaluate_bloom_filter(bloom, test_items, positive_set, negative_set)

    # print(f"True Positive: {results['True Positive']}")
    # print(f"True Negative: {results['True Negative']}")
    # print(f"False Positive: {results['False Positive']}")
    # print(f"False Negative: {results['False Negative']}")

if __name__ == "__main__":
    main()