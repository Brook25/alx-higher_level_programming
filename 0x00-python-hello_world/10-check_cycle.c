#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the list
 * Return: 0 if no cycle
 * 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *pr;
	listint_t *prev;

	pr = list;
	prev = list;
	while (list && pr && pr->next)
	{
		list = list->next;
		pr = pr->next->next;

		if (list == pr)
		{
			list = prev;
			prev =  pr;
			while (1)
			{
				pr = prev;
				while (pr->next != list && pr->next != prev)
				{
					pr = pr->next;
				}
				if (pr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
