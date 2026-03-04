from inventory import calculate_total_stock_value

vendor = {
    "name": "Prajwal Traders",
    "contact": "7000165733",
    "email": "prajwalkatkar.cse24@sbjit.edu.in",
    "association_year": 2010
}


def generate_annual_purchase_report():
    total_value = calculate_total_stock_value()

    print("\n------ Annual Purchase Report ------")
    print("Vendor Name:", vendor["name"])
    print("Contact:", vendor["contact"])
    print("Email:", vendor["email"])
    print("Association Year:", vendor["association_year"])
    print("Total Purchase Value:", total_value)
    print("-----------------------------------")