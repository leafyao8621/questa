#include "../simulator.h"

void QUESTA::Simulator::run_max_weight(
    double s,
    size_t warmup,
    size_t n_iter,
    int *total_queue_length) {
    lemon::GraphExtender<lemon::ListGraphBase>::EdgeMap<int> em(this->lg);
    lemon::MaxWeightedPerfectMatching<lemon::ListGraph> mwm(this->lg, em);
    int cur_total_queue_length = 0;
    for (size_t i = 0; i < warmup; ++i) {
        mwm.run();
        std::cout << "Service:" << std::endl;
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag =
                em[this->lg.edgeFromId(j)] > 0 &&
                mwm.matching(this->lg.edgeFromId(j));
            em[this->lg.edgeFromId(j)] -= flag;
            std::cout << em[this->lg.edgeFromId(j)] << ' ';
            cur_total_queue_length -= flag;
        }
        std::cout << std::endl << "Arrival:" << std::endl;
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag = this->gen() < (s / this->n);
            em[this->lg.edgeFromId(j)] += flag;
            std::cout << em[this->lg.edgeFromId(j)] << ' ';
            cur_total_queue_length += flag;
        }
        std::cout << std::endl;
    }
    int *ii = total_queue_length;
    for (size_t i = 0; i < n_iter; ++i, ++ii) {
        mwm.run();
        std::cout << "Service:" << std::endl;
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag =
                em[this->lg.edgeFromId(j)] > 0 &&
                mwm.matching(this->lg.edgeFromId(j));
            em[this->lg.edgeFromId(j)] -= flag;
            std::cout << em[this->lg.edgeFromId(j)] << ' ';
            cur_total_queue_length -= flag;
        }
        for (int j = 0; j <= this->lg.maxEdgeId(); ++j) {
            int flag = this->gen() < (s / this->n);
            em[this->lg.edgeFromId(j)] += flag;
            std::cout << em[this->lg.edgeFromId(j)] << ' ';
            cur_total_queue_length += flag;
        }
        std::cout << std::endl;
        *ii = cur_total_queue_length;
    }
}
