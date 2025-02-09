#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

#include "simulator/simulator.h"

#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))

struct module_state {
    PyObject* error;
};

PyDoc_STRVAR(simulate__doc__,
    "simulate(mode, s, warmup, n_iter, n, seed, total_queue_length)\n\n"
    "Simulates\n\n"
    "Arguments:\n"
    "        mode {str} -- mode\n"
    "        s {float} -- s\n"
    "        warmup {int} -- warmup\n"
    "        n_iter {int} -- tail\n"
    "        n {int} -- n\n"
    "        seed {int} -- seed\n"
    "        total_queue_length {numpy.ndarray} -- output\n"
);

static PyObject* simulate(PyObject* self, PyObject* args) {
    const char *mode;
    double s;
    size_t warmup, n_iter, n;
    long seed;
    PyObject *total_queue_length;
    if (
        !PyArg_ParseTuple(
            args, "sdllllO!",
            &mode,
            &s,
            &warmup,
            &n_iter,
            &n,
            &seed,
            &PyArray_Type,
            &total_queue_length)) {
        return NULL;
    }
    try {
        QUESTA::Simulator simulator;
        simulator.init(n, seed);
        if (!strcmp(mode, "QUEUE_LENGTH")) {
            simulator(
                QUESTA::Simulator::Mode::QUEUE_LENGTH,
                s,
                warmup,
                n_iter,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "MAX_MINUS_QUEUE_LENGTH")) {
            simulator(
                QUESTA::Simulator::Mode::MAX_MINUS_QUEUE_LENGTH,
                s,
                warmup,
                n_iter,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "MAX_PLUS_QUEUE_LENGTH")) {
            simulator(
                QUESTA::Simulator::Mode::MAX_PLUS_QUEUE_LENGTH,
                s,
                warmup,
                n_iter,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "LOG_MAX_PLUS_QUEUE_LENGTH")) {
            simulator(
                QUESTA::Simulator::Mode::LOG_MAX_PLUS_QUEUE_LENGTH,
                s,
                warmup,
                n_iter,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else {
            PyErr_SetString(PyExc_RuntimeError, "NOT IMPLEMENTED");
            return NULL;
        }
    } catch (QUESTA::Simulator::Err err) {
        switch (err) {
        case QUESTA::Simulator::Err::OUT_OF_MEMORY:
            PyErr_SetString(PyExc_RuntimeError, "OUT OF MEMORY");
            return NULL;
        case QUESTA::Simulator::Err::NOT_IMPLEMENTED:
            PyErr_SetString(PyExc_RuntimeError, "NOT IMPLEMENTED");
            return NULL;
        }
    }
    Py_RETURN_NONE;
}

static PyMethodDef _base_methods[] = {
    {"simulate", (PyCFunction)simulate, METH_VARARGS, simulate__doc__},
    {0}
};

static int _base_traverse(PyObject *m, visitproc visit, void *arg) {
    Py_VISIT(GETSTATE(m)->error);
    return 0;
}

static int _base_clear(PyObject *m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "questa.simulator._base",
    NULL,
    sizeof(struct module_state),
    _base_methods,
    NULL,
    _base_traverse,
    _base_clear,
    NULL
};

PyMODINIT_FUNC PyInit__base(void) {
    PyObject *module = PyModule_Create(&moduledef);
    if (!module) return NULL;
    import_array();
    return module;
}
