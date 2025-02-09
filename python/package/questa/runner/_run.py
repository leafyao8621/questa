import numpy

import questa.runner._base

def run(
    mode: str,
    s: numpy.ndarray,
    warmup: int,
    n_iter: int,
    n: int,
    seed: int,
    n_thread: int):
    """_summary_

    Args:
        mode (str): _description_
        s (numpy.ndarray): _description_
        warmup (int): _description_
        n_iter (int): _description_
        n (int): _description_
        seed (int): _description_
        n_thread (int): _description_

    Returns:
        _type_: _description_
    """
    out = numpy.empty((len(s), n_iter), dtype=numpy.int32)
    questa.runner._base.run(
        mode,
        s,
        len(s),
        warmup,
        n_iter,
        n,
        seed,
        n_thread,
        out
    )
    return out
