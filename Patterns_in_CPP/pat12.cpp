#include<iostream>
using namespace std;
int main(){
	int n,i,j;
	//int space=2*n-2*i;
	cin>>n;
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			cout<<j;
		}
		for(j=1;j<=2*n-2*i;j++){
			cout<<" ";
		}
		for(j=i;j>=1;j--){
			cout<<j;
		}
		cout<<endl;
		//space-=2;
	}
}
