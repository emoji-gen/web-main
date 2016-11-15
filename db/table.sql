--
-- emoji_log
--
CREATE TABLE `emoji_log` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(255) NOT NULL,
  `color` CHAR(8) NOT NULL,
  `back_color` CHAR(8) NOT NULL,
  `font` VARCHAR(255) NOT NULL,
  `public_fg` INTEGER UNSIGNED NOT NULL DEFAULT 1,
  `generated_at` DATETIME NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(`id`),
	INDEX `generated_at_public_fg_idx` (`generated_at`, `public_fg`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8;

