import os
from pathlib import Path

from pdf2image import convert_from_path


def convert_pdf_to_png(pdf_path, output_folder, dpi=300):
    # extract base filename without extension
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # check if any PNG file in the output folder already exists
    existing_images = list(Path(output_folder).glob("*.png"))
    for img in existing_images:
        if base_name in img.stem:
            print(f"Images for {base_name} already exist, skipping conversion")
            return

    # convert PDF to list of PIL images
    # add the poppler_path in the argument if you need to manually define the poppler_path
    pages = convert_from_path(pdf_path, dpi=dpi)

    # ensure output folder exists, if not create
    os.makedirs(output_folder, exist_ok=True)

    # extract the base filename without the extension
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    for i, page in enumerate(pages):
        output_path = os.path.join(output_folder, f"{base_name}_page_{i + 1}.png")
        page.save(output_path, "PNG")
        print(f"Saved {output_path}")


if __name__ == "__main__":
    # change the input_folder and output_folder to your directory accordingly
    input_folder = r"C:\Users\andyp\projects\label-studio\input"
    output_folder = r"C:\Users\andyp\projects\label-studio\data"
    pdf_files = list(Path(input_folder).rglob("*.pdf"))
    print("Total PDF files found: ", len(pdf_files))
    for idx, pdf_file in enumerate(pdf_files):
        convert_pdf_to_png(pdf_file, output_folder, dpi=300)
