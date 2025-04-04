from setuptools import setup, Extension
import numpy

simulator_base =\
    Extension(
        'questa.simulator._base',
        sources=[
            "questa/simulator/src/simulator/simulator.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_max_weight.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_max_size.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_msmw.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_msmw_log.cpp",
            "questa/simulator/src/util/mrg32k3a.cpp",
            "questa/simulator/src/main.cpp"
        ],
        include_dirs=[numpy.get_include()],
        libraries=["lemon"]
    )

runner_base =\
    Extension(
        'questa.runner._base',
        sources=[
            "questa/runner/src/simulator/simulator.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_max_weight.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_max_size.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_msmw.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_msmw_log.cpp",
            "questa/runner/src/runner/runner.cpp",
            "questa/runner/src/main.cpp"
        ],
        include_dirs=[numpy.get_include()],
        libraries=["lemon"],
        extra_link_args=["-pthread"]
    )

setup(
    name="questa",
    version="0.1",
    packages=[
        "questa.simulator",
        "questa.runner",
        "questa.plotter",
    ],
    ext_modules=[
        simulator_base,
        runner_base
    ]
)
