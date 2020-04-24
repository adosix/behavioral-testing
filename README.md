# OPENCART: Tests
I focused on vital parts of functionality for e-shop which are user registration, logging in and also shopping routine
## account
For account I prepared scenarios which ensure that any user can create his account and also log-in to it. I prepared few scenarios where required fields won't be filled or filled with incorrect formats of data.
- correct user registration
- user registration, unfilled fields
- user registration, wrong data
- user logging in
- wrong user logging in, wrong credentials
- wrong user logging in, unfilled field
## shopping
As for shopping I tried to cover basic functionality which is adding items to the shopping cart and going through checkout forms. All scenarios are for registered user as for unregistered user.
### registered user
- Registered user adds item to cart
- Registered user adds the same item to the cart twice
- Registered user clicks on checkout
- Registered user submits Billing details
- Registered user submits payment method
- Registered user submits payment method without confirmed terms
- Registered user confirms order
### unregistered user
- Unregistered user adds item to cart
- Unregistered user adds the same item to the cart twice
- Unregistered user click on checkout
- Unregistered user select guest checkout option 
- Unregistered user submits Billing details
- Unregistered user submits payment method
- Unregistered user submits payment method without confirmed terms
- Unregistered user confirms order