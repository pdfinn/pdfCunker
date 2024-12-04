import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_dir, max_size_mb):
    """
    Splits a PDF into smaller chunks, each under the specified size limit, and names files by page ranges.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_dir (str): Directory to save the output chunks.
        max_size_mb (int): Maximum size of each chunk in MB.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_pdf)
    num_pages = len(reader.pages)
    max_size_bytes = max_size_mb * 1024 * 1024

    chunk_start_page = 0  # Start of the current range
    writer = PdfWriter()

    for current_page in range(num_pages):
        writer.add_page(reader.pages[current_page])

        # Save to a temporary file to check the size
        temp_file = os.path.join(output_dir, "temp_file.pdf")
        with open(temp_file, "wb") as temp_output:
            writer.write(temp_output)
        temp_size = os.path.getsize(temp_file)

        if temp_size > max_size_bytes:
            # Save the current chunk excluding the last page
            writer = PdfWriter()
            for i in range(chunk_start_page, current_page):  # Rebuild without the last page
                writer.add_page(reader.pages[i])
            output_file = os.path.join(output_dir, f"pages_{chunk_start_page + 1}_{current_page}.pdf")
            with open(output_file, "wb") as final_output:
                writer.write(final_output)
            print(f"Saved {output_file} under {max_size_mb}MB.")

            # Start a new chunk with the current page
            writer = PdfWriter()
            writer.add_page(reader.pages[current_page])
            chunk_start_page = current_page

        # Clean up the temporary file
        os.remove(temp_file)

    # Save the last chunk if it contains any pages
    if len(writer.pages) > 0:
        output_file = os.path.join(output_dir, f"pages_{chunk_start_page + 1}_{num_pages}.pdf")
        with open(output_file, "wb") as final_output:
            writer.write(final_output)
        print(f"Saved {output_file} under {max_size_mb}MB.")

def main():
    parser = argparse.ArgumentParser(description="Split a PDF into smaller chunks by size.")
    parser.add_argument("input_pdf", help="Path to the input PDF file.")
    parser.add_argument("output_dir", help="Directory to save the output PDF chunks.")
    parser.add_argument(
        "--max-size", type=float, default=5.0, help="Maximum size of each output chunk in MB (default: 5MB)."
    )
    args = parser.parse_args()

    # Validate arguments
    if not os.path.isfile(args.input_pdf):
        print("Error: Input PDF file does not exist.")
        return
    if args.max_size <= 0:
        print("Error: Maximum size must be greater than 0 MB.")
        return

    split_pdf(args.input_pdf, args.output_dir, args.max_size)

if __name__ == "__main__":
    main()
