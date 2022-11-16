-- delimiter为定界符, 将$$作为块的结束
-- 增加评论
delimiter $$
# drop procedure addcomment;
create procedure addcomment(in pTitle_id int, in pContent varchar(10000),
                            in pUsername varchar(100), in pTime datetime, in pCommentatee_name varchar(50))
begin
    declare vComment_id int;
    -- 当发生错误时, error会被自动记为1
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    -- 开始事务, 保证要么全体成功, 要么全体失败
    start transaction ;
        insert into dc_comment(content, time, username, commentatee_name) values (pContent, pTime, pUsername, pCommentatee_name);
        set vComment_id = (select MAX(id) from dc_comment);
        insert into dc_com2title(title_id, comment_id) values (pTitle_id, vComment_id);
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
end$$

-- 增加作业
delimiter $$
# drop procedure addwork;
create procedure addwork(in pClass_id int, in pHomeworkName varchar(100))
begin
    declare vhomeworkId int;
    -- 当发生错误时, error会被自动记为1
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    -- 开始事务, 保证要么全体成功, 要么全体失败
    start transaction ;
        insert into cl_homework (name) values (pHomeworkName);
        set vhomeworkId = (select MAX(id) from cl_homework);
        insert into cl_class_homework(class_id, homework_id) values (pClass_id, vhomeworkId);
    if error = 1 then
        select error;
        rollback ;
    else
        commit ;
    end if ;
end$$
DELIMITER ;

delimiter $$
drop procedure selectAllClasses;
-- pusername为用户账号, pisChoose表示查询该用户选的课还是没有选的课, true为是, false为不是
create procedure selectAllClasses(in pusername varchar(100), in pisChoose bool)
begin
    declare error int default 0;
    declare continue handler for sqlexception set error=1;

    start transaction ;
    if pisChoose = true then
        select id, name from cl_class where id in
                                        (select class_id from cl_class_user where username = pusername);
    else
        select id, name from cl_class where id not in
                                        (select class_id from cl_class_user where username = pusername);
    end if;

    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
end$$
delimiter ;

delimiter $$
create procedure selectAllWorks(in pClassId int)
begin
    declare error int default 0;
    declare continue handler for sqlexception set error=1;

    start transaction ;
    select id, name from cl_homework where id in
                                           (select homework_id from cl_class_homework where class_id = pClassId);
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
end$$
delimiter ;

delimiter $$
# drop procedure addHomeWorkRecord;
-- on duplicate key实现: 若当前表已经存在username和homework_id对应的记录, 则更新; 否则, 则插入
create procedure addHomeWorkRecord(in pusername varchar(100), in phomework_id int, in ptime datetime, in pname varchar(500))
begin
    declare error int default 0;
    declare continue handler for sqlexception set error=1;

    start transaction ;
    insert into cl_homework_user(username, homework_id, last_time, filename) values (pusername, phomework_id, ptime, ptime)
    on duplicate key update last_time = ptime, filename = pname;
    if error = 1 then
        rollback ;
    else
        commit ;
    end if ;
end$$
delimiter ;

-- 增加课程附件
delimiter $$
# drop procedure addwork;
create procedure addMaterial(in pClass_id int, in pname varchar(100), in ptime datetime)
begin
    declare vMaterial_id int;
    -- 当发生错误时, error会被自动记为1
    declare error int default 0;
    declare continue handler for sqlexception set error=1;
    -- 开始事务, 保证要么全体成功, 要么全体失败
    start transaction ;
        insert into cl_material (name, time) values (pname, ptime);
        set vMaterial_id = @@identity; -- 获得上一步插入的id
        insert into cl_class_material(class_id, material_id) values (pClass_id, vMaterial_id);
    if error = 1 then
        select error;
        rollback ;
    else
        commit ;
    end if ;
end$$
DELIMITER ;

# -- 获取社团发展历史信息
# delimiter $$
# # drop procedure addwork;
# create procedure getAllDevelops()
# begin
#     -- 当发生错误时, error会被自动记为1
#     declare error int default 0;
#     declare continue handler for sqlexception set error=1;
#     -- 开始事务, 保证要么全体成功, 要么全体失败
#     start transaction ;
#         select id, time, overview
#     if error = 1 then
#         select error;
#         rollback ;
#     else
#         commit ;
#     end if ;
# end$$
# DELIMITER ;
call selectAllClasses('123', false);
call selectAllWorks(3);
call addHomeWorkRecord('123', 5, '2022-11-05 20:32:36');
call addMaterial(5, '测试点', '2022-11-05 20:32:00');
# delimiter $$
# drop procedure deletecomment;
# create procedure deletecomment(in pComment_id int)
# begin
#     declare error int default 0;
#     declare continue handler for sqlexception set error=1;
#     start transaction ;
#         delete from dc_com2title where comment_id = pComment_id;
#         delete from dc_comment where id = pComment_id;
#     if error = 1 then
#         rollback ;
#     else
#         commit ;
#     end if ;
#     select error, pComment_id;
# end $$
# delimiter ;


# delimiter $$
# drop procedure deletetitle;
# create procedure deletetitle(in pTitle_id int)
# begin
#     declare error int default 0;
#     declare continue handler for sqlexception set error=1;
#     start transaction ;
#         delete from dc_com2title where title_id = pTitle_id;
#         delete from dc_title where id = pTitle_id;
#     if error = 1 then
#         rollback ;
#     else
#         commit ;
#     end if ;
#     select error, pTitle_id;
# end $$
# delimiter ;