#include <iostream>
#include <chrono>
#include <stdlib.h>
#include <thread>
#include <list>

int main() {
  using namespace std;

  cout << "This program can help you excecute terminal commands in sequence.\n";
  this_thread::sleep_for(chrono::seconds(2));
  cout << "I can only guarantee linux support, but windows might work too.\n";
  this_thread::sleep_for(chrono::seconds(3));
  cout << " \n";
  
  // Variable declarations
  list<string> commands{};
  string com;
  string cont;
  int initDelay;
  int intervalDelay;
  string cmd;
  string begin;
  int control = 0;
  int cancel = 1;
  string clear;
  tuple<string> credits = ("w3schools.org", "Active learning");
  
  // Begin user input
  cout << "Would you like to run the program? ([y]es or [n]o)\n";
  getline(cin, begin);
  cout << "\n";

  /* Prompts for terminal commands to run, while keeping count
  of the amount of commands entered */
  if (begin == "y"){
    while(true){
      cout << "Please enter a command (or [q] to quit): \n";
      getline(cin, com);
      if(com != "q"){
        commands.push_back(com);
        control = control + 1;
        cout << "You have " << control << " command/s\n";
        continue;
      }
      break;
      }
  }
  else{
    throw new string; "Exit status: \"Manual termination\"\n";
  }
  cout << "\n";
  
  /* Prompts the user whether or not they want to continue
  with the process */
  cout << "Final command count: " << control << "\n";
  this_thread::sleep_for(chrono::seconds(1));
  cout << "Would you like to continue? ([y]es or [n]o): \n";
  cin >> cont;
  
  /* This function executes the commands stored in the commands{} list.
  For whatever reason, c++ executes a function at the same time as it's
      declaration if not coded in a different source file in a certain way,
      and will end the program if a function is excecuted this way after it has
      finished...
  It still works though as it is declared at the very end and still returns
      the exit status(hopefully this meets the parameters). */
  string finish(cont);{
    if (cont == "y"){
      cout << "How long do you want the initialization to wait(in seconds)?\n";
      cin >> initDelay;
      cout << "How long do you want each command to wait after the previous?\n";
      cin >> intervalDelay;
      this_thread::sleep_for(chrono::seconds(initDelay));
      while(commands.size() != 0){
        cmd = commands.front();
        
        // c++ weirdness...
        const char* sh = cmd.c_str();
        system(sh);
        
        commands.pop_front();
        this_thread::sleep_for(chrono::seconds(intervalDelay));
      }
    }
    else {
      cout << "Aborting...\n";
    }
    cout << "The program has finished. Would you like to clear the terminal?\n";
    cin >> clear;
    if(clear == "y"){
      system("clear");
    }
    return 0;
  }
  return 0;
}