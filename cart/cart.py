class Cart():
    def __init__(self,request) -> None:
        self.session = request.session

        # Get the session key if it already exist
        cart = self.session.get('session_key')

        # If the user is new, then create a session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart