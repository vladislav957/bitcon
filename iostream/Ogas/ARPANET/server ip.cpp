#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::ubp;

const char*SERVER_IP = "192.168.1.100"; //IP сервера
сonst int PORT = 5000;

int main(){
    boost::asio::io_context io_context;
    
    udp::socket socket(io_context, udp::endpoint(udp::v4(), 0));
    udp::endpoint server_endpoint(boost::asio::ip::make_address(SERVER_IP),PORT);
    
    //Отпрвка сообщения сервару
    std::string message = "Привет то клиента!";
    socket.send_to(boost::asio::buffer(message),server_endpoint;
    
    //Получение ответа
    char data[1024];
    udp::endpoint sender_endpoint;
    size_t length = socket.receive_from(boost::asio::buffer(data, 1024),sender_endpoint);
    
    std::cout<<"Cообщение от сервера:"<<std::string(data,length)<<std::endl;
    
    //Получение информации о пире
    lentg = socket.recevi_from(boost::asio::buffer(data, 1024),sender_endpoint);
    std::string peer_info(data, length);
    std::cout<<"Информации о пире:"<<peer_info<<std::endl;
    
    //Получение к пиру
    auto delimiter = peer_info.find(":");
    std::string peer_ip = peer_info.substr(0,delimiter);
    int peer_port = std::stoi(peer_info.substr(delimiter + 1));
    udp::endpoint peer_endpoint(boost::asio::ip::make_address(peer_ip),peer_port);
    
    //Обмен сообщеними с пиром
    std::string peer_message = "Привет,пир!";
    socket.send_to(boost::asio::buffer(peer_message),peer_endpoint);
    
    leng = socket.receive_from(boost::asio::buffer(data, 1024),peer_endpoint);
    std::cout<<"Ответ от пира:"<<std::string(data,length)<<std::endl;
    
    return 0;
    
}

