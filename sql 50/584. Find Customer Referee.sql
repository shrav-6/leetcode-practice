# use of COALESCE, IFNOT, OR, !=, <>

# solution 1: not equal to: <> or !=
select name from Customer where referee_id IS NULL or referee_id != 2;

# solution 2 - coalesce returns the first non null element: https://www.w3schools.com/sql/func_sqlserver_coalesce.asp
# but here if the referee_id should not be 2 and 0 then can't use 0 in coalesce can use: coalesce(referee_id, -1)
# can also use IFNULL(referee_id, -1): https://www.w3schools.com/mysql/func_mysql_ifnull.asp
SELECT name FROM Customer WHERE IFNULL(referee_id,-1) <> 2;