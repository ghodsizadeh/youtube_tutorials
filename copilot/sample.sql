-- create user table with first name , last name , weatlh , email , password for postgres
CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(255) NOT NULL,
    `last_name` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);

-- inser values in user table
INSERT INTO `user` (`first_name`, `last_name`, `email`, `password`) VALUES
('John', 'Doe', 'Johh@mail.com', 'password'),

-- create inde for email on user table
Creat index `email_idx` on `user` (`email`);