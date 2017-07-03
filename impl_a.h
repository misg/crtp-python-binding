#ifndef CRTP_IMPL_A_H_
#define CRTP_IMPL_A_H_

#include "interface.h"

class ImplA : public Interface<ImplA> {};

#endif // CRTP_IMPL_A_H_
