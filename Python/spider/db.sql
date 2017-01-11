#DROP DATABASE IF EXISTS `wanghong`;
CREATE DATABASE `wanghong` DEFAULT SET utf8mb4 EFAULT COLLATE utf8mb4_general_ci;
USE `wanghong`
set names utf8mb4;

#DROP TABLE IF EXISTS `Table_Huajiao_Live;
CREATE TABLE `Table_Huajiao_Live(
    `FLiveId` INT UNSIGNED NOT NULL,
    `FUserId` INT UNSIGNED NOT NULL,
    `FWatches` INT UNSIGNED NOT NULL DEFAULT 0 COMMIT '观看人数',
    `FPraises` INT UNSIGNED NOT NULL DEFAULT 0 COMMIT '赞数',
    `FReposts` INT UNSIGNED NOT NULL DEFAULT 0 COMMIT 'unknown',
    `FReplies` INT UNSIGNED NOT NULL DEFAULT 0 COMMIT 'unknown',
    `FPublishTimestamp` INT UNSIGNED NOT NULL DEFAULT 0 COMMIT '发布日期',
)
