#include<iostream>

using namespace std;

int main()
{
//    character type
    char middle_initial {'A'};
    cout<<"My middle initial is "<<middle_initial<<"\n";
   
    
//  integers

    unsigned short int score {55};
    cout<<"My exam score is :"<<score<<"\n";
    
//   long number

    long people_on_earth {7600000000};
    cout<<"There are "<<people_on_earth<<" people on earth.\n"; 
    
    long long alpha_centauri_dist {9'461'000'000'000};
    cout<<"Distance to Alpha Centauri is :"<<alpha_centauri_dist<<"\n";
    
    
//  Floating types

    float x {3.3};
    cout<<"Price of $ADA is :"<<x<<"\n";
    
    double pi {3.14159};
    cout<<"Value of pi :"<<pi<<"\n";
    
    long double e {2.7e120};
    cout<<e<<" is a very large number.\n";
    
    
//    Boolean values

    bool game_over {false};
    cout<<"The value of game over is:"<<game_over<<"\n";
    
    
//    overflow example

    short value1 {30000};
    short value2 {3000};
    short product {value1 * value2};
    
    cout<<"The product is :"<<product<<endl;
    
    return 0;
}
    