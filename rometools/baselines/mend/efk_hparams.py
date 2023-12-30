from dataclasses import dataclass

from rometools.util.hparams import HyperParams


@dataclass
class EFKHyperParams(HyperParams):
    lr_scale: float
    n_toks: int
    model_name: str
    counterfact: bool
    zsre: bool
