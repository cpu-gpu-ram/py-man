#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <unistd.h>
using namespace std;

int main() {

    cout << "Welcome!" << "\nPlease select the operation you'd like to perform.\n";

    while (true) {
        
        int usrin;
        cin >> usrin;
        string x;



        switch (usrin)
        {
        case 1:
            cout << "Enter the name of the file you want to create. ";
            cin >> x;
            system(("touch "+x+".txt").c_str());
            break;

            
        case 2:
            cout << "Enter the name of the folder you want to create. ";
            cin >> x;
            system(("mkdir "+x).c_str());


        case 3:
            cout << "What file would you like to remove?";
            cin >> x;
            system(("rm "+x).c_str());
            break;
        

        case 4:
            cout << "What folder would you like to remove?";
            cin >> x;
            system(("rm -rf "+x).c_str());
            break;


        case 5:
            system("sudo lshw -short");
            break;


        case 6:
            system("nmtui");
            break;


        case 7:
            system("ani-cli");
            break;            


        case 8:
            cout << "Running the updater.";
            system("~/py-man/install.sh");
            break;


        case 9:
            exit(0);
            
            
        default:
            cout << "Please select a valid option.";
            break;
        }
        
    }
}
