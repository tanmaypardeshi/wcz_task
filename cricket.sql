-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: cricket
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `match_details`
--

DROP TABLE IF EXISTS `match_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_details` (
  `match_id` int NOT NULL,
  `team_id` int NOT NULL,
  `no_of_4s` int NOT NULL,
  `no_of_6s` int NOT NULL,
  `no_of_wickets` int NOT NULL,
  `score` int NOT NULL,
  `isFirstInnings` tinyint(1) NOT NULL,
  PRIMARY KEY (`match_id`,`team_id`),
  KEY `team_id` (`team_id`),
  CONSTRAINT `match_details_ibfk_1` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`),
  CONSTRAINT `match_details_ibfk_2` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_details`
--

LOCK TABLES `match_details` WRITE;
/*!40000 ALTER TABLE `match_details` DISABLE KEYS */;
INSERT INTO `match_details` VALUES (1,1,5,3,6,250,1),(1,3,4,4,10,138,0),(2,2,8,7,3,144,0),(2,8,6,7,10,140,1),(3,1,8,4,4,246,0),(3,5,6,2,8,240,1),(4,7,6,2,8,240,1),(4,8,8,4,4,246,0),(5,7,2,9,9,222,0),(5,9,4,7,7,300,1),(6,4,2,9,9,222,1),(6,6,5,5,2,340,0),(7,10,6,6,8,348,0),(7,15,4,6,10,345,1),(8,3,3,4,10,180,0),(8,7,5,6,7,240,1);
/*!40000 ALTER TABLE `match_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matches`
--

DROP TABLE IF EXISTS `matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matches` (
  `match_id` int NOT NULL AUTO_INCREMENT,
  `home_team` int NOT NULL,
  `away_team` int NOT NULL,
  `winner_team` int NOT NULL,
  `man_of_the_match` varchar(30) NOT NULL,
  `date_played` date NOT NULL DEFAULT '2020-10-25',
  PRIMARY KEY (`match_id`),
  KEY `home_team` (`home_team`),
  KEY `away_team` (`away_team`),
  KEY `winner_team` (`winner_team`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`home_team`) REFERENCES `team` (`team_id`) ON DELETE CASCADE,
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`away_team`) REFERENCES `team` (`team_id`) ON DELETE CASCADE,
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`winner_team`) REFERENCES `team` (`team_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matches`
--

LOCK TABLES `matches` WRITE;
/*!40000 ALTER TABLE `matches` DISABLE KEYS */;
INSERT INTO `matches` VALUES (1,1,3,1,'Mithali Raj','2020-10-25'),(2,8,2,2,'Dane van Niekerk','2020-10-23'),(3,1,5,1,'Smriti Mandhana','2020-09-25'),(4,8,7,8,'Ayabonga Khaka','2020-09-15'),(5,9,7,9,'Chinelle Henry','2020-10-15'),(6,6,4,6,'Sophie Devine','2020-12-15'),(7,15,10,10,'Kim Garth','2020-08-14'),(8,7,3,7,'Nida Dar','2020-12-06');
/*!40000 ALTER TABLE `matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(40) NOT NULL,
  `coach_name` varchar(30) NOT NULL,
  `captain_name` varchar(30) NOT NULL,
  PRIMARY KEY (`team_id`),
  UNIQUE KEY `unique_team_name` (`team_name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'India','Woorkeri Raman','Mithali Raj'),(2,'Australia','Mathew Mott','Meg Lanning'),(3,'England','Mark Lane','Heather Knight'),(4,'Sri Lanka','Lanka de Silva','Chamari Atapattu'),(5,'Bangladesh','Anju Jain','Salma Khatun'),(6,'New Zealand','Robert Carter','Sophie Devine'),(7,'Pakistan','David Hemp','Bismah Maroof'),(8,'South Africa','Hilton Moreeng','Dane van Niekerk'),(9,'West Indies','Courtney Walsh','Stafanie Taylor'),(10,'Ireland','Ed Joyce','Laura Delany'),(15,'Canada','George Codrington','Suthershini Sivanantham'),(21,'Zimbabwe','Zoe Goss','Mary-Anne Musonda');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-28 19:44:11
