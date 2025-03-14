#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
int main(){
    int testcases;
    cin>>testcases;
    int input[testcases];

    for(int i=0; i<testcases; i++){
        cin>>input[i];
    }
    for(int i=0; i<testcases; i++){
        int temp = input[i];
        int counter=0;
        if(temp>=10){
        int digit;
        vector<int>output;
        while(temp>0){
            digit = temp%10;
            if(digit!=0){
                counter++;
                temp/=10;
                if(temp<10){
                    break;
                }
                output.push_back(digit);
                output.push_back(temp-digit);

            }
            else{
                temp/=10;
                if(temp<10){
                    break;
                }
            }
        }
        cout<<counter;
        for(int i:output){
            cout<<i;
        }

        }
        else{
            cout<<"1\n"<<temp;
        }
    }

    return 0;
}
