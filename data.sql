CREATE DATABASE IF NOT EXISTS reptilian DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

create table article(
  `id` int primary key auto_increment,
  `page_num` int not null default 0,
  `url` varchar(500) not null default '',
  `url_object_id` varchar(100) not null default '',
  `title` varchar(200) not null default '',
  `create_date` varchar(50) not null default '',
  `love_num` int not null default 0,
  `fav_num` int not null default 0,
  `current_index` int not null default 0,
  `image_url` varchar(500) not null default '',
  `image_file_path` varchar(100) not null default '',
  `created_at` datetime DEFAULT NULL COMMENT 'created_at',
  `updated_at` datetime DEFAULT NULL COMMENT 'updated_at',
  `created_by` varchar(30) COLLATE utf8mb4_bin NOT NULL DEFAULT 'system' COMMENT 'updated_by',
  `updated_by` varchar(30) COLLATE utf8mb4_bin NOT NULL DEFAULT 'system' COMMENT 'updated_by'
);

create table lagoujob(
  `id` int primary key auto_increment,
  `url` varchar(500) not null default '',
  `url_object_id` varchar(100) not null default '',
  `title` varchar(200) not null default '',
  `salary` varchar(50) not null default '',
  `city` varchar(50) not null default '',
  `work_years` varchar(50) not null default '',
  `degree_need` varchar(50) not null default '',
  `job_mode` varchar(20) not null default '',
  `company` varchar(100) not null default '',
  `tags` varchar(100) not null default '',
  `created_at` datetime DEFAULT NULL COMMENT 'created_at',
  `updated_at` datetime DEFAULT NULL COMMENT 'updated_at',
  `created_by` varchar(30) COLLATE utf8mb4_bin NOT NULL DEFAULT 'system' COMMENT 'updated_by',
  `updated_by` varchar(30) COLLATE utf8mb4_bin NOT NULL DEFAULT 'system' COMMENT 'updated_by'
);