# 创建数据库和表
create database if not exists databasehw;

drop table tb_user;
# 创建用户表
create table if not exists tb_user(
    username varchar(100) primary key ,
    password varchar(100) not null,
    user_type varchar(10) default 'stu',
    name varchar(50) default '佚名' not null
);
alter table tb_user add column numOfTitles int default 0;
alter table tb_user add column numOfComs int default 0;
alter table tb_user add column photo varchar(100);
# alter table tb_user add column header varchar(100);

drop table dc_title;
drop table dc_comment;
drop table dc_com2title;
# 创建讨论区表
create table if not exists dc_title(
    id int primary key auto_increment,
    title varchar(100) not null ,
    content varchar(10000),
    time datetime,
    username varchar(100),
    foreign key(username) references tb_user(username) on delete cascade
);

-- 创建对title的索引, 便于查询
create index ti on dc_title(title);
alter table dc_title add column numofcoms int default 0;

create table dc_comment(
    id int primary key auto_increment,
    content varchar(10000),
    time datetime,
    username varchar(100),#评论人
    commentatee_name varchar(50),#被评论人姓名
    foreign key (username) references tb_user(username) on delete cascade
);

create table dc_com2title(
    title_id int not null ,
    comment_id int not null ,
    primary key (comment_id),
    foreign key (title_id) references dc_title(id) on delete cascade ,
    foreign key (comment_id) references dc_comment(id) on delete cascade
);

drop table tb_pics;
-- 图床表
create table tb_pics(
    id int primary key auto_increment,
    position varchar(100), -- position就是url
    username varchar(100),
    foreign key (username) references tb_user(username)
);
# drop view view_pics;
create view view_pics(pic_id, develop_id, position) as
    (select pic_id, develop_id, position from tb_pics , an_pics
    where pic_id = tb_pics.id);
show index from tb_user;
show index from dc_comment;
show index from dc_com2title;