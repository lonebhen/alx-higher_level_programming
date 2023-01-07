-- a script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS `second_table`(
    `id` INT,
    `name` VARCHAR,
    `score` INT
);

INSERT INTO `second_table`(`id`,`name`,`score`) VALUES (`id` = 1, `name` = “John”, `score` = 10);
INSERT INTO `second_table`(`id`,`name`,`score`) VALUES (`id` = 2, `name` = “Alex”, `score` = 3);
INSERT INTO `second_table`(`id`,`name`,`score`) VALUES (`id` = 3, `name` = “Bob”, `score` = 14);
INSERT INTO `second_table`(`id`,`name`,`score`) VALUES (`id` = 4, `name` = “George”, `score` = 8);