#include <Tracy.hpp>
#include <thread>

void f()
{
    ZoneScoped;
    std::this_thread::sleep_for(std::chrono::microseconds(100));
}

int main()
{
    ZoneScoped;

    for(int i = 0; i < 10; ++i)
    {
        f();
    }
}
