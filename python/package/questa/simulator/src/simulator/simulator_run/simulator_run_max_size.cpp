#include "../simulator.h"

void QUESTA::Simulator::run_max_size(
    double s,
    size_t warmup,
    size_t n_iter,
    int *total_queue_length) {
    lemon::GraphExtender<lemon::ListGraphBase>::EdgeMap<int> em(this->lg);
    lemon::GraphExtender<lemon::ListGraphBase>::EdgeMap<int> em1(this->lg);
    lemon::MaxWeightedPerfectMatching<lemon::ListGraph> mwm(this->lg, em1);
    int cur_total_queue_length = 0;
    for (size_t i = 0; i < warmup; ++i) {
        mwm.run();
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag =
                em[this->lg.edgeFromId(j)] > 0 &&
                mwm.matching(this->lg.edgeFromId(j));
            em[this->lg.edgeFromId(j)] -= flag;
            cur_total_queue_length -= flag;
        }
        int max = 0;
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag = this->gen() < (s / this->n);
            em[this->lg.edgeFromId(j)] += flag;
            max =
                em[this->lg.edgeFromId(j)] > max ?
                em[this->lg.edgeFromId(j)] :
                max;
            cur_total_queue_length += flag;
        }
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            em1[this->lg.edgeFromId(j)] =
                em[this->lg.edgeFromId(j)] ? max - em[lg.edgeFromId(j)] : 0;
        }
    }
    int *ii = total_queue_length;
    for (size_t i = 0; i < n_iter; ++i, ++ii) {
        mwm.run();
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag =
                em[this->lg.edgeFromId(j)] > 0 &&
                mwm.matching(this->lg.edgeFromId(j));
            em[this->lg.edgeFromId(j)] -= flag;
            cur_total_queue_length -= flag;
        }
        int max = 0;
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag = this->gen() < (s / this->n);
            em[this->lg.edgeFromId(j)] += flag;
            max =
                em[this->lg.edgeFromId(j)] > max ?
                em[this->lg.edgeFromId(j)] :
                max;
            cur_total_queue_length += flag;
        }
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            em1[this->lg.edgeFromId(j)] =
                em[this->lg.edgeFromId(j)] ? max - em[lg.edgeFromId(j)] : 0;
        }
        *ii = cur_total_queue_length;
    }
}
