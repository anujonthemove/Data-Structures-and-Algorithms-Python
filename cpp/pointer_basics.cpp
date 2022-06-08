#include <iostream>
using namespace std;
 
int main() {
    
    /*
     * it is a pointer to integer
     * we cannot say that the datatype to the pointer is int
     * Pointer is a variable that stores address of other variable
     * address is always in hexadecimal form
     * & is address of operator
     * * is de-reference operator - it basically means get the value at the 'address of'
     * Array name itself acts as a pointer
     * Array name always contains base address of the array
     */ 

    int b = 10;
    int* ptr;
    ptr = &b;
    
    int arr[10] = {5, 2, 3, 8, 9};
    int num_elems = 5;
    int* arr_ptr;
    arr_ptr = arr;
    
    cout << "Address of b: " << &b << endl;
    cout << "Value of ptr: " << ptr << endl;
    cout << "Value at the address pointed by ptr: " << *ptr << endl;
    
    cout << "Base address of array arr: " << arr<<endl;
    cout << "Value of arr_ptr: " << arr_ptr<<endl;
    cout << "Value at +1 location: " << *(arr_ptr+1) << endl;

    // another way to access array elements
    for(int i=0; i<num_elems; i++) {
        cout << "value: " << i[arr] << endl;
    }

    cout << "arr: " << (arr) << endl;
    cout << "&arr: " << (&arr) << endl;
    
    cout << "arr+1: " << (arr+1) << endl;
    cout << "&arr+1: " << (&arr+1) << endl;

    // check address of each of element of array
    for(int i=0; i<num_elems+20; i++) {
        cout << "address of arr+" << i << ": " << (arr+i) << endl; 
    }

    cout << endl;
    // check address of each of element of array
    for(int i=0; i<num_elems; i++) {
        cout << "address of &arr+" << i << ": " << (&arr+i) << endl; 
    }

    return 0;
}