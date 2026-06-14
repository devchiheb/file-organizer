# Python File Organizer

A lightweight Python script that automatically organizes files into categorized folders based on their file extensions.

## Features

- Organizes files by type
- Creates folders automatically
- Supports common file formats
- Simple and easy to use
- Lightweight with no external dependencies

## Folder Structure

Before:
Downloads/
├── photo.jpg
├── document.pdf
├── music.mp3
└── video.mp4


After:
Downloads/
├── Images/
│ └── photo.jpg
├── Documents/
│ └── document.pdf
├── Audio/
│ └── music.mp3
└── Videos/
└── video.mp4

## Supported Categories

| Category | Extensions |
|-----------|------------|
| Images | .jpg, .jpeg, .png, .gif, .webp |
| Documents | .pdf, .docx, .txt, .pptx |
| Audio | .mp3, .wav, .flac |
| Videos | .mp4, .mkv, .avi |
| Archives | .zip, .rar, .7z |
| Code | .py, .js, .html, .css, .java |

## Installation

Clone the repository:

```bash
git clone https://github.com/devchiheb/file-organizer.git
cd python-file-organizer

Usage
python main.py
