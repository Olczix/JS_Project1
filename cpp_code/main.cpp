#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>
#include <stdexcept>

using namespace std;

const int SIZE = 21;
int g_data[SIZE];
__int64 g_results[SIZE];
__int64 repetitions = 500000000;
string INPUT_FILE_PATH = "data/generated_data.txt";
string OUTPUT_FILE_PATH = "data/cpp_results_my_function.txt";

__int64 function(int number){
    if(number < 0){
        throw std::invalid_argument("ValueError - invalid argument");
    }
    
    __int64 result = 1;
    for(int i = 2; i<=number; i++){
        result *= i;
    }
    return result;
}

void read_data(){
    ifstream indata;
    int value, line_number = 0;
    indata.open(INPUT_FILE_PATH);
    if(!indata) {
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }
    while ( !indata.eof() ) {
        indata >> g_data[line_number];
        line_number++;
    }
    indata.close();
}

void save_results(){
    ofstream output_file;
    output_file.open(OUTPUT_FILE_PATH);
    for(int i = 0; i < SIZE; i++) {
        output_file << g_results[i] << endl;
    }
    output_file.close();
}

int main()
{
    printf("\n\nCUSTOM FACTORIAL FUNCTION IMPLEMENTATION IN C++ (%lld times)\n", repetitions);
    // Read dataset from file
    read_data();

    // Empty loop - time
    auto empty_loop_start = chrono::steady_clock::now();
    for(__int64 r = 0; r < repetitions; r++) {
        for(int i = 0; i < SIZE; i++) {}
    }
    auto empty_loop_end = chrono::steady_clock::now();
    int empty_loop_in_s = chrono::duration_cast<chrono::seconds> (empty_loop_end - empty_loop_start).count();
    printf("empty loop duration is \t%d [s]\n", empty_loop_in_s);
    

    // Actual calculations - time
    auto loop_start = chrono::steady_clock::now();
    for(__int64 r = 0; r < repetitions; r++) {
        for(int i = 0; i < SIZE; i++) {
            function(g_data[i]);
        }
    }
    auto loop_end = chrono::steady_clock::now();
    int loop_in_s = chrono::duration_cast<chrono::seconds> (loop_end - loop_start).count();
    printf("loop with calculations is \t%d [s]\n", loop_in_s);
    printf("actual calculations time is \t%d [s]\n", loop_in_s - empty_loop_in_s);

    // Make calculations and save the results
    for(int i = 0;i < SIZE; i++) { g_results[i] = function(g_data[i]); }

    // Save results to the file
    save_results();

    return 0;
}
