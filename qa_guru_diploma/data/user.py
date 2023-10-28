from dataclasses import dataclass


@dataclass
class User:
    """
    Test user class
    """

    full_name: str
    phone: str
    email: str
    password: str

