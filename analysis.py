import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def get_customers(url: str = API_URL) -> list[dict]:
    """Fetch the customer list. Report failures clearly instead of crashing."""
    try:
         customers =  requests.get(url,timeout= 15)
         customers.raise_for_status()
         return customers.json()

    except requests.exceptions.RequestException as problem:
        print(f"Customer data cannot be found: {problem}. Network issue occurred ")
        return[]
     
    # raise NotImplementedError



# def explore(record: dict, indent: int = 0) -> None:
#     """Print every key in a (possibly nested) record with its type, indented by depth."""
#     raise NotImplementedError

def explore(record: dict, indent: int = 0) -> None:
    """Print each key and value type, exploring nested data."""
    space = " " * indent

    for key, value in record.items():
        print(f"{space} {key}: {type(value).__name__} ")

        if isinstance(value, dict):
            explore(value , indent +2)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item,dict):
                    explore(item, indent + 2)      
       


def extract_attributes(customers: list[dict]) -> list[dict]:
    """Return one flat dict per customer with the attributes listed in the task."""
    customer_details = []

    for customer in customers:
        attributes = {
            "id": customer["id"],
            "name": customer["name"],
            "username": customer["username"],
            "email": customer["email"],
            "street" : customer["address"]["street"],
            "suite" : customer["address"]["suite"],
            "city" : customer["address"]["city"],
            "zipcode": customer ["address"]["zipcode"],
            "latitude":float(customer["address"]["geo"]["lat"]),
            "longitude":float(customer["address"]["geo"]["lng"]),
            "phone": customer["phone"],
            "website": customer ["website"],
            "company":customer["company"]["name"],
            "catchphrase" : customer["company"]["catchPhrase"],
            "bs":customer["company"]["bs"]

        }

        customer_details.append(attributes)

    return customer_details

#     raise NotImplementedError

def unique_cities(customers: list[dict]) -> set[str]:
    """Return the set of distinct cities."""
    city_names = set()

    for customer in customers:
        city = customer["address"]["city"]
        city_names.add(city)

    return city_names

#Each customer comes from a different city in this dataset, suggesting that marketing should explore location-specific opportunities rather than focusing only on a few customer hubs

    # raise NotImplementedError


def city_counts(customers: list[dict]) -> dict[str, int]:
    """Count customers per city using a loop and/or a dict comprehension (no Counter, no pandas).""" 
    city_total = {}

    for customer in customers:
        city = customer["address"]["city"]

        if city in city_total:
            city_total[city] = city_total[city] + 1
        else:
            city_total[city] = 1

    return city_total


#     raise NotImplementedError

def email_domain_counts(customers: list[dict]) -> dict[str, int]:

    email_counts = {}

    for customer in customers:
        email = customer["email"]
        domain = email.split(".")[-1]

        if domain in email_counts:
            email_counts[domain] +=1
        else:
            email_counts[domain] = 1
            
    return email_counts



    # raise NotImplementedError


def to_dataframe(rows: list[dict]) -> pd.DataFrame:
    table = pd.DataFrame(rows)
    return table


    # raise NotImplementedError


def plot_distribution(counts: dict[str, int], path: Path) -> None:
    """Save a labelled chart of the distribution to path."""
    plt.figure(figsize=(12,6))

    categories = counts.keys()
    numbers = counts.values()

    plt.bar(categories,numbers)

    plt.title("Customer chart")
    plt.xlabel("category")
    plt.ylabel("no of customers")

    plt.savefig(path)
    plt.close()

 
#     raise NotImplementedError



if __name__ == "__main__":

    customers = get_customers()

    if customers:
        explore(customers[0])
        customer_details = extract_attributes(customers)
        city_names = unique_cities(customers)
        print("Unique cities:", city_names)

        city_results = city_counts(customers)
        print("Customers per city:", city_results)

        email_results = email_domain_counts(customers)
        print("Customers per email domail:", email_results)

        table = to_dataframe(customer_details)
        print(table)

        Path("visuals").mkdir(exist_ok=True)
        plot_distribution(
            city_results,
            Path("visuals/customer_distribution.png")
        )
        plot_distribution(
            email_results,
            Path("visuals/email_distribution.png")
        )

    else:
        print("Customer data unaivailable")





