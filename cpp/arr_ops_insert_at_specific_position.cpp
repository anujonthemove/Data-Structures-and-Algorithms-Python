#include <iostream>
using namespace std;

/*
Time complexity of insertion

* best case: O(1)
* worst case: O(n)
* general case: O(n-p)

*/


int main() {

    int arr[10] = {5, 2, 56, 2, 4, 6};

    int size = sizeof(arr)/sizeof(arr[0]);

    int num_elements = 6;

    int pos, elem;

    cout << "Size of current array: " << num_elements <<endl;
    cout << "Current array: " << endl;

    for(int i=0; i < size; i++) {
        cout << arr[i] << " ";
    }

    cout <<  endl;

    cout <<"Enter poition: ";
    cin >> pos;
    cout << endl;

    if(pos <= 0 || pos >= size) {
        cout << "Invalid position" << endl;
    }
    else {
        cout << "Enter element: ";
        cin >> elem;

        for(int i=num_elements-1; i >= pos-1; i--) {
            arr[i+1] = arr[i];
        }

        arr[pos-1] = elem;
    }


    num_elements++;

    cout << "Size of modified array: " << num_elements <<endl;
    cout << "Modified array: " << endl;

    for(int i=0; i < size; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0;
}