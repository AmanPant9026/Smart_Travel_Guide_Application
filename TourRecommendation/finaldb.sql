/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - tour_recommendation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`tour_recommendation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tour_recommendation`;

/*Table structure for table `hotel_db` */

DROP TABLE IF EXISTS `hotel_db`;

CREATE TABLE `hotel_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `name` varchar(255) default NULL,
  `rating` float default NULL,
  `mobile` varchar(255) default NULL,
  `type` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hotel_db` */

insert  into `hotel_db`(`id`,`img`,`name`,`rating`,`mobile`,`type`,`address`,`area`) values (1,'h1.jpg','Sujata hotel',4.8,'1234567895','5-star hotel','Chakrata','Chakrata'),(2,'h2.jpg','Radha krisna hotel',4.9,'4578956324','4-star hotel','Raipur','Raipur'),(3,'h3.jpg','Welcome hotel',4.6,'4785963258','2-star hotel','Dehradun','Dehradun'),(4,'h4.jpg','New welcome hotel',3.7,'1245789632','5-star hotel','Rajpur Road','Rajpur Road'),(5,'h5.jpg','Shrikant hotel',3.5,'2135478963','3-star hotel','Rishikesh','Rishikesh'),(6,'h6.jpg','Krisna hotel',3.1,'3625147896','4-star hotel','Mussoorie','Mussoorie'),(7,'h7.jpg','Krupa hotel',4.7,'3215478963','3-star hotel','Dharampur','Dharampur'),(8,'h8.jpg','New RK hotel',4.1,'2156463622','5-star hotel','Doiwala','Doiwala'),(9,'h9.jpg','Appitite hotel',3.2,'2154789632','4-star hotel','Vikasnagar','Vikasnagar'),(10,'h10.jpg','Shorma hotel',4.8,'2154796325','3-star hotel','Sahaspur','Sahaspur');

/*Table structure for table `place_db` */

DROP TABLE IF EXISTS `place_db`;

