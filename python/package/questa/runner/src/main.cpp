#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

#include "runner/runner.h"

#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))

struct module_state {
    PyObject* error;
};

PyDoc_STRVAR(run__doc__,
    "run(mode, s, s_len, warmup, n_iter, n, seed, n_thread, total_queue_length)\n\n"
    "runs\n\n"
    "Arguments:\n"
    "        mode {str} -- mode\n"
    "        s {numpy.ndaray} -- s\n"
    "        s_len {numpy.ndaray} -- s_len\n"
    "        warmup {int} -- warmup\n"
    "        n_iter {int} -- tail\n"
    "        n {int} -- n\n"
    "        seed {int} -- seed\n"
    "        n_thread {int} -- n_thread\n"
    "        total_queue_length {numpy.ndarray} -- output\n"
);

static PyObject* run(PyObject* self, PyObject* args) {
    const char *mode;
    size_t s_len, warmup, n_iter, n, n_thread;
    long seed;
    PyObject *s, *total_queue_length;
    if (
        !PyArg_ParseTuple(
            args, "sO!llllllO!",
            &mode,
            &PyArray_Type,
            &s,
            &s_len,
            &warmup,
            &n_iter,
            &n,
            &seed,
            &n_thread,
            &PyArray_Type,
            &total_queue_length)) {
        return NULL;
    }
    try {
        QUESTA::Runner runner(n_thread);
        if (!strcmp(mode, "MAX_WEIGHT")) {
            runner(
                QUESTA::Simulator::Mode::MAX_WEIGHT,
                (double*)PyArray_DATA((PyArrayObject*)s),
                s_len,
                warmup,
                n_iter,
                n,
                seed,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "MAX_SIZE")) {
            runner(
                QUESTA::Simulator::Mode::MAX_SIZE,
                (double*)PyArray_DATA((PyArrayObject*)s),
                s_len,
                warmup,
                n_iter,
                n,
                seed,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "MSMW")) {
            runner(
                QUESTA::Simulator::Mode::MSMW,
                (double*)PyArray_DATA((PyArrayObject*)s),
                s_len,
                warmup,
                n_iter,
                n,
                seed,
                (int*)PyArray_DATA((PyArrayObject*)total_queue_length)
            );
        } else if (!strcmp(mode, "MSMW_LOG")) {
            runner(
                QUESTA::Simulator::Mode::MSMW_LOG,
                (double*)PyArray_DATA((PyArrayObject*)s),
                s_len,
                warmup,
                n_iter,
                n,
                seed,
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
    {"run", (PyCFunction)run, METH_VARARGS, run__doc__},
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
    "questa.runner._base",
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
