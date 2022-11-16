-- 社团发展历史信息表
drop table an_develops;
create table if not exists an_develops
(
    id int primary key auto_increment,
    time varchar(100), -- 年份
    overview varchar(10000)
);

-- 社团照片表
drop table an_pics;
create table if not exists an_pics
(
    pic_id int,
    develop_id int,
    foreign key (pic_id) references tb_pics(id),
    foreign key (develop_id) references an_develops(id)
);

insert into an_develops (time, overview)
values ('2008年', '哈哈哈哈');

insert into an_develops (time, overview)
values ('2009年', '哈哈哈');

insert into an_develops (time, overview)
values ('2009年', '哈哈哈');

insert into tb_pics (position, username)
values ('无', '123');

insert into an_pics (pic_id, develop_id)
VALUES (1,1);
