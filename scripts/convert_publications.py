from datetime import datetime, timedelta
import json
import sys
import os
import argparse
from pathlib import Path

def create_header(title, include_link_to_all):
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')

    header = f"""---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "{title}"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: {current_datetime}
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
caption: ""
focal_point: ""
preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---"""  # noqa: E501
    
    if include_link_to_all:
        header += "\n\n[All publications](all)\n"

    return header


categories_ja = {
    "学術論文誌": "学術論文誌",
    "国際会議等発表": "国際会議論文",
    "著書": "著書",
    "国内学会研究会・シンポジウム等発表": "国内学会研究会・シンポジウム等",
    "国内学会大会等発表": "国内学会大会等",
    "解説・総説": "解説・総説",
    "表彰・受賞": "表彰・受賞",
    "その他": "その他"
}


categories_en = {
    "学術論文誌": "Journal",
    "国際会議等発表": "International Conference",
    "著書": "Book",
    "国内学会研究会・シンポジウム等発表": "Domestic Conference and Symposium",
    "国内学会大会等発表": "Annual Domestic Meeting",
    "解説・総説": "Survey",
    "表彰・受賞": "Award",
    "その他": "Misc"
}


def read_json(input_file):
    publications = []

    with open(input_file) as f:
        j = json.load(f)

        print("Converting", j["list_item"]["items_count"], "publications")

        for publication in j["list_item"]["items"]:
            item = {}
            item["authors"] = ", ".join([author["@name"] for author in
                                         publication["dc:creator"]])
            item["title"] = "\"" + publication["dc:title"]["@value"] + "\""
            item["booktitle"] = publication["prism:sourceName"]["@value"] or \
                publication["prism:sourceName2"]["@value"]
            item["category"] = publication["dc:category"]["@value"]
            item["doi"] = publication["prism:doi"]

            date_str = publication["prism:publicationDate"]
            try:
                item["date"] = datetime.strptime(date_str, "%Y/%m/%d")
            except ValueError:
                item["date"] = datetime.strptime(date_str, "%Y/%m")

            publications.append(item)

    return publications


def write_markdown(output_path, publications, categories, header, recent_only):
    with open(output_path, "w") as f:
        f.write(header)

        for key, category in categories.items():
            if recent_only:
                filtered = [p for p in publications if p["category"] == key and 
                            p["date"] > datetime.now() - timedelta(days=365) * 5]
            else:
                filtered = [p for p in publications if p["category"] == key]
            filtered.sort(key=lambda p: p["date"], reverse=True)

            if not filtered:
                print("Skipping category", category)
                continue

            print(len(filtered), "items found for category", category)

            f.write("\n## " + category + "\n\n")

            for item in filtered:
                f.write("1. " + ", ".join([item["authors"], item["title"],
                                           item["booktitle"],
                                           item["date"].strftime("%b. %Y")])
                        + ".")
                if item["doi"]:
                    f.write(" [doi:{}](https://doi.org/{})".format(item["doi"], item["doi"]))
                f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Convert publications from JSON to markdown")
    parser.add_argument('input_file', type=Path, help='Input JSON file')
    parser.add_argument('content_dir', type=Path, help='Path to the content directory')
    args = parser.parse_args()

    if not args.input_file.is_file():
        print(f"Error: The input file '{args.input_file}' does not exist.")
        sys.exit(1)
    
    if not args.content_dir.is_dir():
        print(f"Error: The output directory '{args.output_dir}' does not exist.")
        sys.exit(1)

    input_file = args.input_file
    content_dir = args.content_dir
    output_file_ja_5year = content_dir / "ja" / "publications" / "_index.md"
    output_file_ja_all = content_dir / "ja" / "publications" / "all" / "_index.md"
    output_file_en_5year = content_dir / "en" / "publications" / "_index.md"
    output_file_en_all = content_dir / "en" / "publications" / "all" / "_index.md"

    publications = read_json(input_file)

    header_ja_5year = create_header("研究業績（過去5年分）", include_link_to_all=True)
    header_ja_all = create_header("全ての研究業績", include_link_to_all=False)
    header_en_5year = create_header("Publications (last 5 years)", include_link_to_all=True)
    header_en_all = create_header("All Publications", include_link_to_all=False)

    write_markdown(output_file_ja_5year, publications, categories_ja, header_ja_5year, recent_only=True)
    write_markdown(output_file_ja_all, publications, categories_ja, header_ja_all, recent_only=False)
    write_markdown(output_file_en_5year, publications, categories_en, header_en_5year, recent_only=True)
    write_markdown(output_file_en_all, publications, categories_en, header_en_all, recent_only=False)

if __name__ == "__main__":
    main()
