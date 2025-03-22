import matplotlib.pyplot
import numpy
import matplotlib

def plot(
    max_weight: numpy.ndarray,
    max_size: numpy.ndarray,
    msmw: numpy.ndarray,
    msmw_log: numpy.ndarray,
    n: int,
    ylim: int,
    out: str | None):
    """_summary_

    Args:
        max_weight (numpy.ndarray): _description_
        max_size (numpy.ndarray): _description_
        msmw (numpy.ndarray): _description_
        msmw_log (numpy.ndarray): _description_
        n (int): _description_
        ylim (int): _description_
        out (str | None): _description_
    """
    matplotlib.pyplot.plot(
        max_weight[:, 0],
        max_weight[:, 1],
        label="Max Weight",
        color="black"
    )
    # matplotlib.pyplot.plot(
    #     max_weight[9:20, 0],
    #     max_weight[9:20, 2],
    #     linestyle='--',
    #     label="Max Weight 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     max_weight[9:20, 0],
    #     max_weight[9:20, 3],
    #     linestyle='--',
    #     label="Max Weight 95% CI UB"
    # )
    matplotlib.pyplot.plot(
        max_size[:, 0],
        max_size[:, 1],
        label="Max Size",
        linestyle="--",
        color="purple"
    )
    # matplotlib.pyplot.plot(
    #     max_size[9:20, 0],
    #     max_size[9:20, 2],
    #     linestyle='--',
    #     label="Max Size 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     max_size[9:20, 0],
    #     max_size[9:20, 3],
    #     linestyle='--',
    #     label="Max Size 95% CI UB"
    # )
    matplotlib.pyplot.plot(
        msmw[:, 0],
        msmw[:, 1],
        label="MSMW",
        linestyle="-.",
        color="green"
    )
    # matplotlib.pyplot.plot(
    #     msmw[9:20, 0],
    #     msmw[9:20, 2],
    #     linestyle='--',
    #     label="MSMW 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw[9:20, 0],
    #     msmw[9:20, 3],
    #     linestyle='--',
    #     label="MSMW 95% CI UB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[:, 0],
    #     msmw_log[:, 1],
    #     label="MSMW Log"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[9:20, 0],
    #     msmw_log[9:20, 2],
    #     linestyle='--',
    #     label="MSMW Log 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[9:20, 0],
    #     msmw_log[9:20, 3],
    #     linestyle='--',
    #     label="MSMW Log 95% CI UB"
    # )
    matplotlib.pyplot.plot(
        max_weight[:, 0],
        (
            2 * n * max_weight[:, 0] -\
            (n + 1) * max_weight[:, 0] ** 2
        ) /\
        (2 * (1 - max_weight[:, 0])),
        linestyle='dotted',
        label="Universal Lower Bound",
        color="red"
    )
    matplotlib.pyplot.title(
        r"$E\left[\sum_{i, j}{Q_{i, j}}\right]$ vs Traffic Intensity",
        fontsize=16
    )
    matplotlib.pyplot.xlabel(
        r"Traffic Intensity ($\rho$)",
        fontsize=16
    )
    matplotlib.pyplot.ylabel(
        r"$E\left[\sum_{i, j}{Q_{i, j}}\right]$",
        fontsize=16
    )
    matplotlib.pyplot.ylim(ylim)
    matplotlib.pyplot.subplots_adjust(
        left=0.18, right=0.97, top=0.9, bottom=0.1
    )
    matplotlib.pyplot.grid()
    matplotlib.pyplot.legend(fontsize=16)
    if (out):
        matplotlib.pyplot.savefig(out)
        matplotlib.pyplot.clf()

def plot_scaled(
    max_weight: numpy.ndarray,
    max_size: numpy.ndarray,
    msmw: numpy.ndarray,
    msmw_log: numpy.ndarray,
    n: int,
    xlim: int,
    out: str | None):
    """_summary_

    Args:
        max_weight (numpy.ndarray): _description_
        max_size (numpy.ndarray): _description_
        msmw (numpy.ndarray): _description_
        msmw_log (numpy.ndarray): _description_
        n (int): _description_
        xlim (int): _description_
        out (str | None): _description_
    """
    matplotlib.pyplot.plot(
        max_weight[:, 0],
        (1 - max_weight[:, 0]) * max_weight[:, 1],
        label="Max Weight",
        color="black"
    )
    # matplotlib.pyplot.plot(
    #     max_weight[:, 0],
    #     (1 - max_weight[:, 0]) * max_weight[:, 2],
    #     linestyle='--',
    #     label="Max Weight 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     max_weight[:, 0],
    #     (1 - max_weight[:, 0]) * max_weight[:, 3],
    #     linestyle='--',
    #     label="Max Weight 95% CI UB"
    # )
    # matplotlib.pyplot.plot(
    #     max_size[:, 0],
    #     (1 - max_size[:, 0]) * max_size[:, 1],
    #     label="Max Size",
    #     linestyle="--"
    # )
    # matplotlib.pyplot.plot(
    #     max_size[:, 0],
    #     (1 - max_size[:, 0]) * max_size[:, 2],
    #     linestyle='--',
    #     label="Max Size 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     max_size[:, 0],
    #     (1 - max_size[:, 0]) * max_size[:, 3],
    #     linestyle='--',
    #     label="Max Size 95% CI UB"
    # )
    matplotlib.pyplot.plot(
        msmw[:, 0],
        (1 - msmw[:, 0]) * msmw[:, 1],
        label="MSMW",
        linestyle="-.",
        color="green"
    )
    # matplotlib.pyplot.plot(
    #     msmw[:, 0],
    #     (1 - msmw[:, 0]) * msmw[:, 2],
    #     linestyle='--',
    #     label="MSMW 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw[:, 0],
    #     (1 - msmw[:, 0]) * msmw[:, 3],
    #     linestyle='--',
    #     label="MSMW 95% CI UB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[:, 0],
    #     (1 - msmw_log[:, 0]) * msmw_log[:, 1],
    #     label="MSMW Log"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[:, 0],
    #     (1 - msmw_log[:, 0]) * msmw_log[:, 2],
    #     linestyle='--',
    #     label="MSMW Log 95% CI LB"
    # )
    # matplotlib.pyplot.plot(
    #     msmw_log[:, 0],
    #     (1 - msmw_log[:, 0]) * msmw_log[:, 3],
    #     linestyle='--',
    #     label="MSMW Log 95% CI UB"
    # )
    matplotlib.pyplot.plot(
        max_weight[:, 0],
        (
            2 * n * max_weight[:, 0] -\
            (n + 1) * max_weight[:, 0] ** 2
        ) /\
        2,
        linestyle='dotted',
        label="Universal Lower Bound",
        color="red"
    )
    matplotlib.pyplot.title(
        r"$(1 - \rho)E\left[\sum_{i, j}{Q_{i, j}}\right]$ vs Traffic Intensity",
        fontsize=16
    )
    matplotlib.pyplot.xlabel(
        r"Traffic Intensity ($\rho$)",
        fontsize=16
    )
    matplotlib.pyplot.ylabel(
        r"$(1 - \rho)E\left[\sum_{i, j}{Q_{i, j}}\right]$",
        fontsize=16
    )
    matplotlib.pyplot.xlim(xlim)
    matplotlib.pyplot.subplots_adjust(
        left=0.18, right=0.97, top=0.9, bottom=0.1
    )
    matplotlib.pyplot.grid()
    matplotlib.pyplot.legend(fontsize=16)
    if (out):
        matplotlib.pyplot.savefig(out)
        matplotlib.pyplot.clf()
