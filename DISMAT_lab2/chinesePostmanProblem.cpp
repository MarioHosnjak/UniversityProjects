#include<iostream>
#include<algorithm>
#include<math.h>
#include<climits>

using namespace std;

int main(void){

    int n, a, b;

    cout << "Unesite redom, odvojene razmakom, parametre n, a i b: ";
    cin >> n >> a >> b;
     
    int polje[n][n];

    for(int k = 0; k < n; k++){
        for(int l = 0; l < n; l++){
            if(k < l){
                polje[k][l] = (a*(k+1) + b*(l+1))*(a*(k+1) + b*(l+1)) + 1;
            } else if(l < k){
                polje[k][l] = polje[l][k];
            } else polje[k][l] = 0;
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << polje[i][j] << "    ";
        }
        cout << endl;
    }


// POHLEPNI ALGORITAM / GREEDY ALGORITHM
    //pronađi najmanji brid
    int indK, indL, minValue = INT_MAX;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(polje[i][j] < minValue && polje[i][j] != 0){
                indK = i;
                indL = j;
                minValue = polje[i][j];
            }
        }
    }
    int trenutni1 = indK;
    int trenutni2 = indL;
    int koraci = 2; // početna 2 vrha
    int duljina = minValue; //pocetna duljina
    bool taken[n] = {false};
    taken[indK] = true;
    taken[indL] = true;
    
    while(koraci < n){
        int minVal1 = INT_MAX, minVal2 = INT_MAX;
        for(int i = 0; i < n; i++){
            if(polje[trenutni1][i] < minVal1 && polje[trenutni1][i] != 0 && taken[i] == 0){
                minVal1 = polje[trenutni1][i];
                indK = i;
            }
            if(polje[trenutni2][i] < minVal2 && polje[trenutni2][i] != 0 && taken[i] == 0){
                minVal2 = polje[trenutni2][i];
                indL = i;
            }
        }
        if(minVal1 > minVal2){
            taken[indL] = true;
            duljina += minVal2;
            trenutni2 = indL;
        } else {
            taken[indK] = true;
            duljina += minVal1;
            trenutni1 = indK;
        }
        koraci++;
    }

    duljina += polje[trenutni1][trenutni2];

    cout << "Rezultat pohlepnog algoritma: " << duljina << endl;



// ISCRPNI ALGORITAM / BRUTE-FORCE ALGORITHM
    int vrhovi[n];
    int iscrpniVal = INT_MAX;
    for(int i = 1; i <= n; i++){
        vrhovi[i - 1] = i;
    }
    do{
        int tempVal = 0;
        for(int i = 0; i < n-1; i++){
            // cout << vrhovi[i] << " ";
            tempVal += polje[vrhovi[i]-1][vrhovi[i+1]-1];
        }
        tempVal += polje[vrhovi[0]-1][vrhovi[n-1]-1];
        if(tempVal < iscrpniVal) iscrpniVal = tempVal;
    } while(next_permutation(vrhovi, vrhovi + n));
    cout << "Rezultat iscrpnog algoritma: " << iscrpniVal << endl;

    cout << ((iscrpniVal == duljina) ? "Pohlepni algoritam na ovom grafu DAJE optimalno rjesenje!" : "Pohlepni algoritam na ovom grafu NE DAJE optimalno rjesenje!");

    return 0;
}
