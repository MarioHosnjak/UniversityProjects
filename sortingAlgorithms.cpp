#include<iostream>

using namespace std;

int* selectionSort(int Array[], int size){
    int temp;
    for(int i = 0; i < size; i++){
        int min = i;
        for(int j = i + 1; j < size; j++){
            if(Array[j] < Array[min]){
                min = j;
            }
        }
        temp = Array[min];
        Array[min] = Array[i];
        Array[i] = temp;
    }
    return Array;
}

int* bubbleSort(int Array[], int size){
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < size - i - 1; j++){
            if(Array[j] > Array[j+1]){
                int temp = Array[j];
                Array[j] = Array[j+1];
                Array[j+1] = temp;
            }
        }
    }
}

int* improvedBubbleSort(int Array[], int size){
    bool swapHappened = true;
    for(int i = 0; swapHappened == true; i++){
        swapHappened = false;
        for(int j = 0; j < size - 1 - i; j++){
            if(Array[j] > Array[j+1]){
                int temp = Array[j];
                Array[j] = Array[j+1];
                Array[j+1] = temp;

                swapHappened = true;
            }
        }
        if(!swapHappened) break;
    }
}

int* insertionSort(int Array[], int size){
    int temp, i, j;
    for(i = 1; i < size; i++){
        temp = Array[i];
        for(j = i; j >= 1 && temp < Array[j-1]; j--){
            Array[j] = Array[j-1];
        }
        Array[j] = temp;
    }
}