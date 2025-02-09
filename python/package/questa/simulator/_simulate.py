import numpy

import questa.simulator._base

def simulate(mode: str, s: float, warmup: int, n_iter: int, n: int, seed: int):
    """_summary_

    Args:
        mode (str): _description_
        s (float): _description_
        warmup (int): _description_
        n_iter (int): _description_
        n (int): _description_
        seed (int): _description_

    Returns:
        _type_: _description_
    """
    out = numpy.empty(n_iter, dtype=numpy.int32)
    questa.simulator._base.simulate(
        mode, s, warmup, n_iter, n, seed, out
    )
    return out
