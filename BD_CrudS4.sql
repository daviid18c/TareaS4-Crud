-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.11-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para crud_s4web
DROP DATABASE IF EXISTS `crud_s4web`;
CREATE DATABASE IF NOT EXISTS `crud_s4web` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `crud_s4web`;

-- Volcando estructura para tabla crud_s4web.grupo
DROP TABLE IF EXISTS `grupo`;
CREATE TABLE IF NOT EXISTS `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla crud_s4web.grupo: ~0 rows (aproximadamente)
DELETE FROM `grupo`;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`id`, `descripcion`) VALUES
	(1, 'Activo'),
	(2, 'Pasivo'),
	(3, 'Patrimonio'),
	(4, 'Ingreso'),
	(5, 'Gastos');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla crud_s4web.plancuenta
DROP TABLE IF EXISTS `plancuenta`;
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `grupo` int(11) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `naturaleza` varchar(1) DEFAULT NULL,
  `estado` tinyint(4) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `FK__grupo` (`grupo`),
  CONSTRAINT `FK__grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla crud_s4web.plancuenta: ~0 rows (aproximadamente)
DELETE FROM `plancuenta`;
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
INSERT INTO `plancuenta` (`id`, `codigo`, `grupo`, `descripcion`, `naturaleza`, `estado`) VALUES
	(1, '01', 1, 'Caja', 'D', 1),
	(2, '02', 1, 'Banco', 'D', 1),
	(3, '03', 2, 'Cuenta por pagar', 'A', 1),
	(4, '04', 3, 'Capital Contable', 'A', 1),
	(5, '05', 4, 'Ventas', 'A', 1),
	(6, '06', 5, 'Compras', 'D', 1),
	(7, '07', 5, 'Arriendo', 'D', 0);
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
