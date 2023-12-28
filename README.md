# Socket Programming-Based File Backup System

## Introduction
Client Repository of the Backup System. This repository contains the client-side scripts crucial for processing, analyzing, `Sender.py` script, which efficiently handles the transmission of files in a chunked manner.

## Repository Contents

1. **AbstractiveSummary.py**
   - Implements abstractive summary generation for text files.

2. **CodeConverter.py**
   - Converts various file formats to text for processing.

3. **FileManagement.py**
   - Manages file operations and prepares files for backup.

4. **ImageClassification.py**
   - Classifies images using advanced ML models.

5. **KeybertExtractor.py**
   - Extracts keywords from text using KeyBERT.

6. **PIIData.py**
   - Detects and categorizes PII data in text files.

7. **VideoClassification.py**
   - Classifies video files using ML techniques.

8. **Sender.py**
   - Manages the transmission of files to the server in chunks.
   - Ensures data integrity using checksums.
   - Incorporates ML-generated metadata for each file.

9. **Runner.py**
   - Orchestrates the entire file backup process, integrating Sender and Tag generation scripts.

## Sender.py: File Transmission in Chunks
`Sender.py` is designed to efficiently handle large file transfers over the network. It segments files into manageable chunks, ensuring reliable and secure data transmission even in case of large files or unstable network conditions. Here's how it works:

- **Initialization**: Configures connection settings and file details.
- **Chunked Transmission**: Files are divided and sent in chunks, controlled by a specified chunk size.
- **Checksum Verification**: Each file's integrity is ensured through checksum verification.
- **ML Metadata Integration**: Sends ML-generated metadata (like summaries, keywords, PII data) along with the file.

## Usage
To use these scripts for backing up your files:
1. Ensure all dependencies are installed.
2. Configure each script as needed for your environment.
3. Run `Runner.py` to initiate the backup process.

## Contributing
We welcome contributions to enhance the functionalities of this client-side backup system. Your expertise can significantly improve the efficiency and security of the file transfer process.
