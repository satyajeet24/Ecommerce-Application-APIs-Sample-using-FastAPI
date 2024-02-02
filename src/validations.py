def filter_validations(filter_dict):
    min_price = filter_dict.get("min_price")
    max_price = filter_dict.get("min_price")

    if min_price and min_price < 0:
        raise AttributeError("min_price filter should be of non-negative value")

    if max_price and max_price < 0:
        raise AttributeError("max_price filter should be of non-negative value")


def order_validations(order_dict):
    if not order_dict:
        raise AttributeError("Order is Empty")

    product_items = order_dict.get("items")
    total_amount = sum(item.get("totalAmount") for item in product_items)

    if total_amount <= 0:
        raise AttributeError("total amount of the products of the order should be of non-negative value")

    if not order_dict.get("userAddress"):
        raise AttributeError("User's Address was not present along with Order details.")

    #TODO
    # We may further validate about the orders items


