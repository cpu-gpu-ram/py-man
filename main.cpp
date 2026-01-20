#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
    string options;
    cout << "Welcome!" << "\nPlease select the operation you'd like to perform.\n";

    ifstream readfile("options.txt");
    while (getline(readfile, options)) {
        cout << options;
    }

    while (true) {
            
        string x;
        int usrin;
        cin >> usrin;
        


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
