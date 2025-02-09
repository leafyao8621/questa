#ifndef RUNNER_RUNNER_H_
#define RUNNER_RUNNER_H_

#include <thread>

#include "../simulator/simulator.h"

namespace QUESTA {
    class Runner {
        std::thread *pool;
        size_t n_thread;
    public:
        Runner(size_t n_thread);
        ~Runner();
        void operator()(
            Simulator::Mode mode,
            double *s,
            size_t s_len,
            size_t warmup,
            size_t n_iter,
            size_t n,
            int seed,
            int *total_queue_length);
    };
}

#endif
