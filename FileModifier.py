import os

def modify_content(content):
    """Example modification function - you can customize this"""
    # Convert to uppercase and add line numbers
    modified_lines = []
    for i, line in enumerate(content, 1):
        modified_lines.append(f"{i}: {line.upper()}")
    return modified_lines

def process_file():
    """Main function to handle file operations with error handling"""
    print("File Processor Program")
    print("---------------------\n")
    
    while True:
        try:
            # Get input filename from user
            input_filename = input("Enter the input file name (or 'quit' to exit): ").strip()
            
            if input_filename.lower() == 'quit':
                print("Exiting program...")
                return
            
            # Check if file exists and is readable
            if not os.path.exists(input_filename):
                raise FileNotFoundError(f"File '{input_filename}' does not exist")
                
            if not os.access(input_filename, os.R_OK):
                raise PermissionError(f"Permission denied: Cannot read '{input_filename}'")
                
            # Get output filename from user
            output_filename = input("Enter the output file name: ").strip()
            
            # Check if output file already exists
            if os.path.exists(output_filename):
                overwrite = input(f"File '{output_filename}' already exists. Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    print("Operation cancelled.")
                    continue
                    
            # Check if we can write to output location
            output_dir = os.path.dirname(output_filename) or '.'
            if not os.access(output_dir, os.W_OK):
                raise PermissionError(f"Permission denied: Cannot write to '{output_dir}'")
            
            # Read the input file
            try:
                with open(input_filename, 'r') as infile:
                    content = infile.readlines()
            except UnicodeDecodeError:
                raise UnicodeDecodeError("Could not decode the file - it may be a binary file")
            
            # Modify the content
            modified_content = modify_content(content)
            
            # Write to the output file
            try:
                with open(output_filename, 'w') as outfile:
                    outfile.writelines(modified_content)
                print(f"\nSuccessfully processed file! Output saved to '{output_filename}'")
                print(f"Modified {len(content)} lines.\n")
            except IOError as e:
                raise IOError(f"Error writing to file: {e}")
            
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.\n")
        else:
            # Successfully processed one file, ask if user wants to continue
            another = input("Process another file? (y/n): ").lower()
            if another != 'y':
                print("Exiting program...")
                return

if __name__ == "__main__":
    process_file()
