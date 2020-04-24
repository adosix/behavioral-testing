Feature: testing shopping routine

Scenario: Registered user adds item to cart
Given user is logged in
And a web browser is at the home page of opencart
And user has empty cart
When user clicks on "ADD TO CART" under item
Then user has one item in the cart

Scenario: Registered user adds second item to the cart
Given user is logged in
And one item is in the cart
And a web browser is at the home page of opencart
When user clicks on "ADD TO CART" under item
Then there are two items in the cart

Scenario: Registered user clicks on checkout
Given user is logged in
And there are two items in the cart
When user clicks on the "checkout"
Then user is redirected to the checkout page

Scenario: Registered user submits Billing details
Given user is logged in
And a web browser is at the checkout page
When user fills billing details
And user clicks on the "continue"
Then payment method can be filled

Scenario: Registered user submits payment method
Given user is logged in
And a web browser is at the checkout page
And billing details were submited
When user confirms terms and conditions
And user clicks on the "continue"
Then Confirm order button is displayed

Scenario: Registered user submits payment method without confirmig terms
Given user is logged in
And a web browser is at the checkout page
And billing details were submited
When user does not confirm terms and conditions
And user clicks on the "continue"
Then user is promted that he has to confirm terms and conditions

Scenario: Registered user confirms order
Given user is logged in
And a web browser is at the checkout page
And billing details were submited
And payment method was accepted
When user clicks on the "Confirm Order"
Then order is created

Scenario: Unregistered user adds item to cart
Given user is not logged in
And a web browser is at the home page of opencart
When user clicks on "ADD TO CART" under item
Then item is added to the cart

Scenario: Unregistered user adds the same item to the cart twice
Given user is not logged in
And a web browser is at the page form which we added the item to the cart
When user clicks on "ADD TO CART" under the same item that is in the cart
Then there are is two items in the cart

Scenario: Unregistered user clicks on checkout
Given user is not logged in
And one item is in the the cart
When user clicks on the "checkout"
Then user is redirected to the checkout page


Scenario: Unregistered user select guest checkout option
Given user is not logged in
And a web browser is at the checkout page
When user selects "Guest Checkout"
And user clicks on the "continue"
Then user can fill billing details form

Scenario: Unregistered user submits Billing details
Given user is not logged in
And a web browser is at the checkout page
And user selected guest checkout option
When user fills correctly all required field in billing details form
And user clicks on the "continue"
Then payment method can be filled

Scenario: Unregistered user submits payment method
Given user is not logged in
And a web browser is at the checkout page
And billing details were submited
When user confirms terms and conditions
And user clicks on the "continue"
Then Confirm order button is displayed

Scenario: Unregistered user submits payment method without confirmig terms
Given user is not logged in
And a web browser is at the checkout page
And billing details were submited
When user does not confirm terms and conditions
And user clicks on the "continue"
Then user is promted that he has to confirm terms and conditions

Scenario: Confirming order
Given user is not logged in
And a web browser is at the checkout page
And payment method was accepted
When user clicks on the "Confirm Order"
Then order is created
