create table formations(
    id_formation smallint auto_increment primary key,
    noms varchar(50),
    postnoms varchar(50),
    prenoms varchar(50),
    sexes varchar(10),
    adresses  varchar(100),
    communes varchar(15),
    telephones varchar(15),
    typeFormation varchar(20),
    dateEnregistrement date default currant_date()


);


create table login_simple(
    id_login tinyint auto_increment primary key,
    user_login varchar(50),
    pwd_login varchar(255)
);