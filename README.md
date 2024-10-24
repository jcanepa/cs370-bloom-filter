# Bloom Filter Implementation

This repository contains an implementation of a Bloom filter, a probabilistic data structure used to test whether an element is a member of a set. This project was developed for CS370 Intro to Computer Security, Oregon State University, 2024.

## Features

- Implementation of a Bloom filter.
- Functionality to load items into the Bloom filter and check for membership.
- Evaluation of Bloom filter accuracy, including statistics on true positives, false positives, true negatives, and false negatives.

## Prerequisites

Make sure you have the following installed:

- **Python 3.x**: You can download it from [here](https://www.python.org/downloads/).

To check if Python is installed, run:

```bash
python3 --version
```

## Running the Project

To execute the Bloom filter using main.py, run the following command:
```bash
python3 main.py
```

Make sure that any input files (e.g., rockyou.txt and dictionary.txt) are in the correct path as referenced in the main.py script.

## Usage

The main.py script sets up the Bloom filter and evaluates its performance. It reads in files like rockyou.txt for the seed data and dictionary.txt for testing. To adjust the files or settings, modify the main() function in main.py.

### Evaluating Bloom Filter Performance

The program outputs the following statistics to assess the accuracy of the Bloom filter:

* True Positive
* True Negative
* False Positive
* False Negative
