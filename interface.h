#ifndef CRTP_INTERFACE_H_
#define CRTP_INTERFACE_H_ 

#include <iostream>
#include <typeinfo>

template<class Impl>
class Interface
{
public:
  void print() {
    auto impl = static_cast<Impl*>(this);
    std::cout << typeid(impl).name() << std::endl;
  }
};

#endif // CRTP_INTERFACE_H_
