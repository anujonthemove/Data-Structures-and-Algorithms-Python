#include <iostream>
using namespace std;

int main() {

    int arr[10] = {6, 1, 4, 9, 2};
    int num_elems = 5;
    int elem;
    int pos = 1;

    cout << "Current array: ";

    for(int i=0; i<num_elems; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
    cout << "Enter element: ";
    cin >> elem;
    cout << endl;

    for(int i=num_elems-1; i >= pos-1; i--) {
        arr[i+1] = arr[i];
    }
    arr[pos-1] = elem;

    num_elems++;

    cout << "Mod array: ";

    for(int i=0; i<num_elems; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;

    return 0;
}