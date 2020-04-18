CREATE TABLE `registered_users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `title` text COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` text COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` text COLLATE utf8mb4_general_ci NOT NULL,
  `street` text COLLATE utf8mb4_general_ci NOT NULL,
  `city` text COLLATE utf8mb4_general_ci NOT NULL,
  `province` text COLLATE utf8mb4_general_ci NOT NULL,
  `postal_code` text COLLATE utf8mb4_general_ci NOT NULL,
  `country` text COLLATE utf8mb4_general_ci NOT NULL,
  `phone` text COLLATE utf8mb4_general_ci NOT NULL,
  `email` text COLLATE utf8mb4_general_ci NOT NULL,
  `newsletter` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `registered_users` (`user_id`, `title`, `first_name`, `last_name`, `street`, `city`, `province`, `postal_code`, `country`, `phone`, `email`, `newsletter`) VALUES ('1', 'Mrs', 'ysxc', 'rr', '123 street', 'sydney', '4', '3', 'Canada', 'w', 'w', 'on'),
('2', 'Mr', 'ysxc', 'rr', '123 street', 'sydney', '4', '3', 'Canada', 'w', 'w', 'off');
