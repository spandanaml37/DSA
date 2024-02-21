#include<iostream>
using namespace std;
int main(){
	int n,i,j;
	//int space=2*n-2*i;
	cin>>n;
	for(i=n;i>=0;i--){
		for(j=1;j<=i;j++){
			cout<<"*";
		}
		for(j=1;j<=2*n-2*i;j++){
			cout<<" ";
		}
		for(j=i;j>=1;j--){
			cout<<"*";
		}
		cout<<endl;
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			cout<<"*";
		}
		for(j=1;j<=2*n-2*i;j++){
			cout<<" ";
		}
		for(j=i;j>=1;j--){
			cout<<"*";
		}
		cout<<endl;
		//space-=2;
	}
}
