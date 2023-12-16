-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: student
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `c`
--

DROP TABLE IF EXISTS `c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `c` (
  `cno` int NOT NULL AUTO_INCREMENT,
  `cname` char(20) DEFAULT NULL,
  `credi` int DEFAULT NULL,
  `cdept` char(10) DEFAULT NULL,
  `tname` char(8) DEFAULT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `c`
--

LOCK TABLES `c` WRITE;
/*!40000 ALTER TABLE `c` DISABLE KEYS */;
INSERT INTO `c` VALUES (1,'python',4,'软土','王晓名'),(2,'数据结构',4,'软开','刘红'),(3,'离散数学',4,'软物','李严劲'),(4,'计算机原理',6,'软土','王晓名'),(5,'数据库原理',4,'软开','吴志刚'),(6,'Windows技术',4,'软开','吴志刚'),(7,'编译原理',4,'软开','蒋莹岳'),(8,'系统结构',6,'软开','刘红'),(9,'计算机网络',6,'软开','刘红'),(10,'c语言',4,'软土','王晓名'),(11,'操作系统',4,'软开','蒋莹岳'),(12,'高等数学',4,'软物','李严劲'),(13,'概率论',5,'软物','李严劲');
/*!40000 ALTER TABLE `c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s`
--

DROP TABLE IF EXISTS `s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `sname` char(8) DEFAULT NULL,
  `sex` char(2) DEFAULT NULL,
  `age` char(2) DEFAULT NULL,
  `sdept` char(10) DEFAULT NULL,
  `logn` char(20) DEFAULT NULL,
  `pswd` char(20) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s`
--

LOCK TABLES `s` WRITE;
/*!40000 ALTER TABLE `s` DISABLE KEYS */;
INSERT INTO `s` VALUES (1,'张三','男','19','软土','S1','S1'),(2,'刘八','男','20','软开','S2','S2'),(3,'李四','男','22','软开','S3','S3'),(4,'张六','女','21','软件','S4','S4'),(5,'刘七','女','22','软土','S5','S5'),(6,'刘九','男','21','软物','S6','S6'),(7,'王五','男','22','软开','S7','S7'),(8,'宣二','女','18','软物','S8','S8'),(9,'柳一','女','19','软开','S9','S9');
/*!40000 ALTER TABLE `s` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sc`
--

DROP TABLE IF EXISTS `sc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sc` (
  `sno` int NOT NULL,
  `cno` int NOT NULL,
  `grade` int NOT NULL,
  PRIMARY KEY (`sno`,`cno`),
  KEY `cno` (`cno`),
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`cno`) REFERENCES `c` (`cno`),
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`sno`) REFERENCES `s` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sc`
--

LOCK TABLES `sc` WRITE;
/*!40000 ALTER TABLE `sc` DISABLE KEYS */;
INSERT INTO `sc` VALUES (1,2,56),(1,4,78),(2,6,66),(2,8,88),(2,12,78),(3,1,88),(3,13,76),(4,1,67),(4,2,76),(4,11,78),(5,1,67),(5,2,78),(6,3,91),(6,10,78),(7,5,78),(8,6,78),(9,3,67),(9,7,78),(9,9,78);
/*!40000 ALTER TABLE `sc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-16 18:23:38
