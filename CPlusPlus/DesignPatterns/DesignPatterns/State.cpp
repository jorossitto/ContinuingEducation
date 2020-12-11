#include "State.h"

ostream& operator<<(ostream& os, const State& s)
{
    switch (s)
    {
    case State::On:
        os << "immigrants welcome";
        break;
    case State::Off:
        os << "Closed to new immigrants";
        break;
    }
    return os;
}

ostream& operator<<(ostream& os, const Trigger& t)
{
    switch (t)
    {
    case Trigger::Welcome:
        os << "All immigrants welcome";
        break;
    case Trigger::Closed:
        os << "Sorry closed for immigration";
        break;
    default: break;
    }
    return os;
}
