#include <bits/stdc++.h>
using namespace std;

/*
- Weak : Less than 8 characters and absence of an uppercase character and a symbol
- Moderate : More than 8 characters and absence of either an uppercase character or symbol or less than 3 numbers
- Strong : More than 8 characters and presence of uppercase character and a symbol as well as 3 numbers
*/

bool isLengthGood(string& s){
    return s.length() >= 8;
}

bool containsUpperCaseCharacter(string& s){
    int n = s.length();
    for(int i = 0; i < n; i++){
        char ch = s[i];
        if('A' <= ch && ch <= 'Z') return true;
    }

    return false;
}

bool containsSymbol(string& s){
    int n = s.length();
    for(int i = 0; i < n; i++){
        char ch = s[i];
        if(ch == '_' || ch == '&' || ch == '#' || ch == '%' || ch == '@') return true;
    }

    return false;
}

bool containsAtleast3Numbers(string& s){
    int n = s.length();
    int nums = 0;
    for(int i = 0; i < n; i++){
        char ch = s[i];
        if('0' <= ch && ch <= '9') nums++;
    }

    return nums >= 3;
}

string strengthOfPassword(string& s, unordered_set<string>& commonPassword){
    int n = s.length();
    
    // User has entered a very common password
    if(commonPassword.find(s) != commonPassword.end()) return "Your password is very common! Set another password";

    // If length is less than 8, it s a weak password
    if(!isLengthGood(s)) return "Weak";

    // Length more than 8 but either of the 3 conditions not satisfied then it is not moderate
    else if(isLengthGood(s) && !(containsSymbol(s) && containsUpperCaseCharacter(s) && containsAtleast3Numbers(s))) return "Moderate";

    // Otherwise return Strong Pasword
    return "Strong";
}

int main(){
    string s;
    cout << "Enter your password here: ";
    cin >> s;

    // Making a set of common password
    unordered_set<string> commonPassword;
    commonPassword.insert("123456");
    commonPassword.insert("qwerty");
    commonPassword.insert("password123");

    cout << "Strength of your Password: " << strengthOfPassword(s, commonPassword) << "\n";
    return 0;
}