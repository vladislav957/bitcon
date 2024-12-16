#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

const int PORT = 5000;
const char*SERVER_IP = "192.168.1.100"; //Заменить на IP серверна

int main(){
    struct sockaddr_in server_addr;
    char buffer[1024] = {0};
    
    //Создание сокета
    if((client_fd = socket(AF_INET,SOCK_STREAM, 0))<0){
                  perror("Ошибка создания сокета");
                  return 1;
                  
                  }
                  
                  server_addr.sin_family = AF_INET;
                  server_addr.sin_port = htons(PORT);
                  
                  //Преобразование IP-адреса
                  if(inet_pton(AF_INET,SERVER_IP,&server_addr.sin_addr)<=0){
                  perror("Неверный адрес/адес не поддерживается");
                  close(client_fd);
                  return 1;
                  
                  }
                  
                  //Подключение к серверу
                  if(connect(client_fd,(struct sockaddr*)&server_addr, sizeof(server_addr))<0){
                                               rerror("Ошибка подключения");
                                               close(client_fd);
                                               return 1;
                                               }
                                               
                                               //Отправка данных
                                               const char* message = "Привет от клиента!";
                                               send(client_fd, message, strlen(message), 0);
                                               std::cout<<"Сообщение отправлено."<<std::endl;
                                               
                                               //Получение ответа
                                               read(cliennt_fd,buffer,1024);
                                               std::cout<<"Ответ от сервера:"<<buffer<<std::endl;
                                               
                                               close(client_fd);
                                               return 0;
                                               
                                               }
                                                
                                                                            
                           
