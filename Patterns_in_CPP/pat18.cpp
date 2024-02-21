#include<iostream>
using namespace std;
int main(){
	int n,i,j;
	cin>>n;
	for(i=n;i>=0;i--){
		for(j=i;j<n;j++){
			char ch='A'+j;
			cout<<ch<<" ";
			ch++;
		}
		cout<<endl;
	}
}
