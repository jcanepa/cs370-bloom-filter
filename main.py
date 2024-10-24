from bloom_filter import BloomFilter
from bloom_filter_calculator import BloomFilterCalculator

def read_file_lines(file_path, encoding='ISO-8859-1'):
    """
    Read each line from a file and return a list of stripped lines.

    Args:
        file_path (str): The path to the file.
        encoding (str): The file encoding (default is 'ISO-8859-1').

    Returns:
        list: A list of lines from the file.
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return []

def load_file_into_bloom(bf, file_path):
    """
    Load each line of a text file into the bloom filter.

    Args:
        bf: the instance of the BloomFilter class
        file_path: path to the text file
    """
    lines = read_file_lines(file_path)
    for line in lines:
        bf.add(line)
    print(f"Loaded file: {file_path} into the bloom filter.")

def count_lines_in_file(filepath):
    """
    Count the lines in a file at the given path.

    Args:
        filepath (str): the path to the file.

    Returns:
        int: the number of lines in the file.
    """
    lines = read_file_lines(filepath)
    return len(lines)

def get_bf_parameters(n, p):
    """
    Get bloom filter parameters (size and hash count) based on expected items and desired false positive rate.

    Args:
        n (int): the expected number of items to be stored in the bloom filter.
        p (float): the desired false positive rate (e.g., 0.01 for 1%).

    Returns:
        tuple: a tuple containing (size_in_bits, number_of_hash_functions).
    """
    return BloomFilterCalculator().get_parameters(n, p)

def evaluate_bloom_filter_with_stats(bf, seed_file, dictionary_file):
    """
    Evaluate the bloom filter based on true/false positives and negatives.

    Args:
        bf (BloomFilter): the bloom filter instance.
        seed_file (str): path to the rockyou.txt file (positive values).
        dictionary_file (str): path to the dictionary.txt file (test values).

    Returns:
        dict: a dictionary with TP, TN, FP, FN statistics.
    """
    # read the seed file (positive set) and add to bloom filter
    positive_set = set(read_file_lines(seed_file))
    for item in positive_set:
        bf.add(item)

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0  # should remain zero!

    # read the dictionary file (test set) and evaluate each item
    dictionary_items = read_file_lines(dictionary_file)
    for item in dictionary_items:
        in_bloom_filter = bf.check(item)
        in_positive_set = item in positive_set

        if in_positive_set:
            # should be in both the positive set and bloom filter
            if in_bloom_filter:
                true_positive += 1  # correctly identified as present
            else:
                false_negative += 1  # should not happen in a proper bloom filter
        else:
            # should not be in the positive set
            if in_bloom_filter:
                false_positive += 1  # incorrectly identified as present
            else:
                true_negative += 1  # correctly identified as not present

    # calculate total items and percentages
    total_items = true_positive + true_negative + false_positive + false_negative

    true_positive_percentage = (true_positive / total_items) * 100 if total_items else 0
    true_negative_percentage = (true_negative / total_items) * 100 if total_items else 0
    false_positive_percentage = (false_positive / total_items) * 100 if total_items else 0
    false_negative_percentage = (false_negative / total_items) * 100 if total_items else 0

    # return the statistics
    return {
        "True Positive": (true_positive, f"{true_positive_percentage:.2f}%"),
        "True Negative": (true_negative, f"{true_negative_percentage:.2f}%"),
        "False Positive": (false_positive, f"{false_positive_percentage:.2f}%"),
        "False Negative": (false_negative, f"{false_negative_percentage:.2f}%")
    }


def main():
    # word list used to populate bloom filter
    seed_file_path = 'templates/rockyou.ISO-8859-1.txt'

    # count the number of items in the file
    line_count = count_lines_in_file(
        seed_file_path
    )

    # desired false positive rate (1%)
    false_positive_rate = 0.01

    # calculate bit array size (m) & number of hash functions (k)
    size, hash_count = get_bf_parameters(
        n=line_count,
        p=false_positive_rate
    )

    # create bloom filter with optimal m and k
    bf = BloomFilter(
        size,
        hash_count
    )

    dictionary_file_path = 'templates/dictionary.txt'

    # evaluate bloom filter and get results
    results = evaluate_bloom_filter_with_stats(
        bf,
        seed_file_path,
        dictionary_file_path
    )

    # display the results of bloom filter's accuracy test
    print(f"True Positive: {results['True Positive']}")
    print(f"True Negative: {results['True Negative']}")
    print(f"False Positive: {results['False Positive']}")
    print(f"False Negative: {results['False Negative']}")

if __name__ == "__main__":
    main()