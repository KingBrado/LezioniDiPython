#include <iostream>
#include <vector>
using namespace std;

bool ricerca_vettore(int valore, const vector<int>& lista)
{
    bool trovato = false;
    for(int elemento : lista)
    {
        if(elemento == valore)
        {
            trovato = true;
            break;
        }
    }
    return trovato;
}

int main()
{
    vector<int> una_lista{1, 3, 5, 4, 5};
    cout << "Test 1: true == " << ricerca_vettore(5, una_lista) << endl;
    cout << "Test 2: false == " << ricerca_vettore(19, una_lista) << endl;
    return 0;
}