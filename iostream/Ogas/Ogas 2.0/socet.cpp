#include <iostream>
#include <csting>
#include <unistd.h>
#include <arpa/inet.h>

const int PORT = 5000;

int main(){
    int server_fd, client_fd;
    struct sockaddr_in server_addr,client_add;
    socklen_t client_let = sozeof(client_addr);
    char buffer[1024] = {0};
    
    // Созденение сокета
    if((server_fd = socket(AF_INET,SOCK_STREAM, 0)) == 0) {
                  perror("Ошибка создания сокета");
                  return 1;
                  }
                  
                 server _addr.sin_family = AF_INET;
                 server_addr.sin_addr.S_addr = INADDR_ANY;
                 server_addr.sin_port = htons(PORT);
                 
                 //Привязка сокета
                 if(bind(server_fd,(struct sockaddr*)&server_addr,sizof(servr_addr))<0){
                                           perror("Ошибка привязки");
                                           close(server_fd);
                                           return 1;
                                           }
                                           
                                           
                                           std::cout<<"Узел подключился!"<<std::endl;
                                           
                                           //Получение данные
                                           read(client_fd,buffer,1024);
                                           std::cout<<"Получено сообщение:"<<buffer<<std::endl;
                                           
                                           //Ответ клиенту
                                           const char*response = "Сообщение получено!;
                                           send(client_fd,response, strlen(response), 0);
                                           std::cout<<"Ответ отправлен.!"<<std::endl;
                                           
                                           close(client_fd);
                                           close(server_fd);
                                           return 0;
                                           
                                           }
                                           
                                           
