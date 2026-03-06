# Carver: Automated Binary Recovery Utility
A specialized digital forensics tool developed to recover deleted or orphaned files from raw disk images by identifying unique file signatures (Magic Bytes). This project demonstrates the practical application of data recovery algorithms used in professional forensic investigations.

## Key Features
Signature-Based Recovery: Scans raw binary data for specific headers and footers (Magic Bytes) to reconstruct files.

Multi-Format Support: Currently configured for JPEG and PDF recovery with an extensible architecture for adding new file types.

Data Integrity Filtering: Implements a minimum size threshold (500 bytes) to filter out false positives and fragmented "noise" in the binary stream.

Forensic Manifest Generation: Automatically generates a manifest.txt report that logs the type, offset (hex location), and size of every recovered file for an audit trail.

## Technical Logic
This utility operates on the principle that many files are not wiped from a disk when deleted; instead, their reference in the file system table is removed. By reading the disk image in Binary Read Mode (rb), this tool identifies:

Headers: The starting hex pattern (e.g., FF D8 FF E0 for JPEG).

Footers: The terminating hex pattern (e.g., FF D9 for JPEG).

Everything between these two points is "carved" out and saved as a functional file.

## Project Structure

Carver/
├── main.py          # The core carving engine and logic
├── signatures.py    # Dictionary of hex headers and footers
└── output/          # Directory where recovered files and manifest are stored
How to Run
Place your raw disk image (e.g., test_disk.bin) in the project directory.

#### Run the script:

python main.py

#### Enter the filename when prompted.

#### View recovered files and the forensic report in the output/ folder.
