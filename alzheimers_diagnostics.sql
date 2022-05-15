/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.34-MariaDB : Database - alzheimers_diagnostics
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`alzheimers_diagnostics` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `alzheimers_diagnostics`;

/*Table structure for table `tbl_doctor` */

DROP TABLE IF EXISTS `tbl_doctor`;

CREATE TABLE `tbl_doctor` (
  `doc_id` varchar(10) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `reg_no` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `specialization` varchar(30) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `experience` varchar(10) NOT NULL,
  `house` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` int(6) NOT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbl_doctor` */

insert  into `tbl_doctor`(`doc_id`,`login_id`,`fname`,`lname`,`reg_no`,`email`,`phone_no`,`gender`,`specialization`,`qualification`,`experience`,`house`,`city`,`state`,`pin`) values ('DOC-100',2,'Pooja','Selby','IND-001','poojaselby18@gmail.com','9744663371','Female','Physician','MBBS,MD','5 years','Valayil House','Silvasa','Gujarat',763249),('DOC-101',3,'Ann','Sabu','IND-002','annusabu238@gmail.com','9995566191','Female','Cardiology','MBBS','3 years','Puthenpurakal House','Kumily','Kerala',854697),('DOC-102',4,'Deepthy','Lukose','IND-003','deepthylukose123@gmail.com','8281756948','Female','Neurology','MBBS,MD','8 years','Chamakalayil House','Kottayam','Kerala',796542),('DOC-103',5,'Kevin','Aional','IND-004','kevinaional@gmail.com','9567321445','Male','Dermatology','MBBS,MD','6 years','Kevin Dale','Kollam','Kerala',721685);

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `login_type` varchar(10) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`login_id`,`username`,`password`,`login_type`) values (1,'admin','admin123','admin'),(2,'pooja.selby','pooja@123','doctor'),(3,'annu.sabu','annu@123','doctor'),(4,'deepthy.lukose','deepthy@123','doctor'),(5,'kevin.aional','kevin@123','doctor'),(6,'roshan.francis','roshan@123','doctor');

/*Table structure for table `tbl_patient` */

DROP TABLE IF EXISTS `tbl_patient`;

CREATE TABLE `tbl_patient` (
  `patient_id` varchar(10) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int(3) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `house` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` int(6) NOT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbl_patient` */

insert  into `tbl_patient`(`patient_id`,`fname`,`lname`,`gender`,`age`,`phone_no`,`house`,`city`,`state`,`pin`) values ('P-100','Merin','Jacob','Female',24,'9446732153','Eacheramannil House','Ranni','Kerala',863247),('P-101','Bipina','Kuriakose','Female',27,'9463785216','Ponnattil House','Ettumanoor','Kerala',685321),('P-102','Nafla','Majeed','Female',26,'8281248157','Kottapurath House','Karunagapally','Kerala',668538),('P-103','Sinu','Lukose','Female',26,'8129996819','Sinu Dale','Oyoor','Kerala',658345);

/*Table structure for table `tbl_patient_rec` */

DROP TABLE IF EXISTS `tbl_patient_rec`;

CREATE TABLE `tbl_patient_rec` (
  `rec_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` varchar(10) NOT NULL,
  `doc_id` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `description` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_patient_rec` */

insert  into `tbl_patient_rec`(`rec_id`,`patient_id`,`doc_id`,`date`,`description`,`image`) values (1,'P-100','DOC-101','2018-10-26','','static/uploads/fc1b1ed3-a60f-43a3-bbd0-8af22caaff56.tif'),(2,'P-100','DOC-101','2018-10-26','','static/uploads/561c9779-0d75-42f7-9f66-4af291a69819.tif');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
