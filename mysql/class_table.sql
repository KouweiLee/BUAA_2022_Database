#创建课程表
create table if not exists cl_class
(
    id          int primary key auto_increment,
    name        varchar(100) not null,
    description varchar(10000),
    pingshi     int,
    exam        int,
    time        varchar(100),
    position    varchar(100)
);

#创建材料附件表
create table if not exists cl_material
(
    id   int primary key auto_increment,
    name varchar(100) not null,
    path varchar(500),
    time datetime
);

#创建作业表
create table if not exists cl_homework
(
    id         int primary key auto_increment,
    name       varchar(100) not null,
    content    varchar(10000),
    begin_time datetime,
    end_time   datetime
);

#选课表
create table if not exists cl_class_user
(
    username varchar(100),
    class_id int,
    primary key (username, class_id),
    foreign key (username) references tb_user (username) on delete cascade,
    foreign key (class_id) references cl_class (id) on delete cascade
);

#课程-作业表
create table if not exists cl_class_homework
(
    class_id    int,
    homework_id int,
    primary key (homework_id),
    foreign key (class_id) references cl_class (id) on delete cascade,
    foreign key (homework_id) references cl_homework (id) on delete cascade
);

#用户交作业表
drop table cl_homework_user;
create table if not exists cl_homework_user
(
    id            int primary key auto_increment,
    username      varchar(100),
    homework_id   int,
    score         int,
    last_time     datetime,
    homework_path varchar(500),
    foreign key (username) references tb_user (username) on delete cascade,
    foreign key (homework_id) references cl_homework (id) on delete cascade
);
-- 增加唯一约束, 使得username和homework_id只能在表中出现一次
alter table cl_homework_user add constraint onlyone unique (username, homework_id);
#课程-附件表
create table if not exists cl_class_material
(
    class_id    int,
    material_id int,
    primary key (material_id),
    foreign key (class_id) references cl_class (id) on delete cascade,
    foreign key (material_id) references cl_material (id) on delete cascade
);

create view view_homework_user (attachment_id, homework_id, username, name, time, score)as
    (select id, homework_id, work.username, name, last_time, score from cl_homework_user as work, tb_user as user
     where work.username = user.username);

create view view_material_class (attachment_id, name, time, class_id)
    as (select m.id, m.name, m.time, r.class_id
        from cl_material as m, cl_class_material as r
        where m.id = r.material_id);