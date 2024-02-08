from dataclasses import dataclass


@dataclass
class User:
    full_name: str = None
    email: str = None
    current_address: str = None
