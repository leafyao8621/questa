from setuptools import setup, Extension
import numpy

simulator_base =\
    Extension(
        'questa.simulator._base',
        sources=[
            "questa/simulator/src/simulator/simulator.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_queue_length.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_max_minus_queue_length.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_max_plus_queue_length.cpp",
            "questa/simulator/src/simulator/simulator_run/simulator_run_log_max_plus_queue_length.cpp",
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
            "questa/runner/src/simulator/simulator_run/simulator_run_queue_length.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_max_minus_queue_length.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_max_plus_queue_length.cpp",
            "questa/runner/src/simulator/simulator_run/simulator_run_log_max_plus_queue_length.cpp",
            "questa/runner/src/runner/runner.cpp",
            "questa/runner/src/util/mrg32k3a.cpp",
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
    ],
    ext_modules=[
        simulator_base,
        runner_base
    ]
)
