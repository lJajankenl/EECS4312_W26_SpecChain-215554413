import json

with open("data/review_groups_auto.json") as f:
    review_groups = json.load(f)

personas = []

for group_name, reviews in review_groups.items():
    common_themes = []
    for review in reviews:
        # Simple keyword extraction
        keywords = [word[:20] for word in review.split() if len(word) > 3]
        common_themes.extend(keywords)

    # Get unique keywords
    common_themes = list(set(common_themes))

    persona = {
        "name": f"{group_name} Persona",
        "description": f"User with interests in {', '.join(common_themes)}",
        "derived_from_group": group_name,
        "goals": [],
        "pain_points": [],
        "context": [],
        "constraints": [],
        "evidence_reviews": reviews
    }
    personas.append(persona)

# Save personas
with open("personas/personas_auto.json", "w") as f:
    json.dump(personas, f, indent=4)