#include<iostream>
#include<string>
using namespace std;
class Account{
    public:
    int accountNumber;
    string accountHolderName;
    string accountType; // user/ admin- au diferite drepturi in functie de loggare
    double balance;
    Account(){ // declararea unui construct initial, inainte ca sa fie memorat vreun user
        accountNumber=0;
        accountHolderName="";
        accountType="";
        balance=0.0;

    }
};
void login(){
string userName;
string password;
cout<<"Welcome Admin- Please enter your credentialis..."<<endl;
cout<<"UserName: "<<endl;
cin>>userName;
cout<<"Password: "<<endl;
cin>>password;
if(userName=="Ardelean" && password=="123456"){
    cout<<"Access Granted!"<<endl;
}
else{
    cout<<"Acces Denied!\nTerminating the Program...."<<endl;
    exit(0); // functia din int prin care se opreste programul instant
}
}

int options(){
int choice;
cout<<"\n\n\nPlease select an option from below"<<endl;
cout<<"--------------------------------"<<endl;
cout<<"1. Add a new customer"<<endl;
cout<<"2. Delete an existing costumer's account"<<endl;
cout<<"3. Look for details of an existing customer"<<endl;
cout<<"4. Deposit the money"<<endl;
cout<<"5. Log out."<<endl;
cout<<"Enter your choice from above options: "<<endl;
cin>>choice;
return choice;
}
int deleteCustomer(int acNum, Account obj[]){ // metoda prin care putem aduce un obiect in functie
    for(int i=0;i<30;i++){
        if(obj[i].accountNumber==acNum){
            obj[i].accountNumber=0;
            obj[i].accountHolderName="";
            obj[i].accountType="";
            obj[i].balance=0.0;
            return 1;
        }
    }
return 0;
}
void fetchDetails(Account obj[]){
    int acNum, found=0;
    cout<<"Enter the account numuber: ";
    cin>>acNum;
    for(int i=0;i<30;i++){
        if(obj[i].accountNumber==acNum){
            cout<<"Customer's account Number: "<<obj[i].accountNumber<<endl;
            cout<<"Customer's Name: "<<obj[i].accountNumber<<endl;
            cout<<"Customer's account balance: "<<obj[i].balance<<endl;
            cout<<"Account Type: "<<obj[i].accountType<<endl;
            found=1;
            break;
        }
    }
    if(found==0){
        cout<<"\n Customer was not found in the system"<<endl;
    }
}
void deposit(Account obj[]){
    int acNum, found=0, amount;
    cout<<"Enter the amount to deposit: ";
    cin>>amount;
    cout<<"Enter the account Number";
    cin>>acNum;
    for(int i=0;i<30;i++){
        if(obj[i].accountNumber==acNum){
            obj[i].balance=obj[i].balance+amount;
            cout<<"\nMoney deposited successfully!";
            cout<<"Customer's account Number: "<<obj[i].accountNumber<<endl;
            cout<<"Customer's Name: "<<obj[i].accountNumber<<endl;
            cout<<"Customer's account balance: "<<obj[i].balance<<endl;
            cout<<"Account Type: "<<obj[i].accountType<<endl;
            found=1;
            break;
        }
    }
    if(found==0){
        cout<<"\n Customer was not found in the system"<<endl;
        cout<<"Returning the amount to the user"<<endl;
    }
}

int main(){
int choice;
int accountNumber=1000;
Account acc[30]; // crearea a 30 de obiecte ale clasei Account
int customer=0;
cout<<"--------Welcome to ABC Bank--------"<<endl;
cout<<"      *** Connecting Global ***"<<endl;
// asking the user to enter their details, if the credentials are correct, show them the optons
login();

//condition to check, user selected which option?
while(1){
    choice=options();  //if the credentials were correct, display them the options;
    if(choice ==1){
        cout<<"\nAdd new customer:"<<endl;
        acc[customer].accountNumber=accountNumber;
        cout<<"Enter the user's name"<<endl;
        cin>>acc[customer].accountHolderName; // functia prin care poti introduce numele intrec, cu tot cu spatii
        cout<<"Enter the account type current/saving/other:"<<endl;
        cin>>acc[customer].accountType;
        cout<<"How much is the initial amount: "<<endl;
        cin>>acc[customer].balance;
        customer++;
        accountNumber++;

    }
    else if(choice ==2){
        int acNum,work;
        cout<<"\n Delete an existing customer"<<endl;
        cout<<"Enter the account Number:"<<endl;
        cin>>acNum;
        work=deleteCustomer(acNum,acc);
        if(work==0){
            cout<<"Customer's Data was not found"<<endl;
        }
        else if(work==1){
            cout<<"Customer deleted successfully"<<endl;
        }
    }
    else if(choice ==3){
        cout<<"\n Fetch the user's details"<<endl;
        fetchDetails(acc);
    }
    else if(choice ==4){
        cout<<"\nDeposit the money"<<endl;
        deposit(acc);
    }
    else if(choice == 5){
        cout<<"\n Logging Out"<<endl;
        exit(0);
    }
    } 
}