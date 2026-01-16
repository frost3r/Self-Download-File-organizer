from rules import RULES

#classifies filename based on keywords
def classify(filename: str) -> str:

    name = filename.lower()
    best_category = "Unsorted"
    best_score = 0

    for category, data in RULES.items():
        score = 0
        for keyword in data["keywords"]:
            if keyword in name:
                score += 1

        if score > best_score:
            best_score = score
            best_category = category

    return best_category


def organize_model(filenames):
   
    organization = {}

    for filename in filenames:
        category = classify(filename)
        if category not in organization:
            organization[category] = []
        organization[category].append(filename)

    return organization


if __name__ == "__main__":
    from sample_files import SAMPLE_FILES

    result = organize_model(SAMPLE_FILES)

    for category, files in result.items():
        print(f"\n{category}:")
        for f in files:
            print(f"  - {f}")

