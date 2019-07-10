--
-- emoji_log
--
CREATE TABLE `emoji_log` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `text` varchar(255) NOT NULL,
  `color` char(8) NOT NULL,
  `back_color` char(8) NOT NULL,
  `font` varchar(255) NOT NULL,
  `size_fixed` int(10) unsigned NOT NULL DEFAULT '0',
  `align` varchar(255) NOT NULL DEFAULT 'center',
  `stretch` int(10) unsigned NOT NULL DEFAULT '1',
  `locale` varchar(8) NOT NULL DEFAULT 'ja',
  `public_fg` int(10) unsigned NOT NULL DEFAULT '1',
  `generated_at` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `key01` (`generated_at`,`public_fg`),
  KEY `key02` (`locale`,`generated_at`,`public_fg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

