from dataclasses import dataclass, field


@dataclass
class ResumeProfile:
    education: list[str] = field(default_factory=list)
    experience: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)