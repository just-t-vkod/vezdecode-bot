import sqlite3 as sql

con = sql.connect('data/photos.db', check_same_thread = False)
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS `photos` (`id` INT, `url` INT, `like` INT, `dislike` INT)")
cur.execute("CREATE TABLE IF NOT EXISTS `users` (`id` INT, `url` STR, `vote` INT)")

def addPhoto(id, link):
    cur = con.cursor()
    cur.execute(f"INSERT INTO `photos` VALUES ('{id}', '{link}', 0, 0)")
    con.commit(); cur.close()

def getPhoto(user_id):
    cur = con.cursor()
    cur.execute("SELECT * FROM photos ORDER BY RANDOM() LIMIT 1")
    resultPhoto = cur.fetchall()
    cur.execute("SELECT * from users where id = ?", (user_id,))
    resultUser = cur.fetchall()
    con.commit(); cur.close()
    return (resultPhoto[0][0], resultPhoto[0][1],  [i[1] for i in resultUser])

def vote(user_id, id, vote):
    cur = con.cursor()
    if vote:
        cur.execute('SELECT like FROM `photos` WHERE id = ?', (id,))
        up = cur.fetchall()[0][0] + 1
        cur.execute(
                    'UPDATE photos SET like = ? WHERE id = ?', (up, id))
    else:
        cur.execute('SELECT dislike FROM `photos` WHERE id = ?', (id,))
        down = cur.fetchall()[0][0] + 1
        cur.execute(
                    'UPDATE photos SET dislike = ? WHERE id = ?', (down, id))
    cur.execute(
            'INSERT INTO `users` VALUES (?, ?, ?)', (user_id, id, vote))
    con.commit(); cur.close()

def getData(user_id):
    cur = con.cursor()
    cur.execute('SELECT vote FROM `users` WHERE id = ?', (user_id,))
    statUser = cur.fetchall()
    cur.execute('SELECT url FROM photos WHERE like > 0 ORDER BY like DESC LIMIT 8')
    statPhotos = cur.fetchall()
    con.commit(); cur.close()
    return [[i[0] for i in statUser], [i[0] for i in statPhotos]]
