/*
  This is a brute-force algorithm which colours connected graphs.
  To fully understand this task, please read "3._laboratorijska_vjezba[3].pdf"
*/


#include <iostream>
#include <fstream>
#include<algorithm>
#include<cmath>
#include<climits>

using namespace std;

bool contains(int sArray[], int element, int sn){
    bool found = false;
    for(int i = 0; i < sn; i++){
        if(sArray[i] == element){
            found = true;
            break;
        }
    }
    return found;
}


int main(void){

    string filename;

    cout << "Unesite ime datoteke: ";
    getline(cin, filename);

    int n;
    int ns;

    ifstream MyReadFile(filename);

    MyReadFile >> n;
    MyReadFile >> ns;

    int sArray[ns];

    for(int i = 0; i < n; i++){
        MyReadFile >> sArray[i];
    }

    int matrix[n][n];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int k = abs((i+1) - (j+1));
            if(k == 0) matrix[i][j] = 0;
            if(contains(sArray, k, ns)){
                matrix[i][j] = 1;
            } else {
                matrix[i][j] = 0;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] << "   ";
        }
        cout << endl;
    }

    int vrhovi[n];
    for(int i = 0; i < n; i++){
        vrhovi[i] = i + 1;
    }

    if(n % 2 && ns == 2) {
            int kromBr = 3;
            cout << "Kromatski broj je 3." << endl;
    }else if(n % 2 == 0 && ns == 2 || ns == 1) {
            int kromBr = 2;
            cout << "Kromatski broj je 2." << endl;
    }else if(ns == (n - 1)) {
            int kromBr = n;
            cout << "Kromatski broj je " << n << "." << endl;
    } else {

        int kromatski = INT_MAX;

        //iscrpni algoritam
        do{
            // je li permutacija dobra
            bool validPerm = true;
            for(int i = 0; i < n-1; i++){
                if(matrix[vrhovi[i]-1][vrhovi[i+1]-1] == 0) {
                    validPerm = false;
                    break;
                }
            }
            //cout << validPerm << endl;
            if(validPerm){
                
                // algoritam po dobroj permutaciji
                int boje[n] = {0};
                int brBoja = 0;

                // za prvi element prva boja
                boje[vrhovi[0]-1] = ++brBoja;

                // ostali elementi
                for(int i = 1; i < n; i++){
                    
                    bool pronadenaBoja = false;
                    bool dobraBoja;
                    for(int j = 0; j < n; j++){
                        if(boje[j] != 0 && boje[j] != boje[vrhovi[i-1]]){
                            //probaj odgovara li ta boja
                            //ako odgovara, stavi boje[vrhovi[i]-1] = boje[j]
                            //ako ne odgovara, stavi boje[vrhovi[i]-1] = ++brBoja;
                            pronadenaBoja = true;

                            //prolazim kroz susjedne vrhove, gledam je li koji vrh boje[j] boje
                            dobraBoja = true;
                            for(int k = 0; k < n; k++){
                                //pronađi susjeda s bojom
                                if(matrix[vrhovi[i]-1][k] != 0){
                                    if(boje[k] == boje[j]){
                                        dobraBoja = false;
                                        break;
                                    }
                                }
                            }
                            //ako nismo pronašli susjeda s tom bojom, boja je dobra
                            if(dobraBoja){
                                boje[vrhovi[i]-1] = boje[j];
                                break;
                            }

                        }
                    }
                    if(pronadenaBoja == false || dobraBoja == false){
                        boje[vrhovi[i]-1] = ++brBoja;
                    }

                }
                for(int p = 0; p < n; p++){
                    cout << vrhovi[p] << " ";
                }
                cout << endl;
                for(int p = 0; p < n; p++){
                    cout << boje[p] << " ";
                }
                cout << endl;
                cout << "Broj boja: " << brBoja << endl;
                if(brBoja < kromatski) kromatski = brBoja;
                cout << "Trenutno najmanji broj: " << kromatski << endl;
            }
        } while(next_permutation(vrhovi, vrhovi + n));

        cout << "KROMATSKI BROJ JE: " << kromatski << endl;
    }
    return 0;
}
