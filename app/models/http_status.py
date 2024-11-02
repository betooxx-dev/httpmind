from dataclasses import dataclass
from typing import List

@dataclass
class HttpStatus:
    code: str
    title: str
    type: str
    description: str
    solutions: List[str]
    severity: str

    def to_dict(self):
        return {
            "code": self.code,
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "solutions": self.solutions,
            "severity": self.severity
        }

    @staticmethod
    def from_dict(data: dict, code: str):
        return HttpStatus(
            code=code,
            title=data.get("title", ""),
            type=data.get("type", ""),
            description=data.get("description", ""),
            solutions=data.get("solutions", []),
            severity=data.get("severity", "")
        )