from dotenv import load_dotenv
import os

load_dotenv()

from dataclasses import dataclass
from typing import List

@dataclass
class CSRField:
    name: str
    description: str

CSR_SCHEMA: List[CSRField] = [
    CSRField("trial_id", "ClinicalTrials.gov ID or internal trial identifier"),
    CSRField("title", "Full title of the clinical study"),
    CSRField("indication", "Disease or condition being studied"),
    CSRField("phase", "Study phase (e.g., Phase I, II, III)"),
    CSRField("sample_size", "Total participants randomized or analyzed"),
    CSRField("arms_and_treatments", "Study arms and treatments/doses"),
    CSRField("primary_endpoint", "Primary endpoint definition"),
    CSRField("key_results", "High-level efficacy results"),
    CSRField("serious_adverse_events", "Serious adverse events"),
    CSRField("sponsor", "Sponsor of the trial"),
    CSRField("location", "Trial locations / countries"),
]
