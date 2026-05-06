# Hospital Management Software


## Project Goal
- Stores hospital data
- Accepts CLI Inputs
- Will run advanced SQL analytics
- Dashboard insights

## Functional Requrirments:
- patients
- doctors
- Appointments
- Treatments
- Departments
- Billing

## Step by Step by Module Implementation
- Database designs
- Module wise implementation
    - Connecting to Database
    - Patient Module
    - Doctor Module
    - Appointment Module
    - Treatment Module
    - Department Module
    - Billing Module
    - Dashboard


## Database Design 
### Patient Module
- Table Name is patients
    - patient id
    - patient name
    - address
    - phone number
    - age
    - gender
    - date created
    - date updated
- Table Name is patients_emr (electronic medical records)
    - emr_id
    - patient id
    - weight
    - height
    - bloodpressure
    - pulse
    - any allergies
    - any previous medication
    - any other health issues (thyroid, diabets)

## Department module
- Table name departments
    - department id
    - department name
    - department code

## Doctors Modules
- Table name doctors
    - doctor id
    - doctor name 
    - department id
    - specialist
    - experience
- Table Name doctors availability
    - available id
    - doctor id
    - status


## Appointments Modules
- Table name appointments
    - appointment id
    - patient id
    - dotor id
    - appointment date
    - status

## Treatment Module
- Table name treatment
    - treatment id
    - appointment id
    - treatment type
    - cost

## Billing Module
- Table name 
    - billing id
    - appointment id
    - total amount 
    - payment status
    - payment type




CREATE DATABASE hms;
USE hms;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    phone_number VARCHAR(30),
    address TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    date_updated TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
)

CREATE TABLE `hms`.`patients_emr` (
  `emr_id` INT NOT NULL AUTO_INCREMENT,
  `patient_id` INT NULL,
  `weight` DOUBLE NULL,
  `height` DOUBLE NULL,
  `bloodpressure` VARCHAR(45) NULL,
  `pulse` VARCHAR(45) NULL,
  `allergies` TEXT NULL,
  `previous_medication` TEXT NULL,
  `other_health_isses` TEXT NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`emr_id`),
  INDEX `patientid_fk_idx` (`patient_id` ASC) VISIBLE,
  CONSTRAINT `patientid_fk`
    FOREIGN KEY (`patient_id`)
    REFERENCES `hms`.`patients` (`patient_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

c
CREATE TABLE `hms`.`departments` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `department_name` VARCHAR(200) NULL,
  `department_code` VARCHAR(100) NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`department_id`));


CREATE TABLE `hms`.`doctors` (
  `doctor_id` INT NOT NULL AUTO_INCREMENT,
  `doctor_name` VARCHAR(200) NULL,
  `department_id` INT NULL,
  `specialist` VARCHAR(100) NULL,
  `experience` FLOAT NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`doctor_id`),
  INDEX `deptId_fk_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `deptId_fk`
    FOREIGN KEY (`department_id`)
    REFERENCES `hms`.`departments` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `hms`.`doctor_availability` (
  `available_id` INT NOT NULL AUTO_INCREMENT,
  `doctor_id` INT NULL,
  `status` VARCHAR(45) NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`available_id`));

CREATE TABLE `hms`.`appointments` (
  `appointment_id` INT NOT NULL AUTO_INCREMENT,
  `patient_id` INT NULL,
  `doctor_id` INT NULL,
  `appointment_time` DATETIME NULL,
  `appointment_status` VARCHAR(45) NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`appointment_id`));


CREATE TABLE `hms`.`treatment` (
  `treatment_id` INT NOT NULL AUTO_INCREMENT,
  `treatment_type` TEXT NULL,
  `appointment_id` INT NULL,
  `cost` DOUBLE NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`treatment_id`),
  INDEX `appointmentId_fk_idx` (`appointment_id` ASC) VISIBLE,
  CONSTRAINT `appointmentId_fk`
    FOREIGN KEY (`appointment_id`)
    REFERENCES `hms`.`appointments` (`appointment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);



CREATE TABLE `hms`.`billing` (
  `billing_id` INT NOT NULL AUTO_INCREMENT,
  `appointment_id` INT NULL,
  `total_amount` DECIMAL(10,2) NULL,
  `payment_status` VARCHAR(45) NULL,
  `payment_type` VARCHAR(45) NULL,
  `date_created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`billing_id`),
  INDEX `appointmentId_fk_idx` (`appointment_id` ASC) VISIBLE,
  CONSTRAINT `appointmentId_billing_fk`
    FOREIGN KEY (`appointment_id`)
    REFERENCES `hms`.`appointments` (`appointment_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

