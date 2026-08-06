create table essasys (
    essay_id number generated always as identity primary key,
    title varchar2(200) not null,
    auther_name varchar2(200) not null,
    body clob not null default 'This is an essay',
    created_at date default sysdate not null,
    status varchar2(10) default 'DRAFT' not null,
    constraint chk_essay_status
        check (status in ('DRAFT', 'PUBLISHED'))
    
);