from dataclasses import dataclass


@dataclass
class Candidate:
    name: str
    role: str
    experience_level: str
    skills: list[str]