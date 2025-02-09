#include <cstring>

#include "simulator.h"

void QUESTA::Simulator::init(size_t n, int seed) {
    for (size_t i = 0; i < n; i++) {
        lg.addNode();
        lg.addNode();
    }
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = n; j < (n << 1); ++j) {
            lg.addEdge(lg.nodeFromId(i), lg.nodeFromId(j));
        }
    }
    this->gen.seed(seed);
    this->n = n;
}
