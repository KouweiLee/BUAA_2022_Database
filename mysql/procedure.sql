-- delimiter为定界符, 将$$作为块的结束
delimiter $$
drop procedure addcomment;
create procedure addcomment(in pTitle_id int, in pContent varchar(10000),
                            in pUsername varchar(100), in pTime datetime)
begin
    declare vComment_id int;
    -- 当发生错误时, error会被自动记为1
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    -- 开始事务, 保证要么全体成功, 要么全体失败
    start transaction ;
        insert into dc_comment(content, time, username) values (pContent, pTime, pUsername);
        set vComment_id = (select MAX(id) from dc_comment);
        insert into dc_com2title(title_id, comment_id) values (pTitle_id, vComment_id);
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
end$$

delimiter $$
drop procedure deletecomment;
create procedure deletecomment(in pComment_id int)
begin
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    start transaction ;
        delete from dc_com2title where comment_id = pComment_id;
        delete from dc_comment where id = pComment_id;
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
    select error, pComment_id;
end $$
delimiter ;


delimiter $$
drop procedure deletetitle;
create procedure deletetitle(in pTitle_id int)
begin
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    start transaction ;
        delete from dc_com2title where title_id = pTitle_id;
        delete from dc_title where id = pTitle_id;
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
    select error, pTitle_id;
end $$
delimiter ;