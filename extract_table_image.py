import os

from gmft.auto import AutoFormatConfig, AutoTableDetector
from gmft_pymupdf import PyMuPDFDocument


def setup_config(model_path="microsoft/table-transformer-detection", threshold=0.8):
    detector_config_format = AutoFormatConfig()

    detector_config_format.detector_path = model_path

    detector_config_format.detector_base_threshold = threshold

    detector = AutoTableDetector(config=detector_config_format)

    return detector


def convert_table2img(pdf_path, detector):
    doc = PyMuPDFDocument(pdf_path)
    tables = []
    for page in doc:
        tables += detector.extract(page)

        return tables


if __name__ == "__main__":
    # In this example I use the default, but you should change the detector path to your finetuned model path
    # change the detection threshold as desired; in this case we usually want a high threshold
    model_path = "microsoft/table-transformer-detection"
    detector = setup_config(model_path, threshold=0.8)

    # get the list of documents to detect tables
    file_path = r"C:\Users\andyp\projects\label-studio\data"
    filenames = os.listdir(file_path)
    output_path = r"C:\Users\andyp\projects\label-studio\data-table-images"

    for idx, f in enumerate(filenames):
        base_name = os.path.splitext(os.path.basename(f))[0]

        tables = convert_table2img(os.path.join(file_path, f), detector)

        for i, t in enumerate(tables):
            filename = f"{base_name}_table_{i}.png"
            full_path = os.path.join(output_path, filename)

            t.image(dpi=300).save(full_path)
