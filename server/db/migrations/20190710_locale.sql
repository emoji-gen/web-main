--
-- emoji_log
--
ALTER TABLE `emoji_log`
  ADD `locale` VARCHAR(8) NOT NULL DEFAULT 'ja' AFTER `stretch`;

ALTER TABLE `emoji_log`
  ADD INDEX `key02` (`locale`, `generated_at`, `public_fg`);

ALTER TABLE `emoji_log` RENAME INDEX `generated_at_public_fg_idx` TO `key01`;
