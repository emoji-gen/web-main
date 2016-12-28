--
-- emoji_log
--
ALTER TABLE `emoji_log`
  ADD `size_fixed` INTEGER UNSIGNED NOT NULL DEFAULT 0 AFTER `font`,
  ADD `align` VARCHAR(255) NOT NULL DEFAULT 'center' AFTER `size_fixed`,
  ADD `stretch` INTEGER UNSIGNED NOT NULL DEFAULT 0 AFTER `align`;
