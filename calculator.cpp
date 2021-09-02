#include<iostream>

using namespace std;
class calculator
{
    int a,b;
public:
    void get();
    void add();
    void sub();
    void division();
    void mult();
};

void calculator::get()
{
    cout<<"Enter two number.\n";
    cin>>a>>b;
}
void calculator::add()
{
    cout<<"The sum is = "<<a+b;
    
}
void calculator::sub()
{
    cout<<"The difference is"<<a-b;
    
}
void calculator::division()
{
    cout<<"The division is ="<<a/b;
    
}
void calculator::mult()
{
    cout<<"The multiplication is ="<<a*b;
    
}

int main()
{
    calculator c;
    c.get();
    c.add();
    c.sub();
    c.division();
    c.mult();
    return 0;
}