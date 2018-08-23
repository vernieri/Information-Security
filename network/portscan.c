#include <stdio.h>
#include <netdb.h>

main(int argc, char *argv[]){

	int port;
	int init;
	int limit = 65535;
	char * ip;
	ip = argv[1];

	int mysock;
	int con;

	struct sockaddr_in target;

	for(port=init;port<limit;port++){

		mysock = socket(AF_INET, SOCK_STREAM, 0);
		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(ip);

		con = connect(mysock, (struct sockaddr *) &target, sizeof target);

		if(con == 0){
			printf("[+] PORT %d is OPEN \n", port);
			close(mysock);
			close(con);
		}
		else{

			//printf("Nah, its closed... \n");
			close(mysock);
			close(con);
		}
	}


}

//gcc -o portscan portscan.c
