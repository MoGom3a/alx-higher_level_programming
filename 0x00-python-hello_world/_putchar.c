#include <unistd.h>
#include "main.h"

/**
 *_putchar - Write the char
 *@c: the char to prtint
 *
 *Return: 1 (success) & -1 (error)
 */
int_putchar(char c)
{
	return (write(1, &c,1));
}
