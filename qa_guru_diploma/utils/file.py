import qa_guru_diploma
from pathlib import Path


def relative_from_root(relative_path: str):
    return (
        Path(qa_guru_diploma.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )