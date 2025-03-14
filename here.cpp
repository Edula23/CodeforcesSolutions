#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
int main(){
     vector<char>number;
     string number2;
     getline(cin, number2);
     for(char i:number2){
        number.push_back(i);
     }
    int counter=0;
    for(char ch: number){
        if(ch =='4'||ch == '7'){
            counter++;
        }
    }
    if(counter ==4 || counter==7){
        cout<<"YES"<<endl;
    }
    else{
        cout<<"NO";
    }

    return 0;
}



