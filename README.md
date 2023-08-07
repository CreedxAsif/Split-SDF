# Split SDF Utility

## Overview

This repository contains a utility for splitting large SDF (Structure-Data File) files into smaller, more manageable chunks. SDF files are commonly used to store chemical structures and associated data, making them a crucial format in cheminformatics and drug discovery.

## Features

- Efficiently splits large SDF files into smaller files for easier handling and analysis.
- Maintains the integrity of chemical structures and associated data during the splitting process.
- Configurable options for specifying the number of records or size of each split file.
- Simple and user-friendly command-line interface.

## Usage

To split an SDF file using Split_SDF, follow these steps:

1. Clone this repository or download the latest release.
2. Open a terminal window and navigate to the Split_SDF directory.
3. Run the following command: python split_SDF.py -i input_file.sdf -n molecules_per_file -o output_directory

5. Replace `input_file.sdf` with the path to your SDF file, `molecules_per_file` with the desired number of molecules per output file, and `output_directory` with the directory where you want the output files to be saved.

For more information and additional options, run: python split_sdf.py -h