CREATE TABLE `place_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `rating` float default NULL,
  `type` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `place_db` */

insert  into `place_db`(`id`,`img`,`title`,`rating`,`type`,`time`,`phone`,`location`,`area`) values (1,'p1.jpg','Raipur national park',3.5,'National Park','6:30am - 6:30pm','1245879632','Raipur','Raipur'),(2,'p2.jpg','Raipur fort',4.7,'historic places','6:30am - 6:30pm','78964513257','Rajpur Road','Rajpur Road'),(3,'p3.jpg','Dharampur garde',4.4,'garden','6:30am - 6:30pm','7245189435','Dharampur','Dharampur'),(4,'p4.jpg','Mussoorie museum',3.8,'museum','6:30am - 6:30pm','124596325874','Mussoorie','Mussoorie'),(5,'p5.jpg','garden',3.1,'garden','6:30am - 6:30pm','2136547896','Doiwala','Doiwala'),(6,'p6.jpg','Sahaspur garden',4.6,'garden','6:30am - 6:30pm','2365847965','Sahaspur','Sahaspur'),(7,'p7.jpg','national park',4.8,'National Park','6:30am - 6:30pm','12124587965','Chakrata','Chakrata'),(8,'p8.jpg','Vikasnagar place',4.1,'historic places','6:30am - 6:30pm','1245789632','Vikasnagar','Vikasnagar'),(9,'p9.jpg','Rishikesh temple',3.5,'temple','6:30am - 6:30pm','2548796321','Rishikesh','Rishikesh'),(10,'p10.jpg','Dehradun park',3.9,'National Park','6:30am - 6:30pm','2547896562','Dehradun','Dehradun');

/*Table structure for table `recomm` */

DROP TABLE IF EXISTS `recomm`;

CREATE TABLE `recomm` (
  `user_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `rating` float NOT NULL,
  PRIMARY KEY  (`user_id`,`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomm` */

insert  into `recomm`(`user_id`,`item_id`,`rating`) values (1,1,2),(1,2,5),(1,3,1),(1,4,3),(1,5,4),(2,1,4),(2,2,4),(2,3,5),(2,4,3),(3,1,4),(3,2,4),(3,3,4),(3,4,4),(4,1,4),(4,4,4),(4,5,1),(5,1,4),(6,1,3),(7,1,3),(8,1,3),(9,1,3),(10,1,3);

/*Table structure for table `recreation_db` */

DROP TABLE IF EXISTS `recreation_db`;

CREATE TABLE `recreation_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `rating` float default NULL,
  `type` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `website` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recreation_db` */

insert  into `recreation_db`(`id`,`img`,`title`,`rating`,`type`,`phone`,`time`,`location`,`website`,`area`) values (1,'rc1.jpg','Olympic size swimming pool',4.4,'Swimming pool','9920090883','12:00pm - 11:00pm','Chakrata','https://www.jehannuma.com/','Chakrata'),(2,'rc2.jpg','Forbes advisor',3.6,'Swimming pool','9920090883','7:00am - 11:00pm','Rajpur Road','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Rajpur Road'),(3,'rc3.jpg','Gaming hub at red door',4.5,'Gaming hub','9920090883','12:00pm - 11:00pm','Dharampur','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Dharampur'),(4,'rc4.jpg','Olympic size swimming pool',3.8,'Play station','9920090883','12:00pm - 11:00pm','Mussoorie','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Mussoorie'),(5,'rc5.jpg','Gaming hub at red door',3.1,'Gaming hub','9920090883','12:00pm - 11:00pm','Sahaspur','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Sahaspur'),(6,'rc6.jpg','Olympic size swimming pool',3.9,'Play station','9920090883','12:00pm - 11:00pm','Doiwala','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Doiwala'),(7,'rc7.jpg','Forbes advisor',4.8,'Swimming pool','9920090883','12:00pm - 11:00pm','Rishikesh','https://www.jehannuma.com/','Rishikesh'),(8,'rc8.jpg','Gaming hub at red door',4.2,'Play station','9920090883','12:00pm - 11:00pm','Vikasnagar','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Vikasnagar'),(9,'rc9.jpg','Olympic size swimming pool',3.8,'Gaming hub','9920090883','12:00pm - 11:00pm','Raipur','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Raipur'),(10,'rc10.jpg','Forbes advisor',4.7,'Swimming pool','9920090883','12:00pm - 11:00pm','Dehradun','https://www.jehannuma.com/','Dehradun');

/*Table structure for table `restaurant_db` */

DROP TABLE IF EXISTS `restaurant_db`;

CREATE TABLE `restaurant_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `name` varchar(255) default NULL,
  `rating` float default NULL,
  `type` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `url` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `restaurant_db` */

insert  into `restaurant_db`(`id`,`img`,`name`,`rating`,`type`,`phone`,`time`,`address`,`url`,`area`) values (1,'rs1.jpg','La Kuchina',4.4,'Indian','1234567896','12:00pm - 11:00pm','La Kuchina','https://www.jehannuma.com/','Rajpur Road'),(2,'rs2.jpg','Momo Cafe',4.5,'Cafe','2587413698','6:30am - 11:30pm',' Maharana Pratap Nagar, Bhopal','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Rishikesh'),(3,'rs3.jpg','Under the Mango Tree',4.7,'Italian','2587469852','7:00am - 11:00pm','Bhopal, Madhya Pradesh 462013','https://www.jehannuma.com/','Doiwala'),(4,'rs4.jpg','Under the Mango Tree',4.1,'Cafe','2587469852','12:00pm - 11:00pm','Bhopal, Madhya Pradesh 462013','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Raipur'),(5,'rs5.jpg','La Kuchina',3.5,'Indian','2587469852','6:30am - 11:30pm',' Maharana Pratap Nagar, Bhopal','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Dehradun'),(6,'rs6.jpg','Momo Cafe',3.1,'Italian','2587469852','12:00pm - 11:00pm',' Maharana Pratap Nagar, Bhopal','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Dharampur'),(7,'rs7.jpg','La Kuchina',3.7,'Indian','2587469852','7:00am - 11:00pm','La Kuchina','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Mussoorie'),(8,'rs8.jpg','La Kuchina',3.8,'Indian','2587469852','6:30am - 11:30pm',' Maharana Pratap Nagar, Bhopal','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Vikasnagar'),(9,'rs9.jpg','Momo Cafe',3.2,'Cafe','2587469852','12:00pm - 11:00pm','Bhopal, Madhya Pradesh 462013','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Sahaspur'),(10,'rs10.jpg','Under the Mango Tree',4.5,'Italian','2587469852','7:00am - 11:00pm','La Kuchina','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','Chakrata');

/*Table structure for table `usertable` */

DROP TABLE IF EXISTS `usertable`;

CREATE TABLE `usertable` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `mobile` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `usertable` */

insert  into `usertable`(`id`,`username`,`email`,`mobile`,`password`) values (1,'a','yasj@gmail.com','8879343922','a'),(2,'b','yashsalvi1999@gmail.com','9930090883','hhshhs'),(3,'j','yashsalvi1999@gmail.com','1234567890','j'),(4,'k','yas@gmail.com','1234587649','k'),(5,'p','yashsalvi1999@gmail.com','1234567896','p'),(6,'z','yashsalvi1999@gmail.com','1234567890','z'),(7,'u','yashsalvi1999@gmail.com','1234567890','u'),(8,'c','yashsalvi1999@gmail.com','1234568907','c'),(9,'yo','yashsalvi1999@gmail.com','1234568890','yo'),(10,'roshan','yashsalvi1999@gmail.com','1234567890','roshan');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
