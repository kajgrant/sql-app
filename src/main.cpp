#include <iostream>
#include <string>

using namespace std;

class authentication
{
public:
    void setUname(string uname)
    {
        this->username = uname;
    }
    void setPassword(string pwd)
    {
        this->password = pwd;
    }
    string getUname()
    {
        return this->username;
    }
    string getPassword()
    {
        return this->password;
    }
    void setAuthentication()
    {
        string uname, pwd;
        cout << "Please enter your username: ";
        cin >> uname;
        cout << "\nPlease enter your password: ";
        cin >> pwd;

        this->setUname(uname);
        this->setPassword(pwd);
    }

private:
    string username;
    string password;
};

int main()
{

    authentication userAuth;
    char selection;

    cout << "Welcome to the SQL navigator! Please select and option below:\n";
    cout << "---------------------------------------------------\n";
    cout << "1: Login\n";
    cout << "2: Search Business\n";
    cout << "3: Search Users\n";
    cout << "4: Make Friend\n";
    cout << "5: Write Review\n";
    cout << "6: Exit\n";
    cin >> selection;

    while (!(1 <= (int)(selection - 48) && (int)(selection - 48) <= 6) || !isdigit(selection))
    {
        cout << "Error: Incorrect input, please try again!\n";
        cin >> selection;
    }

    switch (selection)
    {
    case '1':
        userAuth.setAuthentication();
        break;
    case '2':
        break;
    case '3':
        break;
    case '4':
        break;
    case '5':
        break;
    case '6':
        break;
    }

    return 0;
}