#ifndef SIMULATOR_SIMULATOR_H_
#define SIMULATOR_SIMULATOR_H_

#include <lemon/list_graph.h>
#include <lemon/matching.h>

#include "../util/mrg32k3a.h"

namespace QUESTA {
    class Simulator {
    private:
        lemon::ListGraph lg;
        MRG32K3a gen;
        size_t n;
    public:
        enum Mode {
            QUEUE_LENGTH,
            MAX_MINUS_QUEUE_LENGTH,
            MAX_PLUS_QUEUE_LENGTH,
            LOG_MAX_PLUS_QUEUE_LENGTH
        };
        enum Err {
            OUT_OF_MEMORY,
            NOT_IMPLEMENTED
        };
        void init(size_t n, int seed);
    private:
        void run_queue_length(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_max_minus_queue_length(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_max_plus_queue_length(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_log_max_plus_queue_length(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
    public:
        void operator()(
            Mode mode,
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
    };
}

#endif
