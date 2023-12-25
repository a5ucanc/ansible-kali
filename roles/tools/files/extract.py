import os
import sys
import shutil
import tarfile
import zipfile
import gzip
import argparse
import stat

def extract_file(src, dest):
    extracted_files = []
    if src.endswith('.zip'):
        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall(dest)
            extracted_files = [os.path.join(dest, file) for file in zip_ref.namelist()]
    elif src.endswith('.tar.gz') or src.endswith('.tgz') or src.endswith('.tar') or src.endswith('.bz2'):
        mode = 'r:gz' if src.endswith('.tar.gz') or src.endswith('.tgz') else 'r:bz2' if src.endswith('.bz2') else 'r:'
        with tarfile.open(src, mode) as tar_ref:
            tar_ref.extractall(dest)
            extracted_files = [os.path.join(dest, member.name) for member in tar_ref.getmembers() if member.isfile()]
    elif src.endswith('.gz'):
        filename = os.path.join(dest, os.path.basename(src)[:-3])
        with gzip.open(src, 'rb') as gz_ref, open(filename, 'wb') as out_f:
            shutil.copyfileobj(gz_ref, out_f)
            extracted_files.append(filename)
    else:
        print(f"Unsupported file format: {src}")
        sys.exit(0)
    return extracted_files

def set_permissions(file_paths):
    for file_path in file_paths:
        os.chmod(file_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

def main():
    parser = argparse.ArgumentParser(description="Extract compressed files")
    parser.add_argument("source", help="Path to the compressed file")
    parser.add_argument("destination", help="Path to extract the files to")
    args = parser.parse_args()

    extracted_files = extract_file(args.source, args.destination)
    set_permissions(extracted_files)
    os.remove(args.source)

if __name__ == "__main__":
    main()
