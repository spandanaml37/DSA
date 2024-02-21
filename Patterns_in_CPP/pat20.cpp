#include<iostream>
using namespace std;
int main(){
	int i,j,n;
	cin>>n;
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
}
	for(i=n-1;i>=0;i--){
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

}
