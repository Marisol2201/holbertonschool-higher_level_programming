#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	while (fast && fast->next)/*Empty list has no loop.*/
	{
		slow = slow->next;          /*1 hop*/
		fast = fast->next->next;     /*2 hops*/

		if (slow == fast)  /*fast caught up to slow, so there is a loop*/
			return (1); /*true*/
	}
	return (0);  /*fast reached null, so the list terminates*/
}
