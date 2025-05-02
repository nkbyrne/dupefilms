#!/usr/bin/env python3

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Valid video file extensions
VIDEO_EXTENSIONS = {'.mkv', '.mp4', '.avi', '.mov'}

# Regex to extract movie title without resolution tags
def extract_movie_key(filename):
    name = filename.lower()
    # Remove resolution and encoding tags
    cleaned = re.sub(r'\.(720p|1080p|2160p|4k|bluray|webrip|dvdrip|hdr|x264|x265|hevc).*', '', name)
    cleaned = re.sub(r'\W+', '.', cleaned).strip('.')
    return cleaned

# Recursively find all movie files under multiple base paths
def find_movies(base_paths):
    movie_files = defaultdict(list)
    for base_path in base_paths:
        for root, _, files in os.walk(base_path):
            for f in files:
                ext = Path(f).suffix.lower()
                if ext in VIDEO_EXTENSIONS:
                    full_path = os.path.join(root, f)
                    key = extract_movie_key(f)
                    movie_files[key].append(full_path)
    return movie_files

# Choose the best quality (based on file size)
def choose_best(files):
    return max(files, key=lambda f: os.path.getsize(f))

def main():
    if len(sys.argv) < 2:
        print("Usage: dedupe_movies.py <folder1> <folder2> ...")
        sys.exit(1)

    folders = sys.argv[1:]
    movie_files = find_movies(folders)

    for title, files in movie_files.items():
        if len(files) == 1:
            print(f"✅ {Path(files[0]).name} — OK")
        else:
            print(f"\n🔁 Duplicate found for: {title}")
            best = choose_best(files)
            print(f"   🏆 Keeping: {Path(best).name}")

            for f in files:
                if f != best:
                    print(f"   🗑️  Deleting lower quality: {Path(f).name}")
                    # Uncomment the next line to delete files
                    os.remove(f)

if __name__ == "__main__":
    main()
