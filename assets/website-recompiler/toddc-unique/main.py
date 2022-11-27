import pandas as pd
import re

# 0 - DEFINE CONSTS =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
ITEMS_CSV = "../../destiny-dc/items/unique/csv/unique.csv"
TAGS_CSV = "./data/tags.csv"
N_ROWS_PER_ENTRY = 2
N_START = 898
OUT_MD = "../../../projects/destiny-dc/items/unique.md"

# for markdown
TEMPLATE = """
## Unique: {content0}

{content1}

![](../../../assets/destiny-dc/items/unique/img/{item_id}.png)  
"""
SEPARATOR = "\n---\n"


# regexes
RE_CONTENT = re.compile(".*?\)(.*)") # matches the cell text content, ex: [Sign_Apple_Gel]Apple Gel[END]    
RE_TAGS = re.compile("(\[.*?\])") # matches anything between square brackets, ex: [Sign_Apple_Gel] and [END]

def create_desc_from_raw(row: pd.Series, tags_df: pd.DataFrame) -> str:
    # 1 - extract content
    raw_en = row["English"].replace('\n', ' ')
    content = RE_CONTENT.search(raw_en).group(1).strip()
    
    # 2 - replace tags
    content = content.replace("[LINE]", '')
    tags = RE_TAGS.findall(content)

    for t in tags:
        replacement = tags_df.loc[tags_df["tags"] == t].iloc['comments'] if t in tags_df["tags"] else ""
        content = content.replace(t, replacement)

    return content

# main
if __name__ == "__main__":
    # 1 - LOAD DATA =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    items_df: pd.DataFrame = pd.read_csv(ITEMS_CSV)
    tags_df: pd.DataFrame = pd.read_csv(TAGS_CSV)

    # 2 - MAKE TEXT PRETTY =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    items_df["content"] = items_df.apply(lambda row: create_desc_from_raw(row, tags_df), axis=1)
    
    # 3 - ADD CONTENT TYPE AND ITEM ID =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    items_df.insert(0, "content_type", ["title" if idx % N_ROWS_PER_ENTRY == 0 else "description" for idx in range(0, len(items_df))])
    items_df.insert(0, "item_id", [(idx // N_ROWS_PER_ENTRY) + N_START for idx in range(0, len(items_df))])

    # 4 - COLLAPSE DATAFRAME =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    items_df = items_df[["item_id", "content"]]
    s = items_df.groupby(["item_id"]).cumcount()

    out_df = items_df.set_index(["item_id", s], drop=True).unstack().sort_index(level=1, axis=1)
    out_df.columns = [f'{x}{y}' for x, y in out_df.columns]
    out_df.insert(0, "item_id", out_df.index)

    # 5 - MARKDOWN =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    all_entries = [TEMPLATE.format(**row) for _, row in out_df.iterrows()]
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(SEPARATOR.join(all_entries))

    print("DONE :)")
    
    

