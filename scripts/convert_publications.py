from datetime import datetime, timedelta
import json
import sys


header_ja = """---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "業績 (過去5年分)"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2020-02-17T18:32:18+09:00
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
---
"""  # noqa: E501


header_en = """---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Publications (last 5 years)"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2020-02-17T18:32:18+09:00
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
---
"""  # noqa: E501


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


def read_json(input_fname):
    publications = []

    with open(input_fname) as f:
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


def write_markdown(output_fname, publications, categories, header):
    with open(output_fname, "w") as f:
        f.write(header)

        for key, category in categories.items():
            filtered = [p for p in publications if p["category"] ==
                        key and p["date"] > datetime.now() -
                        timedelta(days=365) * 5]
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
    input_fname = sys.argv[1]
    output_fname_ja = sys.argv[2]
    output_fname_en = sys.argv[3]

    publications = read_json(input_fname)

    write_markdown(output_fname_ja, publications, categories_ja, header_ja)
    write_markdown(output_fname_en, publications, categories_en, header_en)


if __name__ == "__main__":
    main()
