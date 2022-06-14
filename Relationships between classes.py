class Customer:  # class declaration
    def __init__(self, name, email, mobile, address, id):  # constructor
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.id = id


class Order:
    def __init__(self, order_number, product_id, price, shipping_address):
        self.order_number = order_number
        self.product_id = product_id
        self.price = price
        self.shipping_address = shipping_address

    def calcShipping(self, cost):
        self.cost = cost
        if cost > 40:
            y = 0
        else:
            y = 5
            return y

    def calcTotal(self, item_price, shipping_price):
        self.item_price = item_price
        self.shipping_price = shipping_price
        x = item_price + shipping_price
        return x

    def sendReceipt(self, email, id, shipping_address, item_name, total):
        self.email = email
        self.id = id
        self.total = total
        self.item_name = item_name
        self.shipping_address = shipping_address
        print("Send email receipt to - ", email, "Product ID = ", id, "Item Name = ", item_name, "Shipping Address = ",
              shipping_address, "Total Cost = £", total)


class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price


class Payment:
    def __init__(self, id, total, date, payment_details, name, email):
        self.id = id
        self.total = total
        self.date = date
        self.payment_details = payment_details
        self.name = name
        self.email = email

    def checkPaymentAccepted(self):
        print("this method would be used to verify payment had gone through successfully.")



customer = Customer("talon", "talon@xyz.com", "0777777777", "example address", 1)  # create customer obj

product = Product("1", "T-shirt", "Tops", 10)  # create product obj

order = Order("1", "1", 50, customer.address)  # create order obj

payment = Payment(customer.id, order.calcTotal(product.price, order.calcShipping(product.price)), "sample date", "sample payment details", customer.name, customer.email)

order.sendReceipt(customer.email, product.product_id, customer.address, product.name,
                  order.calcTotal(product.price, order.calcShipping(product.price)))


# sendReceipt method shows the relationship between different Classes. The Order class relies on both Product and
# Customer Classes by using their attributes in the method call. Payment Class uses the Customer ID and the Customer
# Name from the Customer class to keep track of payment and as part of the payment details.
# Payment also shared relationship with Order Class, to gain price information.
