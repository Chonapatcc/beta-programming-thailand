#include <iostream>
using namespace std;
int main(){
        int a,b,c;
        cin >>a>>b>>c;
        int score=a+b+c;
        if (score<=100 && score>=80){
            cout << "A";}
        else if(score<80 && score>=75){
            cout << "B+";
        }
        else if(score<75 && score>=70){
            cout << "B";
        }
        else if(score<70 && score>=65){
            cout << "C+";
        }
        else if(score<65 && score>=60){
            cout << "C";
        }
        else if(score<60 && score>=55){
            cout << "D+";
        }
        else if(score<55 && score>=50){
            cout << "D";
        }
        else{
            cout << "F";
        }
}
