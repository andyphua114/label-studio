# Label Studio Utilities — Prep, Convert & Extract

Helper scripts to prepare datasets, convert documents to images, and extract table crops for use with Label Studio. Use these utilities to clean up exported paths, turn PDFs into page images, and extract table regions for downstream model training or manual annotation.

```text
label-studio/
├── data/                   # (sample) converted page image from pdf
├── data-table-images/      # (sample) saved table crops extracted from pages
├── input/                  # (sample) PDF document
├── custom.json             # Example of labeled data
├── extract_table_image.py  # Crop table regions from page images using bboxes
├── image_converter.py      # Convert PDFs to images
├── rename_json.py          # Fix/normalize paths & filenames inside JSON
├── requirements.txt        # Python dependencies
├── result.json             # Sample JSON (e.g., post-processed output) after using rename_json.py
└── .gitignore
```

## Utilities

### 1. Convert documents to images

Use `image_converter.py` to generate page images from PDFs (before importing to Label Studio or running downstream detection/recognition).

### 2. Fix/normalize JSON paths

Use `rename_json.py` to correct mismatched Windows directory paths, URL-encoded strings, or move images between folders while keeping JSON references consistent.

### 3. Extract table crops

Use `extract_table_image.py` to read page-level images and saves cropped table images into data-table-images/ for quick inspection or model training.

## Blog Article

You can find a guide for implementation at the following link: [How to Annotate Tables in Label Studio for Table Transformer Fine-Tuning](https://medium.com/@andyphuawc/how-to-annotate-tables-in-label-studio-for-table-transformer-fine-tuning-e19ff651db01#eb1d)

## Notes

Written based on a Windows machine, so do take note when working with directory path.
