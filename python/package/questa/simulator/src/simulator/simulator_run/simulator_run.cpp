#include "../simulator.h"

void QUESTA::Simulator::operator()(
    Mode mode,
    double s,
    size_t warmup,
    size_t n_iter,
    int *total_queue_length) {
    switch (mode) {
    case Mode::QUEUE_LENGTH:
        this->run_queue_length(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::MAX_MINUS_QUEUE_LENGTH:
        this->run_max_minus_queue_length(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::MAX_PLUS_QUEUE_LENGTH:
        this->run_max_plus_queue_length(s, warmup, n_iter, total_queue_length);
        break;
    case Mode::LOG_MAX_PLUS_QUEUE_LENGTH:
        this->run_log_max_plus_queue_length(
            s, warmup, n_iter, total_queue_length);
        break;
    }
}
