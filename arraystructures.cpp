#include <iostream>
using namespace std;
struct student{
    string id, name;
    int mark[10];
    int sum, ranK;
};
void getData(student s[], int &n, int &nCourses){
    cout<<"How many students";
    cin>>n;
    cout<<"How many courses";
    cin>>nCourses;
    for(int i=0; i<n; i++){
        cout<<"Enter student "<<i+1<<" details: ";
        cin>>s[i].id>>s[i].name;
        for(int j=0; j<nCourses; j++){
            cin>>s[i].mark[j];
        }
    }

}
void total(student s[], int &n, int &nCourses){
    for(int i=0; i<n; i++){
            int sum =0;
            for(int j=0; j<nCourses; j++){
        sum+=s[i].mark[j];
            }
            s[i].sum=sum;
    }

}
void ranks(student s[], int &n, int &nCourses){

    for(int i=0; i<n; i++){
        int counter=0;
        for(int j=0; j<n; j++){
            if(s[i].sum <= s[j].sum){
                counter++;
            }

        }
    s[i].ranK=counter;
    //cout<<s[i].ranK;
    }
}
void display(student s[], int &n, int &nCourses){
    cout<<"ID\t Name\t Sum\t Rank"<<endl;
    for(int i=0; i<n; i++){
        cout<<s[i].id<<"\t"<<s[i].name<<"\t"<<s[i].sum<<"\t"<<s[i].ranK<<endl;
    }
}


int main(){
    int n, nCourses;
    student s[10];
    getData(s, n, nCourses);
    total(s, n, nCourses);
    ranks(s, n, nCourses);
    display(s, n, nCourses);
    return 0;
    }
