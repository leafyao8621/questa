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
            MAX_WEIGHT,
            MAX_SIZE,
            MSMW,
            MSMW_LOG
        };
        enum Err {
            OUT_OF_MEMORY,
            NOT_IMPLEMENTED
        };
        void init(size_t n, int seed);
    private:
        void run_max_weight(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_max_size(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_msmw(
            double s,
            size_t warmup,
            size_t n_iter,
            int *total_queue_length);
        void run_msmw_log(
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
