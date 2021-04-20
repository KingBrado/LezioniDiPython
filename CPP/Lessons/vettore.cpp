#include <iostream>
#include <vector>

using namespace std;

int somma_vettore(const vector<int>& v)
{
    int somma = 0;
    for(int e : v)
    {
        somma += e;
    }
    return somma;
}

void popola_vettore(vector<int>& v)
{
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
}

int main(int argc, char** argv)
{
    vector<int> v{1,2,3,4,5,6};
    cout << somma_vettore(v) << endl;
    
    vector<int> a;
    popola_vettore(a);

    for(int e: a)
    {
        cout << e << ' ';
    }
    cout << '\n';

   // int c;
  //  popola_vettore(c);
   // cout << c<< endl;

    return 0;
}