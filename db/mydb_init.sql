SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`accounts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`accounts` (
  `account_id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`account_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`admins` (
  `account_id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `birth_date` DATE NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `salary` DECIMAL(9,2) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(120) NOT NULL,
  PRIMARY KEY (`account_id`),
  CONSTRAINT `fk_admins_accounts`
    FOREIGN KEY (`account_id`)
    REFERENCES `mydb`.`accounts` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`categories` (
  `category_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`expenses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`expenses` (
  `expense_id` INT(11) NOT NULL AUTO_INCREMENT,
  `admin_id` INT(11) NOT NULL,
  `ammount` DECIMAL(9,2) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`expense_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`products` (
  `product_id` INT(11) NOT NULL AUTO_INCREMENT,
  `category_id` INT(11) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `unit_price` DECIMAL(9,2) NOT NULL,
  `quantity` INT(11) NOT NULL,
  PRIMARY KEY (`product_id`),
  INDEX `fk_products_categories1_idx` (`category_id` ASC) ,
  CONSTRAINT `fk_products_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `mydb`.`categories` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`sellers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sellers` (
  `account_id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `birth_date` DATE NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `salary` DECIMAL(9,2) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(120) NOT NULL,
  PRIMARY KEY (`account_id`),
  CONSTRAINT `fk_admins_accounts0`
    FOREIGN KEY (`account_id`)
    REFERENCES `mydb`.`accounts` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`sells`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sells` (
  `sell_id` INT(11) NOT NULL,
  `account_id` INT(11) NOT NULL,
  `product_id` INT(11) NOT NULL,
  `unit_price` DECIMAL(9,2) NOT NULL,
  `quantity` INT(11) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`sell_id`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- ---------------------------------------------------------
-- Creating an admin account
-- ---------------------------------------------------------
INSERT INTO mydb.accounts VALUES (1, 'admin', 'admin', 'admin');
INSERT INTO mydb.admins VALUES (1, 'admin', 'admin', '2000-01-01', 1111, 1111.11, 'male', 'XXX');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
