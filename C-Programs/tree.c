#include <errno.h>
#include <dirent.h>
#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

void printSpacing(int amount){
    int i;
    for(i = 0; i < amount; ++i){
        printf("\t");
    }
}

char * my_strcat(char *a, char *b){
	int x = strlen(a);
	int i;
	for(i = 0; i < strlen(b); i++){
		a[x + i] = b[i];
	}
}

void tookDir(int spaceNum, DIR *folder, char *dirPATH) {
    struct dirent *point;
	while((point = readdir(folder)) != NULL){

		char temp[PATH_MAX] = "";

		char point_to_string[PATH_MAX];
		char slash[] = "/";
		strncpy(point_to_string, point->d_name, PATH_MAX);

		strncat(temp, dirPATH, PATH_MAX);
		strncat(temp, point_to_string, PATH_MAX);
		
		char buf[PATH_MAX];
		ssize_t len = readlink(temp, buf, sizeof(buf)-1);

		strncat(temp, slash, PATH_MAX);

		DIR *isDir = opendir(temp);

		if(isDir != NULL){
			if(strcmp(point->d_name,"..") != 0 && strcmp(point->d_name, ".")){
				printSpacing(spaceNum);
				printf("%s", point->d_name);

				if(len != -1){
					printf(" -> ");
					buf[len] = '\0';
					printf("%s", buf);
					printf("\n");

				}else if(point->d_type == DT_DIR){
					printf("\n");
					char tempDir[PATH_MAX] = "";
					strncat(tempDir, temp, PATH_MAX);
					tookDir(spaceNum+1, isDir, tempDir);
				}else{
					printf("\n");
				}
			}
		}else if(errno == EACCES){
			printSpacing(spaceNum);
			printf("%s", point->d_name);
			printf(" [Error: %s]", strerror(errno));
			printf("\n");
		}else{
			printSpacing(spaceNum);
			printf("%s", point->d_name);
			if(len != -1){
					printf(" -> ");
					buf[len] = '\0';
					printf("%s", buf);
					printf("\n");
			}
			printf("\n");
		}

		closedir(isDir);
	}
}


int main(int argc, char *argv[]){

	char PATH[PATH_MAX] = "./";

	if(argv[1] != NULL){
		char slash[] = "/";
		strncpy(PATH, argv[1], PATH_MAX);
		strncat(PATH, slash, PATH_MAX);
	}

	DIR *folder = opendir(PATH);
	
	if(folder == NULL) {
		fprintf(stderr, "Error: ");
		printf("%s\n", strerror(errno));
		return(1);
	}else{
		tookDir(0, folder, PATH);
	}
	closedir(folder);

	return 0;
}


