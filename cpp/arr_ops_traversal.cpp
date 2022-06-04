#include <iostream>
using namespace std;

/*
Array Operations: traversal
*/

int main() {

	
	int a[5] = {10, 2, 31, 44, 59};
	int size = sizeof(a)/sizeof(a[0]);
	for(int i = 0; i < size; i++) {
		cout <<"a[" << i << "]: " << a[i] << endl;

	}

	cout << endl;

	return 0;
}