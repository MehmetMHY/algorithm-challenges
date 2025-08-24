// Mines CSCI 262 Project 5 Animal Code
// May 2019

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<string> past;
vector<string> text;
vector<string> lines;
bool logo_yes_no;

struct node{
    string data;
    struct node* left;
    struct node* right;
};

//--------------------------------------------------------------------------------------
//----*The code between the lines are used to test the binary tree of this program.-----
//----*TESTING ONLY! MAINLY FOR THE DEVELOPER! NOT PART OF MAIN CODE!-------------------
//--------------------------------------------------------------------------------------
bool history(struct node *root, string goal) {
    if(root == NULL){
        return false;
    }
    if(root->data == goal){
        return true;
    }
    if(history(root->left, goal) || history(root->right, goal)){
        cout << root->data << "->";
        return true;
    }
    return false;
}
int count(struct node *root) {
    if (root == NULL){
        return 0;
    }
    return 1 + count(root->left) + count(root->right);
}
void test_it(struct node *root, int b, bool pick, bool on_off, string w){
    if(on_off == true){
        cout << endl << "[ TEST MODE ON - Comment out to turn off ]" << endl;

        if(pick == false && b < lines.size()){
            w = lines[b];
        }

        for(int i=0;i<lines.size();i++){
            cout << i << ") " << lines[i] << endl;
        }

        cout << endl;
        history(root, w);
        cout << "[END]" << endl;
        cout << "*Total Nodes: " << count(root) << endl << endl;

        //string w = lines[10];for(int i=0;i<lines.size();i++){cout<<i<<") "<<lines[i]<<endl;}cout<<endl;printAncestors(root, w);cout<<"[END]"<<endl;cout<<"*Total Nodes: "<<count(root)<<endl;
    }
}
//--------------------------------------------------------------------------------------

struct node* newnode(string data) {
    struct node* node = (struct node*) malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return(node);
}

struct node* read_game_tree(vector<string> lines) {
    struct node *root = newnode(lines[0]);
    struct node *p = root;
    stack<node *> mp; //Saved Not_Full nodes

    for(int i = 1; i < lines.size(); i++){
        string check = lines[i].substr(0,2);
        if(check == "#Q"){
            if(p->left == NULL || mp.size() == 1){
                p->left = newnode(lines[i]);
                mp.push(p);
                p = p->left;
            }else{
                p->right = newnode(lines[i]);
                mp.push(p);
                p = p->right;
            }
        }
        else if(check == "#A"){
            if(p->left == NULL){
                p->left = newnode(lines[i]);
            }else{
                p->right = newnode(lines[i]);
                p = mp.top();
                mp.pop();
            }
        }

    }
    return root;
}

void play_again(struct node *root){
    string input;

    while(true){
        cout << "Would you like to expand the game tree (y/n)? " << endl;
        cin >> input;
        if(input == "y"){
            break;
        }
        else if(input == "n"){
            break;
        }
        else{
            cout << "Error, only enter y or n!" << endl << endl;
        }
    }

    if(input == "y"){
        cout << "I asked the following: " << endl;
        for(int i = 0; i < past.size(); i++){
            cout << past[i] << endl;
        }
        string question;
        string answer;

        cout << "Enter a new animal in the form of a question," << endl;
        cout << "e.g., 'Is it a whale?': " << endl;
        getline(cin, question);
        getline(cin, question);
        question = "#Q " + question;

        cout << "Now enter a question for which the answer is 'yes' for your new" << endl;
        cout << "animal, and which does not contradict your previous answers:" << endl;
        getline(cin, answer);
        answer = "#A " + answer;

        string s = root -> data;
        root -> data = question;
        root -> left = newnode(answer);
        root -> right = newnode(s);
    }

    cout << endl;
    past.erase(past.begin(), past.end());
}

void play_game(struct node *root){
    string input;
    while(true){
        string ans;
        string que = root->data;
        string question = que.substr(3, que.length());
        cout << question << " (y/n): " << endl;
        cin >> ans;

        if(ans == "y"){
            if(root->left != NULL){
                input = root->data; input += " YES";
                past.push_back(input.substr(3, input.length()));
                root = root->left;
            }else{
                cout << "YAY! I guessed your animal!" << endl << endl;
                input = root->data; input += " YES";
                past.push_back(input.substr(3, input.length()));
                break;
            }
        }
        else if(ans == "n"){
            if(root->right != NULL){
                input = root->data; input += " NO";
                past.push_back(input.substr(3, input.length()));
                root = root->right;
            }else{
                cout << "BOO! I don't know!" << endl << endl;
                input = root->data; input += " NO";
                past.push_back(input.substr(3, input.length()));
                //Wanna Try Again?
                play_again(root);
                break;
            }
        }
        else{
            cout << "Error, only enter y or n!" << endl << endl;
        }
    }
}

