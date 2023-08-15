# EMG Data Processing Scripts

This repository contains Python scripts for processing and filtering EMG (Electromyography) data. The scripts implement various filtering techniques to preprocess raw EMG signals and generate filtered outputs.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Introduction

EMG data processing is crucial for analyzing muscle activity in various applications, such as biomechanics, neuroscience, and rehabilitation. This collection of Python scripts provides tools to preprocess EMG signals by applying different types of filters.

## Requirements

- Python (3.x recommended)
- NumPy
- SciPy
- Matplotlib
- pandas

## Usage

1. Clone the repository to your local machine:

`git clone https://github.com/symatevo/EMG-data.git`

2. Navigate to the cloned repository:

`cd EMG-data`


3. Execute the individual Python scripts to perform specific filtering operations on your EMG data. Make sure to replace `'ID_AH_Movement_1.txt'` and `'ID_AV Movement 2.txt'` with your actual data file names.

Example:

python Butterworth_filter.py
python Filters_9plots.py
python bandpass.py


4. Filtered data will be saved as CSV files in the repository.

## File Descriptions

- `Butterworth_filter.py`: Implements a Butterworth highpass filter on EMG data.
- `Filters_9plots.py`: Applies a bandpass filter and generates plots for comparison.
- `bandpass.py`: Applies a bandpass filter and saves filtered data to a CSV file.


