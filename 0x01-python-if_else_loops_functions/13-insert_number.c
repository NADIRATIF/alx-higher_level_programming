#include "lists.h"

/**
 * insert_node - Inserts a number.
 * @head: pointer.
 * @number: number to insert.
 * Return: NULL.
 *         Otherwise - a pointer.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *h, *n;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->n = number;

	if (nd == NULL || nd->n >= number)
	{
		n->next = nd;
		*h = n;
		return (n);
	}

	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;

	n->next = nd->next;
	nd->next = n;

	return (n);
}