void preorder(struct node *root){
    if (root != NULL) {
        text.push_back(root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void save_game_tree(struct node *root){
    preorder(root);
    std::ofstream outfile ("save.txt");

    for(int b = 0; b < text.size(); b++){
        outfile << text[b] << endl;
    }

    outfile.close();
    text.erase(text.begin(), text.end());
}

void delete_game_tree(struct node *root){
    cout << "---------------------------------------------------" << endl;
    cout << "Shutting Down";

    for(int i = 0; i < 51-13; i++){
        cout << ".";
    }

    cout << endl << "---------------------------------------------------" << endl;
    past.clear();
    text.clear();
    lines.clear();

    if(root != NULL) {
        root = NULL;
        preorder(root->left);
        preorder(root->right);
    }
}

void print(bool on_off){
    if(on_off){
        cout << "---------------------------------------------------" << endl;
        cout << "                       @((#,  ,###@              \n"
                "          @@#&@,   %(     ((###     /%           \n"
                "   @  @/       .&.(      ##@@@#%      &          \n"
                "  ( #          ##*        &  @&&      &          \n"
                "  ( .(@@(    ### ##        &@@&     *&           \n"
                "  ((@@#          %%%%%          &&&@@            \n"
                "  &@%#         %&&&&%*.,,,.(&&@@@                \n"
                "  @#. *%%&@.///***********/////*/****&           \n"
                " @%%@@@@,***********,,,,,,,**************@       \n"
                "      .,,,,,,,,,,,,,,,,/@@@@@@@%************/    \n"
                "     %,,,,,,,,,,,,....@@      &@#.***********.   \n"
                "    @................@@        .&(,,,,,,******/  \n"
                "    &.............../@          @/.,,,,,,,,,,,,  \n"
                "     @..............&@          %(.............  \n"
                "     .@..............@         @@%............@  \n"
                "       @*,,,,,.......@@       @@%............@   \n"
                "         @@,,,,,,,,,..*@&@@@@@%,,,,........#@    \n"
                "            @@@*****,,,,,,,,,,,,,,,,,,,,*@*      \n"
                "             @@******************(&@@&@@@@@*     \n"
                "             @,@@@@@@@@@*//////////#@@@@///.     \n"
                "                         @@///////////(//*       \n"
                "                           ,@.////////(@ @     " << endl;
        cout << "---------------------------------------------------" << endl;
    }else{
        cout << "---------------------------------------------------" << endl;
    }

    cout << "Welcome to 20 questions!" << endl;
    cout << "  1) Play the game" << endl;
    cout << "  2) Save the game file" << endl;
    cout << "  3) Quit" << endl;
    cout << "Please make your selection (1, 2, or 3): ";
    cout << endl << "---------------------------------------------------" << endl;
}

int main() {
    ifstream in("animal.txt");
    string str;
    while (std::getline(in, str)){
        if(str.size() > 0){
            lines.push_back(str);
        }
    }

    in.close();
    node* root = read_game_tree(lines);
    if(root == NULL){
        return -1;
    }

    while(true){
        string logo;
        cout << "Would you like to print the logo every time?" << endl;
        cout << "  1) YES" << endl;
        cout << "  2) NO" << endl;
        cout << "Please make your selection (1 or 2): " << endl;
        cin >> logo;
        if(logo == "1"){
            logo_yes_no = true;
            cout << "[ no logo will be displayed from now on ]" << endl << endl;
            break;
        }else if(logo == "2"){
            logo_yes_no = false;
            cout << "[ the logo will be displayed from now on ]" << endl << endl;
            break;
        }else{
            cout << "Sorry, I don't understand." << endl << endl;
        }
    }

    while (true) {
        string tmp;
        int choice;

        //• print(bool): Prints Welcome text to terminal and, if true, the 20 Questions logo image
        //• In print(bool), change the True to a False to remove the 20 Questions logo print. Leave
        //  the True if you want to keep printing the 20 Questions logo.

        print(logo_yes_no);

        cout << "ENTER HERE: ";
        cin >> tmp;
        choice = atoi(tmp.c_str());

        //• test_it: Used to test the position of a certain node. How to use it is the comment below.
        //  (root, node #, [true = pick from vector element & false = use custom string], on/off boolean, custom string)
        //• Uncomment the line below to use to function if you want to.

        //test_it(root, 6, false, true, "NA");

        switch (choice) {
            case 1:
                play_game(root);
                break;
            case 2:
                save_game_tree(root);
                cout << "[ Game Saved ]" << endl << endl;
                break;
            case 3:
                delete_game_tree(root);
                break;
            default:
                cout << "Sorry, I don't understand." << endl << endl;
        }

        if(choice == 3){
            break;
        }
    }
    return 0;
}