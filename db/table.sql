--
-- emoji_log
--
CREATE TABLE `emoji_log` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(255) NOT NULL,
  `color` CHAR(8) NOT NULL,
  `back_color` CHAR(8) NOT NULL,
  `font` VARCHAR(255) NOT NULL,
  `size_fixed` INTEGER UNSIGNED NOT NULL DEFAULT 0,
  `align` VARCHAR(255) NOT NULL DEFAULT 'center',
  `stretch` INTEGER UNSIGNED NOT NULL DEFAULT 0,
  `public_fg` INTEGER UNSIGNED NOT NULL DEFAULT 1,
  `generated_at` DATETIME NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(`id`),
	INDEX `generated_at_public_fg_idx` (`generated_at`, `public_fg`)
) ENGINE=InnoDB DEFAULT CHARACTER SET utf8mb4;

