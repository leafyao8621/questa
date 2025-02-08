#include "../simulator.h"

void QUESTA::Simulator::run_max_minus_queue_length(
    double s,
    size_t warmup,
    size_t n_iter,
    size_t *total_queue_length) {
    lemon::GraphExtender<lemon::ListGraphBase>::EdgeMap<size_t> em(this->lg);
    lemon::MaxWeightedPerfectMatching<
        lemon::ListGraph,
        lemon::GraphExtender<lemon::ListGraphBase>::EdgeMap<size_t>>
            mwm(this->lg, em);
    size_t cur_total_queue_length = 0;
    for (size_t i = 0; i < warmup; ++i) {
        size_t max = 0;
        for (size_t j = 0, *jj = this->queue_length; j < (n << 1); ++j, ++jj) {
            size_t flag = this->gen() < (s / this->n);
            *jj += flag;
            max = *jj > max ? *jj : max;
            em[this->lg.edgeFromId(j)] += flag;
            cur_total_queue_length += flag;
        }
        for (size_t j = 0, *jj = this->queue_length; j < (n << 1); ++j, ++jj) {
            em[this->lg.edgeFromId(j)] =
                *jj ? max - em[lg.edgeFromId(j)] : 0;
        }
        mwm.run();
        for (size_t j = 0; j < n; ++j) {
            size_t flag =
                em[mwm.matchingMap()[this->lg.nodeFromId(j)]] >= 1;
            em[mwm.matchingMap()[this->lg.nodeFromId(j)]] -= flag;
            cur_total_queue_length -= flag;
        }
    }
    for (size_t i = 0, *ii = total_queue_length; i < n_iter; ++i, ++ii) {
        size_t max = 0;
        for (size_t j = 0, *jj = this->queue_length; j < (n << 1); ++j, ++jj) {
            size_t flag = this->gen() < (s / this->n);
            *jj += flag;
            max = *jj > max ? *jj : max;
            em[this->lg.edgeFromId(j)] += flag;
            cur_total_queue_length += flag;
        }
        for (size_t j = 0, *jj = this->queue_length; j < (n << 1); ++j, ++jj) {
            em[this->lg.edgeFromId(j)] =
                *jj ? max - em[lg.edgeFromId(j)] : 0;
        }
        mwm.run();
        for (size_t j = 0; j < n; ++j) {
            size_t flag =
                em[mwm.matchingMap()[this->lg.nodeFromId(j)]] >= 1;
            em[mwm.matchingMap()[this->lg.nodeFromId(j)]] -= flag;
            cur_total_queue_length -= flag;
        }
        *ii = cur_total_queue_length;
    }
}
