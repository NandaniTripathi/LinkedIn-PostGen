import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        # Load JSON using UTF-8
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        # Clean invalid Unicode characters
        def clean_unicode(obj):
            if isinstance(obj, str):
                return obj.encode("utf-8", errors="replace").decode("utf-8")
            elif isinstance(obj, list):
                return [clean_unicode(item) for item in obj]
            elif isinstance(obj, dict):
                return {
                    key: clean_unicode(value)
                    for key, value in obj.items()
                }
            return obj

        posts = clean_unicode(posts)

        # Convert JSON into DataFrame
        self.df = pd.json_normalize(posts)

        # Categorize post length
        self.df["length"] = self.df["line_count"].apply(
            self.categorize_length
        )

        # Collect unique tags
        all_tags = self.df["tags"].apply(lambda x: x).sum()
        self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        # Tier 1: exact match on tag + language + length
        df_filtered = self.df[
            (self.df["tags"].apply(lambda tags: tag in tags))
            & (self.df["language"] == language)
            & (self.df["length"] == length)
        ]
        if len(df_filtered) > 0:
            return df_filtered.to_dict(orient="records"), "exact"

        # Tier 2: drop length, keep tag + language
        df_filtered = self.df[
            (self.df["tags"].apply(lambda tags: tag in tags))
            & (self.df["language"] == language)
        ]
        if len(df_filtered) > 0:
            return df_filtered.to_dict(orient="records"), "tag_language"

        # Tier 3: drop language too, match tag only
        df_filtered = self.df[
            self.df["tags"].apply(lambda tags: tag in tags)
        ]
        if len(df_filtered) > 0:
            return df_filtered.to_dict(orient="records"), "tag_only"

        # Tier 4: nothing matches this tag at all
        return [], "none"

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()

    posts, tier = fs.get_filtered_posts(
        "Medium",
        "Hinglish",
        "Job Search"
    )

    print(f"match tier: {tier}")
    print(posts)
