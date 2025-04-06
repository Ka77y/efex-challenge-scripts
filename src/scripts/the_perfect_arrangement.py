from typing import List
from src.models.customer import Customer


def arrange(customer_list: List[Customer]) -> List[Customer]:
    result_list: List[Customer] = []
    for customer in customer_list:
        mixed_name = customer.first_name + customer.last_name
        if len(mixed_name) < 12:
            customer.mixed_name = mixed_name
            result_list.append(customer)

    result_list.sort(key=lambda customer: (len(customer.mixed_name), customer.mixed_name.lower(), customer.mixed_name, customer.id))

    return result_list

