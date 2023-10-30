#include "lists.h"
/**
 * check_cycle - check if link list is cyclic
 * @list: lists
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *last;

	if (!list || !list->next)
		return (0);
	first = list;
	last = list;

	while (last != NULL && first != NULL && first->next != NULL)
	{
		last = last->next;
		first = first->next->next;
		if (first == last)
		{
			return (1);
		}
	}
	return (0);
}
