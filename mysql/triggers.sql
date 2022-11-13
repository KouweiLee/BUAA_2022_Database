-- 增加评论时, 主题帖评论数+1
delimiter $$
create trigger NumOfComments_update
    after insert
    on dc_com2title
    for each row
begin
    update dc_title set numofcoms = numofcoms + 1 where id = NEW.title_id;
end$$
delimiter ;

-- 当删除评论时, 当前主题帖的评论数-1
# drop trigger NumOfComments_delete;
delimiter $$
create trigger NumOfComments_delete
    before delete
    on dc_comment
    for each row
begin
    update dc_title
    set numofcoms = numofcoms - 1
    where id =
          (select title_id from dc_com2title where comment_id = OLD.id);
end$$
delimiter ;

-- 用户增加帖子时, 用户发帖数加1
delimiter $$
create trigger user_titles_add
    after insert
    on dc_title
    for each row
begin
    update tb_user set numOfTitles = tb_user.numOfTitles + 1 where username = NEW.username;
end$$
delimiter ;

-- 用户删除帖子时, 用户发帖数-1; 同时, 贴内所有评论删除
delimiter $$
# drop trigger user_titles_delete;
create trigger user_titles_delete
    before delete
    on dc_title
    for each row
begin
    update tb_user set numOfTitles = tb_user.numOfTitles - 1 where username = OLD.username;
    delete from dc_comment where id in
         (select comment_id from dc_com2title where title_id = OLD.id);
end$$
delimiter ;

-- 增加作业时, 作业平均分更新
drop trigger homework_ave_update;
delimiter $$
create trigger homework_ave_update
    after update
    on cl_homework_user
    for each row
begin
    update cl_homework
    set averageScore =
            (select avg(score)
             from cl_homework_user
             where homework_id = NEW.homework_id
               and score is not null
             group by homework_id)
    where id = NEW.homework_id;
end$$
delimiter ;

-- 删除作业时, 作业平均分更新
delimiter $$
# drop trigger homework_ave_delete;
create trigger homework_ave_delete
    after delete
    on cl_homework_user
    for each row
begin
    declare ave int;
    -- 只有作业已经被给分后才更新, 否则没必要更新
    if OLD.score is not null then
        set ave = (select avg(score)
                   from cl_homework_user
                   where homework_id = OLD.homework_id
                     and score is not null
                   group by homework_id);
        if ave is null then
            set ave = 0;
        end if;
        update cl_homework
        set averageScore = ave
        where id = OLD.homework_id;
    end if;
end$$
delimiter ;

-- 删除课程时, 所有作业和附件全部删除
delimiter $$
create trigger course_delete
    before delete
    on cl_class
    for each row
begin
    delete from cl_material where cl_material.id in
        (select material_id from cl_class_material where class_id = OLD.id);
    delete from cl_homework where cl_homework.id in
        (select homework_id from cl_class_homework where class_id = OLD.id);
end$$
delimiter ;

-- 删除作业时, 所有当前作业下的附件都要删除
delimiter $$
create trigger homework_delete
    before delete
    on cl_homework
    for each row
begin
    delete from cl_homework_user where homework_id = OLD.id;
end$$
delimiter ;

show triggers ;