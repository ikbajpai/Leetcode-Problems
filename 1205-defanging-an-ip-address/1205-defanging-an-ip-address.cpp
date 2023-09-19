#include <string>

class Solution {
public:
    std::string defangIPaddr(std::string address) {
        for (size_t i = 0; i < address.size(); i++) {
            if (address[i] == '.') {
                address.replace(i, 1, "[.]");  // Replace '.' with "[.]"
                i += 3;  // Skip the replaced characters
            }
        }
        return address;
    }
};
