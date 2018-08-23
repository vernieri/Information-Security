#include <stdio.h>
#include <netdb.h>

main(){

	int mysock;
	int con;

	struct sockaddr_in target;

	mysock = socket(AF_INET, SOCK_STREAM, 0);
	target.sin_family = AF_INET;
	target.sin_port = htons(80);
	target.sin_addr.s_addr = inet_addr("TARGET_IP");

	con = connect(mysock, (struct sockaddr *) &target, sizeof target);
	
	if(con == 0){
		printf("Open Door \n");
		close(mysock);
		close(con);
	}
	else{

		printf("Nah, its closed... \n");
	}


}

//gcc -o socket socket.c
