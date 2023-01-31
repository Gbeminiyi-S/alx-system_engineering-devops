#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - Runs an infinite while loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	int count = 0;
	pid_t child_pid;

	while (count < 5)
	{
		child_pid = fork();

		if (child_pid == 0) /* child process */
			exit(0);
		else /* parent */
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(5);
		}
		count++;
	}
	infinite_while();

	return (0);
}
