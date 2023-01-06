#include "lists.h"



size_t count_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
	//printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}




/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head node
 * Return: 1 if palindrome and 0 if not
 */



int is_palindrome(listint_t **head)
{
unsigned int num = count_listint((const listint_t *) *head);
int num_arr[num / 2];
size_t i;
for (i = 0; i < num / 2; i++)
{
	num_arr[i] = (*head)->n;
	*head = (*head)->next;
}

if (num % 2 > 0)
	*head = (*head)->next;

i -= 1;
while (*head != NULL)
{
if ((*head)->n != num_arr[i])
	return (0);

*head = (*head)->next;
i--;
}

return (1);
}
