Feature: testing user registration, logging in, logging out



Scenario: correct user registration
Given unregistered user
And a web browser is at the register page of opencart
When user fills all required registration fields correctly
And user accepts terms of privacy policy
And user presses "Continue"
Then account is created
And user is logged in 

Scenario: user registration, unfilled fields
Given unregistered user
And a web browser is at the register page of opencart
When user fills required registration fields with incorrect data
And user accepts terms of privacy policy
And user presses "Continue"
Then account is not created
And user is not logged in 

Scenario: user registration, wrong data
Given unregistered user
And a web browser is at the register page of opencart
When user does not fill all required registration fields
And user accepts terms of privacy policy
And user presses "Continue"
Then account is not created
And user is not logged in 

Scenario: user logging in
Given registered user
And a web browser is at the login page of opencart
When user fills all required login fields correctly
And user presses "Login"
Then user is logged in

Scenario: wrong user logging in, wrong credentials
Given a web browser is at the login page of opencart
When user fills all login fields with invalid credentials
And user presses "Login"
Then user is not logged in

Scenario: wrong user logging in, wrong password
Given a web browser is at the login page of opencart
When user fills correct username and incorrect password
And user presses "Login"
Then user is not logged in


Scenario: wrong user logging in, unfilled field
Given a web browser is at the login page of opencart
When user does not fill all login required fields
And user presses "Login"
Then user is not logged in