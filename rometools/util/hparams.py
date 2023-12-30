import json
from dataclasses import dataclass
import os


@dataclass
class HyperParams:
    """
    Simple wrapper to store hyperparameters for Python-based rewriting methods.
    """

    @classmethod
    def from_json(cls, fpath):
        MODULE_FOLDER = os.path.join(os.path.dirname(__file__), "..")
        print("MODULE_FOLDER", MODULE_FOLDER)
        with open(os.path.join(MODULE_FOLDER + "/", fpath), "r") as f:
            data = json.load(f)

        return cls(**data)
