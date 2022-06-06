#_____________SQL_To_Create_Database_Tables___________
def create_schema():
    CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS User (
        id           INTEGER PRIMARY KEY,
        first_name   TEXT,
        last_name    TEXT,
        phone        TEXT,
        email        TEXT    NOT NULL
                            UNIQUE,
        password     TEXT    NOT NULL,
        active       INTEGER DEFAULT (1) 
                            NOT NULL,
        date_created TEXT    NOT NULL,
        hire_date    TEXT,
        user_type    TEXT    NOT NULL
                            DEFAULT user
        );
    '''

    CREATE_COMPETENCY_TABLE = '''
    CREATE TABLE IF NOT EXISTS Competency (
            id           INTEGER PRIMARY KEY,
            name         TEXT    NOT NULL,
            date_created TEXT    NOT NULL
        );
    '''

    CREATE_ASSESSMENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS Assessment (
            id            INTEGER PRIMARY KEY,
            name          TEXT    NOT NULL,
            type          TEXT,
            date_created  TEXT,
            competency_id INTEGER REFERENCES Competency (id) 
        );
    '''

    CREATE_ASS_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS Assessment_Result (
            id            INTEGER PRIMARY KEY,
            user_id       INTEGER REFERENCES User (id),
            assessment_id INTEGER REFERENCES Assessment (id),
            score         INTEGER NOT NULL,
            date_taken    TEXT    NOT NULL,
            manager_id    INTEGER REFERENCES User (id) 
        );
    '''



#________For_verifying_Users_In_Database_______________
SELECT_USER_BY_EMAIL = '''
SELECT * FROM User WHERE email=?
'''



#______________View_Menu_Querys_______________
VIEW_ALL_USERS = 'SELECT * FROM User'


#________________________________Add______________________________________________________________

ADD_USER = '''
INSERT INTO User(first_name, last_name, phone, email, password, date_created, hire_date, user_type)
VALUES(?,?,?,?,?,?,?,?)
'''

ADD_COMP = '''
INSERT INTO Competency(name, date_created)
VALUES(?,?)
'''

ADD_ASSESS_TO_COMP = '''
INSERT INTO Assessment(name,date_created,competency_id)
VALUES(?,?,?) 
'''

ADD_ASSESS_RESULT_FOR_USER = '''
INSERT INTO Assessment_Result(user_id,assessment_id,score,date_taken,manager_id)
VALUES(?,?,?,?,?)
'''


UPDATE_FIRST = '''
UPDATE User
SET
    first_name = ?
WHERE id = ?
'''

UPDATE_LAST = '''
UPDATE User
SET
    last_name = ?
WHERE id = ?
'''
UPDATE_PHONE = '''
UPDATE User
SET
    phone = ?
WHERE id = ?
'''
UPDATE_EMAIL = '''
UPDATE User
SET
    email = ?
WHERE id = ?
'''



UPDATE_USER_BY_ID = '''
UPDATE User
SET
    first_name = ?,
    last_name = ?,
    phone = ?,
    email = ?,
    password = ?,
    date_created = ?,
    hire_date = ?,
WHERE id = ?;
'''
