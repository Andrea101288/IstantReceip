# DATABASE CREATION

CREATE DATABASE IF NOT EXISTS istantReceip;
USE istantReceip;

CREATE TABLE IF NOT EXISTS receipt(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(128) NOT NULL,
    description varchar(10000) NOT NULL    
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredient(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(128) NOT NULL,
    calories bigint NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS receiptIngredients(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    idIngredient bigint NOT NULL,
    idReceipt bigint NOT NULL,
    foreign key (idIngredient) references ingredient(id),
    foreign key (idReceipt) references receipt(id),
    amount varchar(256) NOT NULL,
    mainIng boolean NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredientApp(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(256) NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredientAppRel(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    idIngredient bigint NOT NULL,
    idIngredientApp bigint NOT NULL,
    foreign key (idIngredient) references ingredient(id),
    foreign key (idIngredientApp) references ingredientApp(id)
)Engine = InnoDB;




