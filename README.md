
# PDF Chunker

PDF Chunker is a Python script designed to split large PDF files into smaller chunks based on a user-defined maximum size limit. It maintains the sequence of pages and names the output files based on page ranges for clarity.

## Features
- **Configurable Size Limit**: Specify the maximum size (in MB) for each output chunk.
- **Page Range Naming**: Output files are named using the page range they cover (e.g., `pages_1_5.pdf`).
- **Error Handling**: Handles invalid input files and ensures valid configurations.
- **Cross-Platform**: Works on macOS, Linux, and Windows.

## Requirements
- Python 3.7+
- PyPDF2 library (version 3.0 or higher)

Install dependencies using:
```bash
pip install PyPDF2
```

## Usage
Run the script with the following arguments:

```bash
python pdfChunker.py [input_pdf] [output_dir] [--max-size MAX_SIZE]
```

### Arguments
- `input_pdf`: Path to the input PDF file (required).
- `output_dir`: Directory where the output files will be saved (required).
- `--max-size`: Maximum size (in MB) for each output file (default: `5.0` MB).

### Examples
1. Split a PDF into chunks of 5MB (default):
   ```bash
   python pdfChunker.py /path/to/input.pdf /path/to/output/dir
   ```

2. Split a PDF into chunks of 3MB:
   ```bash
   python pdfChunker.py /path/to/input.pdf /path/to/output/dir --max-size 3
   ```

3. Split a PDF into chunks of 1MB:
   ```bash
   python pdfChunker.py /path/to/input.pdf /path/to/output/dir --max-size 1
   ```

## Example Output
For an input PDF with 10 pages, the output might look like this (if splitting at 3MB):
```
output_dir/
├── pages_1_3.pdf
├── pages_4_6.pdf
├── pages_7_10.pdf
```

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Built with [PyPDF2](https://pypdf2.readthedocs.io/).
- Inspired by the need for splitting large PDF files for resource-constrained environments.

