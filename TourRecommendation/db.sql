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
  `rating` varchar(255) default NULL,
  `mobile` varchar(255) default NULL,
  `type` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hotel_db` */

insert  into `hotel_db`(`id`,`img`,`name`,`rating`,`mobile`,`type`,`address`,`area`) values (1,'jehan_numa.png','Jehan Numa Palace Hotel','4.5','1234567895','5-star hotel','157, Shyamla Hills Rd, Shymala Hills, Bhopal, Madhya Pradesh','ghansoli'),(2,'marriott.png','Courtyard by Marriot','4.0','4578956324','4-star hotel','Courtyard by Marriott, DB City, Arera Hills, Bhopal, Madhya Pradesh','nerul'),(3,'sayaji.png','Sayaji Hotel','4.2','4785963258','3-star hotel','Sayaji Hotel, Van Vihar Rd, Near Sair Sapata, Prempura, Bhopal, Madhya Pradesh','thane'),(4,'jehan_numa.png','Courtyard by Marriot','4.8','4789562514','4-star hotel','Sayaji Hotel, Van Vihar Rd, Near Sair Sapata, Prempura, Bhopal, Madhya Pradesh','juinagar');

/*Table structure for table `place_db` */

DROP TABLE IF EXISTS `place_db`;

CREATE TABLE `place_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `rating` varchar(255) default NULL,
  `type` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `place_db` */

insert  into `place_db`(`id`,`img`,`title`,`rating`,`type`,`time`,`phone`,`location`,`area`) values (1,'van_vihar.png','Van Vihar National Park','3.4','Sizable Parkland with wild animals','6:30am - 6:30pm','1245879632','Van Vihar National Park, Shymala Hills, Bhopal, Madhya Pradesh','Airoli'),(2,'bhojtal.png','Bhojtal','3.5','Upper Lake','6:30am - 6:30pm','78964513257','Bhojtal, Madhya Pradesh','ghansoli'),(3,'taj_mahal.png','Taj Mahal Palace','3.6','Architecture, history, and palace','6:30am - 6:30pm','7245189435','Taj Mahal Palace, Kohefiza, Bhopal, Madhya Pradesh 462001','rabale'),(4,'bhojtal.png','Bhojtal','3.7','Upper Lake','6:30am - 6:30pm','12457849568','Bhojtal, Madhya Pradesh','juinagar'),(5,'van_vihar.png','Bhojtal','3.8','Architecture, history, and palace','6:30am - 6:30pm','124578965','Van Vihar National Park, Shymala Hills, Bhopal, Madhya Pradesh','turbhe'),(6,'taj_mahal.png','Taj Mahal Palace','3.9','Upper Lake','6:30am - 6:30pm','1245785926','Taj Mahal Palace, Kohefiza, Bhopal, Madhya Pradesh 462001','koparkhairane'),(7,'bhojtal.png','Bhojtal','4','Architecture, history, and palace','6:30am - 6:30pm','346158956','Bhojtal, Madhya Pradesh','thane'),(8,'taj_mahal.png','Taj Mahal Palace','4.2','Architecture, history, and palace','6:30am - 6:30pm','4315784956','Taj Mahal Palace, Kohefiza, Bhopal, Madhya Pradesh 462001','nerul');

/*Table structure for table `recomm` */

DROP TABLE IF EXISTS `recomm`;

CREATE TABLE `recomm` (
  `user_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `rating` float NOT NULL,
  PRIMARY KEY  (`user_id`,`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomm` */

insert  into `recomm`(`user_id`,`item_id`,`rating`) values (1,1,2),(1,2,5),(1,3,1),(1,4,3),(1,5,4),(2,1,4),(2,2,4),(2,3,5),(2,4,3),(3,1,4),(3,2,4),(3,3,4),(3,4,4),(4,1,4),(4,4,4),(4,5,1);

/*Table structure for table `recreation_db` */

DROP TABLE IF EXISTS `recreation_db`;

CREATE TABLE `recreation_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `rating` varchar(255) default NULL,
  `type` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `website` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recreation_db` */

insert  into `recreation_db`(`id`,`img`,`title`,`rating`,`type`,`phone`,`time`,`location`,`website`,`area`) values (1,'swim1.png','Olympic size swimming pool','4.4','Swimming pool','9920090883','12:00pm - 11:00pm','La Kuchina, Shymala Hills, Bhopal, Madhya Pradesh','https://www.jehannuma.com/','Airoli'),(2,'swim2.png','Forbes advisor','3.6','Swimming pool','9920090883','7:00am - 11:00pm','Under the Mango Tree, 157','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','thane'),(3,'game1.png','Gaming hub at red door','4.5','Gaming hub','9920090883','12:00pm - 11:00pm','Momo Cafe, DB City Mall, Zone-I','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','nerul'),(4,'game2.png','Marketwatch','4.9','Gaming hub','9920090883','7:00am - 11:00pm','Dakshin Restaurant','https://www.jehannuma.com/','juinagar');

/*Table structure for table `restaurant_db` */

DROP TABLE IF EXISTS `restaurant_db`;

CREATE TABLE `restaurant_db` (
  `id` int(255) NOT NULL auto_increment,
  `img` varchar(255) default NULL,
  `name` varchar(255) default NULL,
  `rating` varchar(255) default NULL,
  `type` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `url` varchar(255) default NULL,
  `area` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `restaurant_db` */

insert  into `restaurant_db`(`id`,`img`,`name`,`rating`,`type`,`phone`,`time`,`address`,`url`,`area`) values (1,'la_kuchina.png','La Kuchina','4.4','Indian','1234567896','12:00pm - 11:00pm','La Kuchina, Shymala Hills, Bhopal, Madhya Pradesh','https://www.jehannuma.com/','rabale'),(2,'momo_cafe.png','Momo Cafe','4.5','Cafe','2587413698','6:30am - 11:30pm','Momo Cafe, DB City Mall, Zone-I, Maharana Pratap Nagar, Bhopal, Madhya Pradesh','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','nerul'),(3,'mango_tree.png','Under the Mango Tree','3.5','Italian','2587469852','7:00am - 11:00pm','Under the Mango Tree, 157, Shymala Hills, Bhopal, Madhya Pradesh 462013','https://www.jehannuma.com/','juinagar'),(4,'crystal_dew.png','Crystal Dew','3.9','Indian','7894562135','6:30am - 11:30pm','Crystal Dew, 2nd Floor, 201, Above INOX, C21 Mall, Hoshangabad Road, Bhopal, Madhya Pradesh','https://www.marriott.com/hotels/hotel-information/restaurant/bhocy-courtyard-bhopa','koparkhairane');

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

insert  into `usertable`(`id`,`username`,`email`,`mobile`,`password`) values (1,'a','yasj@gmail.com','8879343922','a'),(2,'b','yashsalvi1999@gmail.com','9930090883','hhshhs'),(3,'j','yashsalvi1999@gmail.com','1234567890','j'),(4,'k','yas@gmail.com','1234587649','k');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
