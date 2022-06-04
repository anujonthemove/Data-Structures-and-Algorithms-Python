#include <iostream>
using namespace std;

int main() {

	int arr_size = 0;

	cout << "Enter size of (integer)array: ";

	cin >> arr_size;

	int arr[arr_size];

	for(int i=0; i<arr_size; i++) {
		cin >> arr[i];
	}


	cout << "User input array is: ";

	for(int i=0; i<arr_size; i++) {
		cout << arr[i] << " ";
	} 
	
	cout << endl;
	return 0;
}