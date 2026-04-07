import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

with open("personas/personas_auto.json") as f:
    personas = json.load(f)

specifications = []

acceptance_criteria_map = {
    'G1': 'The system provides calming and relaxing features.',
    'G2': 'The system provides sleep guidance and monitoring features.',
    'G3': 'The system provides a simple and intuitive navigation interface.',
    'G4': 'The system provides transparent and affordable pricing options.',
    'G5': 'The system provides personalized recommendations and feedback.'
}

for i, persona in enumerate(personas):
    requirement_id = f"FR_auto_{i + 1}"

    description = f"The system shall provide {acceptance_criteria_map[persona['derived_from_group']]}"

    source_persona = persona['name']
    traceability = f"Derived from review group {persona['derived_from_group']}"

    given_clause = f"Given the user's current mental state"
    when_clause = f"When the system processes their request"
    then_clause = f"Then {acceptance_criteria_map[persona['derived_from_group']]}"

    acceptance_criteria = f"Acceptance Criteria: [{given_clause}, {when_clause}, {then_clause}]"

    specifications.append({
        "requirement_id": requirement_id,
        "description": description,
        "source_persona": source_persona,
        "traceability": traceability,
        "acceptance_criteria": acceptance_criteria
    })

with open("spec/spec_auto.md", "w", encoding="utf-8") as f:
    for spec in specifications:
        f.write(f"# Requirement ID: {spec['requirement_id']}\n")
        f.write(f"- Description: {spec['description']}\n")
        f.write(f"- Source Persona: {spec['source_persona']}\n")
        f.write(f"- Traceability: {spec['traceability']}\n")
        f.write(f"{spec['acceptance_criteria']}\n\n")