#include <iostream>
using namespace std;
 
int main() {
    int arr[10] = {6, 1, 4, 9, 2};
    int num_elems = 5;
    int pos;
    int item;

    cout << "Current array: ";

    for(int i=0; i<num_elems; i++) {
        cout << arr[i] << " ";
    }

    cout << "Enter position to delete from: ";
    cin >> pos;

    if(pos <=0 || pos > num_elems) {
        cout << "Invalid position" << endl;
    }

    else{
        item = arr[pos-1];
        for(int i=pos-1; i<num_elems-1; i++) {
            arr[i] = arr[i+1];
        }
        num_elems--;
    }

    cout << "Deleted element: " << item << endl;


    cout << "Mod array: ";

    for(int i=0; i<num_elems; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;

    
    
    return 0;
}