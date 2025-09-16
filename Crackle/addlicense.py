import os
import sys

# Define your license header text here
LICENSE_HEADER = """// Copyright (c) Devan Iyer
// Licensed under the MIT License.
// See LICENSE file in the project root for full license information.

"""

# File extensions to process
FILE_EXTENSIONS = ['.cs', '.razor', '.js', '.css']

def has_license(lines):
    # Simple check if license text already present (adjust as needed)
    sample = ''.join(lines[:len(LICENSE_HEADER.splitlines())]).lower()
    return 'copyright' in sample or 'license' in sample

def add_license_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check if already has license header
    if has_license(lines):
        print(f"License already present in {file_path}, skipping.")
        return

    # Preserve shebang if present on first line (common in scripts)
    shebang = ''
    if lines and lines[0].startswith('#!'):
        shebang = lines[0]
        lines = lines[1:]

    # Prepend license header
    new_content = [shebang] if shebang else []
    new_content.append(LICENSE_HEADER)
    new_content.extend(lines)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    print(f"Added license header to {file_path}")

def process_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in FILE_EXTENSIONS):
                file_path = os.path.join(dirpath, filename)
                try:
                    add_license_to_file(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_license.py <path-to-your-blazor-project>")
        sys.exit(1)

    root_directory = sys.argv[1]
    process_directory(root_directory)
