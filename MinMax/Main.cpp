#include <iostream>

using namespace std;

int main(){
    int num,n,min=2147483647,max=-2147483648;
    cin>> num;
    for(int i=0;i<num;i++){
        cin>>n;
        if (max<n){
            max=n;
        }
        if (min>n){
            min=n;
        }
    }
    cout << min<<endl;
    cout<< max<<endl;
}