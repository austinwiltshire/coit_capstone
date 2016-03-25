We have data like the following, I want to be able to search the data by a user to get the list of cars they've bought, as well as search by a car name and get a list of users that have bought that car.

* Come up with a user id scheme that can be used, and write a script that will turn the first name and last name into a user id.
* Parse and store the data into a SQLite database, including new user ids.
* Create a script that will search the database by user id and return the cars for that user. Will get the user id via command line arg.
* Create a script that will search the database by car and return all the users that have that car. Will get car via command line arg.

Good code structuring, reuse and other things between the three scripts is important.

Try and get as much done in the first 8 hours as possible. Don't be afraid to ask questions. We'll have a check in at 8 hours, and then another at 3 days. Then we'll finish whatevers left including responding to code
review. Data is formatted in 'cars.txt' below.

```
f: Buyer's first name
l: Buyer's last name
c: comma seperated list of cars
o: Buyer's favorite color (based on car buying preferences)
```
Note: Not all of the data will be there, in fact, any of the fields can be empty.
