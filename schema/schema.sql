USE master;
GO
-- create database 'chat' to host our schema
IF NOT EXISTS(SELECT * from sys.databases WHERE name='chat')
BEGIN
	CREATE DATABASE chat;
END
GO

USE chat
-- create table 'user' to store set of recipients
IF NOT EXISTS(SELECT * from chat.INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'user')
BEGIN
	CREATE TABLE [user]
	(
		id BIGINT PRIMARY KEY NOT NULL IDENTITY(1,1),
		username VARCHAR(200) NOT NULL CONSTRAINT uq_user_username UNIQUE(username),
		created_date_utc DATETIME NOT NULL CONSTRAINT df_user_created DEFAULT GETUTCDATE()
	)
END
GO
-- create table 'message' to store received message
IF NOT EXISTS(SELECT * from chat.INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'message')
BEGIN
	CREATE TABLE [message]
	(
		id BIGINT PRIMARY KEY NOT NULL IDENTITY(1,1),
		[user_id] BIGINT NOT NULL CONSTRAINT fk_user_id REFERENCES [user] (id),
		[text] TEXT NOT NULL,
		expiration_date_utc DATETIME NOT NULL,
		created_date_utc DATETIME NOT NULL CONSTRAINT df_message_created DEFAULT GETUTCDATE()
	)
END
GO
-- create non-clustered on 'username' column in 'user'
IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_user_username')
BEGIN
    CREATE NONCLUSTERED INDEX idx_user_username ON [user] ([username])
END
GO

-- create non-clustered on 'user_id' column in 'message'
IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'idx_message_user_id')
BEGIN
    CREATE NONCLUSTERED INDEX idx_message_user_id ON [message] ([user_id])
END
GO