#include <string.h>
#include <stdio.h>
#include <arpa/inet.h> //definitions for internet operations
#include <unistd.h> //standard symbolic constants and types
#define PORT 5001 //Server port
#include <thread>

//Variables
char nickname[20];
char message[120];
char userInput[100];
char buffer[1024] = {0};
int server = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in serv_addr;
bool flag = true;

//Listening to Server and Sending Nickname
void recieveMessage()
{
    while (true)
    {
        //Recieve Message From Server
        //If 'NICK' Send Nickname
        read(server, buffer, 1024);
        if (strcmp(buffer,"NICK") == 0)
        {
            memset(&buffer[0], 0, sizeof(buffer));
            send(server, nickname, strlen(nickname), 0);
        }
        else
        {
            printf("%s\n",buffer);
            memset(&buffer[0], 0, sizeof(buffer));
        }
    }
}

// Sending Messages To Server
void sendMessage()
{
    while (true)
    {
        memset(&message[0], 0, sizeof(message));
        memset(&userInput[0], 0, sizeof(userInput));
        fgets(userInput, 100, stdin);
        if(flag == false)
        {
            userInput[strlen(userInput)-1] = 0;
            strcpy(message,nickname);
            strcat(message,": ");
            strcat(message, userInput);
            send(server, message, strlen(message), 0);
        }
        flag = false;
    }
}

int main()
{
    // Choosing Nickname
    printf("Choose your nickname: ");
    scanf("%s",&nickname);

    //Connecting To Server
    serv_addr.sin_family = AF_INET; 
    serv_addr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, "25.59.220.176", &serv_addr.sin_addr) <= 0) //Server IP address
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
   
    if (connect(server, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
    { 
        printf("\nConnection Failed \n");
        return -1;
    }
    std::thread recieve_thread(recieveMessage);
    std::thread send_thread(sendMessage);
    recieve_thread.join();
    send_thread.join();
    return 0;
}