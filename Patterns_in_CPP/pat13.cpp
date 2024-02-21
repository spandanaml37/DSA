#include<iostream>
using namespace std;
int main(){
	int n,i,j,num=1;
	cin>>n;
	for(i=0;i<n;i++){
		for(j=0;j<i+1;j++){
			cout<<num;
			num+=1;
		}
		cout<<endl;
	}
}
