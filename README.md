# 🧹 dedupe_movies.py

A Python script to scan multiple folders for duplicate movie files and automatically keep the highest quality version (based on file size). Ideal for organizing large media libraries and removing redundant video files.

---

## 📦 Features

- Supports common video formats: `.mkv`, `.mp4`, `.avi`, `.mov`
- Detects duplicates using smart title matching (ignores resolution/encoding tags)
- Keeps only the largest file (assumed best quality) among duplicates
- Logs actions clearly and supports safe dry runs
- Easy to customize and extend

---

## 🚀 Usage

```bash
python3 dedupe_movies.py <folder1> <folder2> ...
