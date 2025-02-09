#ifndef UTIL_MRG32K3A_H_
#define UTIL_MRG32K3A_H_

namespace QUESTA {
    class MRG32K3a {
    private:
        double s10, s11, s12, s20, s21, s22;
    public:
        void seed(int seed);
        double operator()(void);
    };
}

#endif
