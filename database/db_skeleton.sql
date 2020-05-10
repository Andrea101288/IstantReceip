# DATABASE CREATION

CREATE DATABASE IF NOT EXISTS istantRecipe;
USE istantRecipe;

CREATE TABLE IF NOT EXISTS recipe(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(128) NOT NULL,
    description varchar(10000) NOT NULL    
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredient(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(128) NOT NULL,
    en_name varchar(128) NOT NULL,
    calories bigint NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS recipeIngredients(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    id_ingredient bigint NOT NULL,
    id_recipe bigint NOT NULL,
    foreign key (id_ingredient) references ingredient(id),
    foreign key (id_recipe) references receipt(id),
    amount varchar(256) NOT NULL,
    main_ingredient boolean NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredient_app(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    name varchar(256) NOT NULL
)Engine = InnoDB;

CREATE TABLE IF NOT EXISTS ingredient_appRel(
    id bigint PRIMARY KEY AUTO_INCREMENT,
    id_ingredient bigint NOT NULL,
    id_ingredient_app bigint NOT NULL,
    foreign key (id_ingredient) references ingredient(id),
    foreign key (id_ingredient_app) references ingredient_app(id)
)Engine = InnoDB;




