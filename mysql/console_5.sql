# delimiter $$
# create trigger Tri_addComment
#     after insert on dc_comment
#     for each row
# begin
#     insert into dc_com2title (title_id, comment_id) values ()
#
# end $$