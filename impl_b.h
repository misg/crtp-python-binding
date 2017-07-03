#ifndef CRTP_IMPL_B_H_
#define CRTP_IMPL_B_H_

#include "interface.h"

class ImplB : public Interface<ImplB> {};

#endif // CRTP_IMPL_B_H_
