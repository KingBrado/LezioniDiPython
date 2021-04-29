#include <iostream>
#include <list>
using namespace std;

bool ricerca_lista(int valore, const list<int>& lista)
{
    for (auto it=begin(lista); it != end(lista); ++it)
    {
        if(*it == valore)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    list<int> una_lista{1, 3, 5, 4, 5};
    for (auto it=begin(una_lista); it != end(una_lista); ++it)
    {
        cout << *it << " ";
    }
    cout << endl;

    cout << ricerca_lista(5, una_lista) << endl;
    return 0;
}