#include "../simulator.h"

void QUESTA::Simulator::operator()(
    Mode mode,
    double s,
    size_t warmup,
    size_t n_iter,
    int *total_queue_length) {
    switch (mode) {
    case Mode::MAX_WEIGHT:
        this->run_max_weight(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::MAX_SIZE:
        this->run_max_size(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::MSMW:
        this->run_msmw(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::MSMW_LOG:
        this->run_msmw_log(
            s, warmup, n_iter, total_queue_length);
        break;
    }
}
