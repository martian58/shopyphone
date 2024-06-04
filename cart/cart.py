from store.models import Product

class Cart():
    def __init__(self,request) -> None:
        self.session = request.session

        # Get the session key if it already exist
        cart = self.session.get('session_key')

        # If the user is new, then create a session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart


    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    

    def get_products(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids) 

        return products
    
    def remove(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def cart_total(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids) 
        
        # quantities = self.cart

        total = 0

        for product in products:
                total += product.price

        return total

