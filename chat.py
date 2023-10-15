import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect("group_chat.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL
    )
''')

# Create a table to store groups
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Groups (
        GroupID INTEGER PRIMARY KEY,
        GroupName TEXT NOT NULL
    )
''')

# Create a table to store group memberships
cursor.execute('''
    CREATE TABLE IF NOT EXISTS GroupMembers (
        GroupMemberID INTEGER PRIMARY KEY,
        UserID INTEGER,
        GroupID INTEGER,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (GroupID) REFERENCES Groups(GroupID)
    )
''')

# Create a table to store messages
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Messages (
        MessageID INTEGER PRIMARY KEY,
        GroupID INTEGER,
        UserID INTEGER,
        Content TEXT NOT NULL,
        Timestamp DATETIME NOT NULL,
        FOREIGN KEY (GroupID) REFERENCES Groups(GroupID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'group_chat.db' created successfully.")
