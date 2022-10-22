# 创建数据库和表
create database if not exists databasehw;

drop table tb_user;
# 创建用户表
create table if not exists tb_user(
    username varchar(100) primary key ,
    password varchar(100) not null,
    user_type INT default 0,
    name varchar(50) default '佚名' not null
);

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
    foreign key(username) references tb_user(username)
);

create table dc_comment(
    id int primary key auto_increment,
    content varchar(10000),
    time datetime,
    username varchar(100),
    foreign key (username) references tb_user(username)
);

create table dc_com2title(
    title_id int not null ,
    comment_id int not null ,
    primary key (title_id, comment_id),
    foreign key (title_id) references dc_title(id),
    foreign key (comment_id) references dc_comment(id)
);