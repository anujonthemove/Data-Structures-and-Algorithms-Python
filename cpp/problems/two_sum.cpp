#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

class Solution {
    public:
        vector <int> twoSum(vector<int>& nums, int target) {
            int nums_size = nums.size();
            vector<int> pos;
            int two_sum = 0;

            for(int i=0; i < nums_size; i++) {
                 
                for(int j=i+1; j < nums_size; j++) {
                    two_sum = nums[i]+nums[j];
                    if (two_sum == target) {
                        pos.push_back(i);
                        pos.push_back(j);
                        break;
                        }
                }
                
                //if (two_sum == target) { break; }
            }
            return pos;
        }
};


int main() {

    vector<int> vect{3, 2, 4};
    vector<int> sol;

    int target = 6;

    Solution obj;

    sol = obj.twoSum(vect, target);
    
    for(int i=0; i < sol.size(); i++) {
        cout << sol[i] << endl;
    }
    
    return 0;
}