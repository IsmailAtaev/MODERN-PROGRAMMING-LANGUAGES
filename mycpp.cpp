#include <iostream>
#include  <vector>

using namespace std;
 
int main (){

   vector<int> numbers {12,21,22,11,44,33};
   float summa = 0;

   for (int i = 0; i < numbers.size(); i++)
   {
      summa += numbers.at(i);
   }
   

   cout << "sum = " << summa  << endl; 
   cout << "ARF = " << summa / numbers.size() <<  endl;
   cout << "Hello isma!" << endl;
   return 0;
}