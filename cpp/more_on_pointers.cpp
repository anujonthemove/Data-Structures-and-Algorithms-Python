#include <iostream>
#include <cstdio>

using namespace std;

int main() {

	int arr_size = 0;
    
	cout << "Enter size of (integer)array: ";

	cin >> arr_size;

	int arr[arr_size];

    int* ptr;
    ptr = arr;

    // the default method
    for(int i=0; i<arr_size; i++) {
		scanf("%d", &arr[i]);
	}

	// for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", (arr+i));
	// }

    // this is valid
    // for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", (i+arr));
	// }

    // this is valid
    // for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", &ptr[i]);
	// }

    // this is valid
    // for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", (ptr+i));
	// }

    
    // this is NOT VALID
    // for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", (&arr+i));
	// }

    // this is NOT VALID
    // for(int i=0; i<arr_size; i++) {
	// 	scanf("%d", (&ptr+i));
	// }

    cout << "User input new array is: ";

	for(int i=0; i<arr_size; i++) {
		cout << arr[i] << " ";
	} 
	
	cout << endl;
	return 0;
}