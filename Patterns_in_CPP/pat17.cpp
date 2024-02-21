#include<iostream>
using namespace std;
int main(){
	int n,i,j;
	cin>>n;
	for(i=0;i<=n;i++){
		for(j=0;j<n-i;j++){
			cout<<" "<<" ";
		}
		for(j=0;j<i;j++){
			char ch='A'+j;
			cout<<ch<<" ";
			ch++;
		}
		for(j=i-2;j>=0;j--){
			char ch='A'+j;
			cout<<ch<<" ";
			ch++;
		}
		cout<<endl;
}
}
