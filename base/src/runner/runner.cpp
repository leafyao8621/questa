#include "runner.h"

QUESTA::Runner::Runner(size_t n_thread) {
    this->pool = new std::thread[n_thread];
    this->n_thread = n_thread;
}

QUESTA::Runner::~Runner() {
    delete[] this->pool;
}

void QUESTA::Runner::operator()(
    Simulator::Mode mode,
    double *s,
    size_t s_len,
    size_t warmup,
    size_t n_iter,
    size_t n,
    int seed,
    int *total_queue_length) {
    std::thread *iter_pool = this->pool;
    for (size_t i = 0; i < s_len && i < this->n_thread; ++i, ++iter_pool) {
        *iter_pool =
            std::thread(
                [] (
                    Simulator::Mode mode,
                    double *s,
                    size_t s_len,
                    size_t start,
                    size_t step,
                    size_t warmup,
                    size_t n_iter,
                    size_t n,
                    int seed,
                    int *total_queue_length) {
                    double *iter_s = s + start;
                    int *iter_total_queue_length =
                        total_queue_length + start * n_iter;
                    for (
                        size_t i = start;
                        i < s_len;
                        i += step,
                        iter_s += step,
                        iter_total_queue_length += step * n_iter) {
                        Simulator simulator;
                        simulator.init(n, seed);
                        simulator(
                            mode,
                            *iter_s,
                            warmup,
                            n_iter,
                            iter_total_queue_length
                        );
                    }
                },
                mode,
                s,
                s_len,
                i,
                n_thread,
                warmup,
                n_iter,
                n,
                seed,
                total_queue_length
            );
    }
    iter_pool = this->pool;
    for (size_t i = 0; i < s_len && i < this->n_thread; ++i, ++iter_pool) {
        iter_pool->join();
    }
}
