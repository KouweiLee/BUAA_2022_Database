CREATE TABLE Student
(
    Sid     int PRIMARY KEY,
    Sname   VARCHAR(20) NOT NULL,
    Sgender VARCHAR(2)  not null,
    Sage    INT         not null
);

alter table Student
    add constraint ck_age check ( Sage <= 200 );

CREATE TABLE teacher
(
    Tid     int         NOT NULL,
    Tname   varchar(20) NOT NULL,
    Tgender varchar(2)  NOT NULL,
    Tage    int         NOT NULL,
    Temail  varchar(127) DEFAULT NULL,
    Tphone  varchar(30)  DEFAULT NULL,
    PRIMARY KEY (Tid),
    UNIQUE KEY uni_phone (Tphone)
);

create table Course
(
    Cid     int primary key,
    Cname   varchar(30) not null,
    Ctype   varchar(10) not null,
    Ccredit int         not null,
    Tid     int,
    foreign key (Tid) references Teacher (Tid)
);

create table SC
(
    Sid   int,
    Cid   int,
    Score int,
    foreign key (Sid) references Student (Sid),
    foreign key (Cid) references Course (Cid),
    constraint ck_score check ( Score <= 100 )
);

insert into Student (Sid, Sname, Sgender, Sage)
values (20373159, '李国玮', 'M', 20);
insert into Student (Sid, Sname, Sgender, Sage)
values (20373111, '陈金', 'M', 22);
insert into Student (Sid, Sname, Sgender, Sage)
values (19373111, '陈开摆', 'F', 19);

insert into teacher (Tid, Tname, Tgender, Tage, Temail, Tphone)
values (123456789, '张老师', 'M', 40, '123456@123.com', '15924532999');
insert into teacher (Tid, Tname, Tgender, Tage, Temail, Tphone)
values (123456700, '雷俊', 'F', 45, '123000@123.com', '15912331233');

insert into Course (Cid, Cname, Ctype, Ccredit, Tid)
values (11112222, '数据库', 'CS', 4, 123456789);
insert into Course (Cid, Cname, Ctype, Ccredit, Tid)
values (11113333, '英语', 'En', 2, 123456700);

insert into SC (Sid, Cid, Score)
values (20373159, 11112222, 100);
insert into SC (Sid, Cid, Score)
values (20373159, 11113333, 100);

insert into SC (Sid, Cid, Score)
values (20373111, 11112222, 99);
insert into SC (Sid, Cid, Score)
values (20373111, 11113333, 59);

insert into SC (Sid, Cid, Score)
values (19373111, 11112222, 90);
insert into SC (Sid, Cid, Score)
values (19373111, 11113333, 79);
select Tid
from teacher
where Tgender = 'M';
select Cid
from Course
where Tid in (select Tid from teacher where Tgender = 'M')
  and Ccredit >= 2;
select Sid
from SC
where Cid in (select Cid
              from Course
              where Tid in (select Tid from teacher where Tgender = 'M')
                and Ccredit >= 2)
  and Score >= 80;
select Sname, Cname, Score, Tname
from Student,
     Course,
     SC,
     teacher
where teacher.Tid in (select Tid from teacher where Tgender = 'M')
  and Course.Ccredit >= 2
  and SC.Score >= 80
  and Student.Sid = SC.Sid
  and SC.Cid = Course.Cid
  and Course.Tid = teacher.Tid;

create view SC_20 as
(
select Sid, Score
from SC
where left(Sid, 2) = 20);

update Course
set Ctype = '必修'
where Cid in (select Cid
              from (select Cid from Course order by Cid desc) as a);

update SC
set SCore = 65
where Cid in (select Cid
              from Course
              where Tid in
                    (select Tid from teacher where Tname = '雷俊'));

delete from SC where Score >= 90;

create trigger Tage_tri before insert on teacher
    for each row
    begin
        if NEW.Tage <= 18 then
            signal sqlstate '45000' set message_text  = 'cannot insert, age error!';
        end if;
    end;

insert into Student (Sid, Sname, Sgender, Sage)
values (20372229, '华莱', 'M', 9);
insert into teacher (Tid, Tname, Tgender, Tage, Temail, Tphone)
values (123456987, '哈哈哈', 'M', 17, '122223@123.com', '15035660024');
create index '20373159' on teacher(Tid, Tname, Tage);