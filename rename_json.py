import json
import re


def rename_json():
    # assuming your file is `result.json`
    with open("result.json", "r") as file:
        data = json.load(file)

    # pattern match from images\...__data%5C
    pattern = r"images\\.*?__data%5C"

    # replacement path - change this to the directoy that contains your images
    replacement_path = r"C:/Users/andyp/projects/label-studio/data/"

    for image in data["images"]:
        original = image["file_name"]
        image["file_name"] = re.sub(pattern, replacement_path, original)

    # save to new file
    with open("custom.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    rename_json()
