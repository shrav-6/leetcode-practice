# use of distinct and order by
select distinct(author_id) as id from Views where author_id = viewer_id order by id ASC;