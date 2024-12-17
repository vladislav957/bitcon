#include <iostream>
#include <csting>
#include <unistd.h>
#include <arpa/inet.h>
#include <Python.h>
#define SPAM_MODULE
#include "spammodule.h"

const int PORT = 5000;

static int
PySpam_System(const char *command)
{
    return system(command);
}

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
                                           PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject *m;
    static void *PySpam_API[PySpam_API_pointers];
    PyObject *c_api_object;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    /* Initialize the C API pointer array */
    PySpam_API[PySpam_System_NUM] = (void *)PySpam_System;

    /* Create a Capsule containing the API pointer array's address */
    c_api_object = PyCapsule_New((void *)PySpam_API, "spam._C_API", NULL);

    if (PyModule_AddObject(m, "_C_API", c_api_object) < 0) {
        Py_XDECREF(c_api_object);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

#ifndef Py_SPAMMODULE_H
#define Py_SPAMMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

/* Header file for spammodule */

/* C API functions */
#define PySpam_System_NUM 0
#define PySpam_System_RETURN int
#define PySpam_System_PROTO (const char *command)

/* Total number of C API pointers */
#define PySpam_API_pointers 1


#ifdef SPAM_MODULE
/* This section is used when compiling spammodule.c */

static PySpam_System_RETURN PySpam_System PySpam_System_PROTO;

#else
/* This section is used in modules that use spammodule's API */

static void **PySpam_API;

#define PySpam_System \
 (*(PySpam_System_RETURN (*)PySpam_System_PROTO) PySpam_API[PySpam_System_NUM])

/* Return -1 on error, 0 on success.
 * PyCapsule_Import will set an exception if there's an error.
 */
static int
import_spam(void)
{
    PySpam_API = (void **)PyCapsule_Import("spam._C_API", 0);
    return (PySpam_API != NULL) ? 0 : -1;
}

#endif

#ifdef __cplusplus
}
#endif

#endif /* !defined(Py_SPAMMODULE_H) */

PyMODINIT_FUNC
PyInit_client(void)
{
    PyObject *m;

    m = PyModule_Create(&clientmodule);
    if (m == NULL)
        return NULL;
    if (import_spam() < 0)
        return NULL;
    /* additional initialization can happen here */
    return m;
}
                                           
                                           
