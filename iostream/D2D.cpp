#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::udp;

int main(){
    try{
        boost::asio::io_context(io_contxt, udp::endpoint(udp::v4(),0));
        std::string message = "D2D!";
        udp::endpoint target(boost::asio::ip::address:from_string("..")8080);
        
        socket.send_to(boost::asio::buffer(message),targt);
        
        char reply[1024];
        udp::endpoint sender_endpoint;
        size_t reply_length = socket.receive_from(boost::asio::buffer(reply),sender_endpoint);
        std::cout<<"Reply:"<<std::strng(reply,reply_length)<<std::endl;
        
        }cotch(std::exception& e){
                               std::cerr<<"Error:"<<e.what()<<std:;endl;
                               }
                               return 0;
                               }
