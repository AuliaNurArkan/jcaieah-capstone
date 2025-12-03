-- MySQL dump 10.13  Distrib 8.0.44, for macos15 (arm64)
--
-- Host: localhost    Database: moduleone
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car_rental`
--

DROP TABLE IF EXISTS `car_rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_rental` (
  `rental_id` int NOT NULL AUTO_INCREMENT,
  `car_type` text,
  `rental_duration` int DEFAULT NULL,
  `rental_cost` int DEFAULT NULL,
  `customer_gender` text,
  `rental_date` text,
  `branch_city` text,
  PRIMARY KEY (`rental_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_rental`
--

LOCK TABLES `car_rental` WRITE;
/*!40000 ALTER TABLE `car_rental` DISABLE KEYS */;
INSERT INTO `car_rental` VALUES (1,'SUV',3,300,'Male','2024-01-01','Jakarta'),(2,'Sedan',2,200,'Female','2024-01-02','Jakarta'),(3,'SUV',5,450,'Female','2024-01-03','Bandung'),(4,'Hatchback',1,100,'Male','2024-01-04','Bandung'),(5,'Sedan',4,350,'Female','2024-01-05','Surabaya'),(6,'SUV',7,600,'Male','2024-01-06','Surabaya'),(7,'Sedan',3,280,'Female','2024-01-07','Medan'),(8,'Hatchback',2,150,'Male','2024-01-08','Medan'),(9,'SUV',6,500,'Female','2024-01-09','Jakarta'),(10,'SUV',6,550,'Male','2024-01-10','Bandung');
/*!40000 ALTER TABLE `car_rental` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-03 23:30:38
