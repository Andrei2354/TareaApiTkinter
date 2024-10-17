from dataclasses import dataclass
@dataclass
class Reviews:
    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str