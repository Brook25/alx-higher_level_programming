#include <stdlib.h>
#include "lists.h"

/**
 * inser_node - Inserts a num into a sorted singly linked list.
 * @head: a pointer to a pointer to a singly linked list
 * @number: value of new node
 * Return: The address of the new node, or NULL if it fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag1 = 0;
	listint_t *new_node = NULL, *actual = NULL, *after = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	actual = *head;
	if (number <= actual->n)
	{
		new_node->next = actual, *head = new_node;
		return (*head);
	}
	if (number > actual->n && !actual->next)
	{
		actual->next = new_node;
		return (new_node);
	}
	after = actual->next;
	while (actual)
	{
		if (!after)
			actual->next = new_node, flag1 = 1;
		else if (after->n == number)
			actual->next = new_node, new_node->next = after, flag1 = 1;
		else if (after->n > number && actual->n < number)
			actual->next = new_node, new_node->next = after, flag1 = 1;
		if (flag1)
			break;
		after = after->next, actual = actual->next;
	}
	return (new_node);
}
