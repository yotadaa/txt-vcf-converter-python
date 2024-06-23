import os
import string

def read_numbers_from_file(file_path):
    """Read phone numbers from a file, each number separated by a newline."""
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()
    return numbers

def write_numbers_to_vcf(numbers, output_file, output_base, current):
    """Write phone numbers to a VCF file."""
    with open(output_file, 'w') as file:
        for i, number in enumerate(numbers):
            file.write("BEGIN:VCARD\n")
            file.write("VERSION:3.0\n")
            file.write(f"FN:{output_base}_{current*100+i+1}\n")
            file.write(f"TEL:{number}\n")
            file.write("END:VCARD\n")
            file.write("\n")  # Add a blank line between VCards for readability

def split_numbers_into_chunks(numbers, chunk_size):
    """Split a list of numbers into chunks of a specified size."""
    for i in range(0, len(numbers), chunk_size):
        yield numbers[i:i + chunk_size]


def main(input_file, output_base):
    input_file =  input_file  # Input text file containing phone numbers
    output_base = output_base  # Base name for output VCF files
    chunk_size = 100  # Number of contacts per VCF file

    # Read numbers from input file
    numbers = read_numbers_from_file(input_file)

    output_files = []
    # Split numbers into chunks and write each chunk to a separate VCF file
    for i, chunk in enumerate(split_numbers_into_chunks(numbers, chunk_size)):
        output_file = f"{output_base}_{i + 1}.vcf"
        write_numbers_to_vcf(chunk, output_file, f"{output_base}_{i + 1}", i)
        print(f"VCF file '{output_file}' created successfully.")
        output_files.append(output_file)
    return output_files
        
    

##if __name__ == "__main__":    
##    alphabet = string.ascii_uppercase
##    for i in range(15):
##        main(f"MM{alphabet[i]}.txt", f"MM{alphabet[i]}")
