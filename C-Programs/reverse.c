/*
 * Class: Operating System (CSCI442)
 * Project: Project 1 - Warm Up
 * Date: 1-21-2022
 * By: Mehmet Yilmaz
 * 
 * CREDIT(s):
 *		- Linux Programmer's Manual (Man Command) For GETLINE(3):	prompt> man 3 getline
 *		- Linux Programmer's Manual (Man Command) For FPRINTF(3):	prompt> man 3 fprintf
 *		- Linux Programmer's Manual (Man Command) For ERRNO(3):	prompt> man 3 errno
 *		- Project 1's GitHub Page: https://github.com/CSCI-442-Mines/project-1-MehmetMHY
 *		- C_Programming_Review.pptx lecture provided by CSCI442
 *		- Ismail Sahal - Helping me debug some heap buffer overflow bugs
 *		- Piazza Question Posts: @46, @57, @67, and @70
 *		- Linux Kernel Coding Style: https://www.kernel.org/doc/html/v5.8/process/coding-style.html
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[])
{
	FILE *input_file = NULL;
	FILE *output_file = NULL;

	if (argc != 2 && argc != 3) {
		fprintf(stderr, "usage: reverse <input> <output>\n");
		exit(1);
	}

	input_file = fopen(argv[1], "r");
	
	if (input_file == NULL) {
		fprintf(stderr, "error: cannot open file '%s'\n", argv[1]);
		exit(1);
	}

	if (argc == 3) {
		int arg1size = sizeof(argv[1]) * sizeof(char);
		int arg2size = sizeof(argv[2]) * sizeof(char);
		
		// determine largest argument size to set size_t to strncmp
		int argsize = arg1size;
		if (arg1size < arg2size) {
			argsize = arg2size;
		}

		int same_string = strncmp(argv[1], argv[2], arg1size);
		if (errno != 0) {
			fprintf(stderr, "error: strncmp failed\n");
			exit(1);
		}

		if (same_string == 0) {
			fprintf(stderr, "error: input and output file must differ\n");
			exit(1);
		}

		output_file = fopen(argv[2], "w");
		if (output_file == NULL) {
			fprintf(stderr, "error: cannot open file '%s'\n", argv[2]);
			exit(1);
		}
	}

	int line_count;

	char *line = NULL;
	size_t len = 0;
	size_t nread;

	int c = 0;
	while(1) {

		nread = getline(&line, &len, input_file);
		if (errno != 0) {
			fprintf(stderr, "error: getline failed\n");
			exit(1);
		}

		if (nread == -1) {
			line_count = c;
			break;
		}

		c = c + 1;
	}

	free(line);
	if (errno != 0) {
		fprintf(stderr, "error: free failed\n");
		exit(1);
	}

	fclose(input_file);
	if (errno != 0) {
		fprintf(stderr, "error: fclose failed\n");
		exit(1);
	}

	// used to store every line in input_file
	char **all_lines = (char **)malloc(line_count * sizeof(char*));

	if (all_lines == NULL) {
		fprintf(stderr, "error: malloc failed\n");
		exit(1);
	}

	input_file = fopen(argv[1], "r");

	if (input_file == NULL) {
		fprintf(stderr, "error: cannot open file '%s'\n", argv[1]);
		exit(1);
	}

	line = NULL;
	len = 0;

	c = 0;
	while(1) {
		nread = getline(&line, &len, input_file);
		if (errno != 0) {
			fprintf(stderr, "error: getline failed\n");
			exit(1);
		}

		if (nread == -1) {
			break;
		}

		char *arr = (char *)malloc((nread+1) * sizeof(char));
		if (arr == NULL) {
			fprintf(stderr, "error: malloc failed\n");
			exit(1);
		}

		int i;
		for (i = 0; i < nread; i++) {
			arr[i] = line[i];
		}

		// add NULL to end of string (char *)
		arr[nread] = '\0';

		all_lines[c] = arr;
		c = c + 1;
	}

	// loop array of lines in reverse
	int x;
	for (x = line_count-1; x >= 0; --x) {

		if (output_file == NULL) {
			fprintf(stdout, "%s", all_lines[x]);
		}else{
			fprintf(output_file, "%s", all_lines[x]);
		}

		free(all_lines[x]);
		if (errno != 0) {
			fprintf(stderr, "error: free failed\n");
			exit(1);
		}
	}

	free(all_lines);
	if (errno != 0) {
		fprintf(stderr, "error: free failed\n");
		exit(1);
	}

	free(line);
	if (errno != 0) {
		fprintf(stderr, "error: free failed\n");
		exit(1);
	}

	fclose(input_file);
	if (errno != 0) {
		fprintf(stderr, "error: fclose failed\n");
		exit(1);
	}

	if (output_file != NULL) {
		fclose(output_file);
		if (errno != 0) {
			fprintf(stderr, "error: fclose failed\n");
			exit(1);
		}
	}

	exit(0);
}

