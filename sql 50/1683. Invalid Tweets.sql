# use of LENGTH() -> to count the number of characters in a string can work for this too LENGTH(1234) but should be only numbers
select tweet_id from Tweets where LENGTH(content)>15;