import datetime
import click
import sqlite3
import time

def rsvp(userName, yyyymmdd, hhmm, attend, conn):
    query = """SELECT rowid, name FROM participants WHERE name like ?"""
    result = conn.execute(query, ('%'+userName+'%',)).fetchall()
    if len(result) == 0:
        raise NameError('No users matching', userName)
    if len(result) > 1:
        raise NameError('Multiple users matching', userName, result)
    userId = result[0][0]
    
    query = """SELECT rowid, yyyymmdd, hhmm, event FROM dateTimes WHERE yyyymmdd=? AND hhmm=?"""
    result = conn.execute(query, (yyyymmdd, hhmm)).fetchall()
    if len(result) == 0:
        raise NameError('No dates matching', yyyymmdd, hhmm)
    if len(result) > 1:
        raise NameError('Multiple dates matching', yyyymmdd, hhmm, result)
    dateId = result[0][0]
    eventId = result[0][3]
    
    now = int(time.time() * 1000)
    query = """INSERT OR REPLACE INTO rsvps
    (rowid, event, participant, dateTime, attend, timestamp) VALUES
    ((SELECT rowid FROM rsvps WHERE event=? AND participant=? AND dateTime=?), ?, ?, ?, ?, ?)"""
    result = conn.execute(query, (eventId, userId, dateId, eventId, userId, dateId, int(attend), now)).fetchall()
    return result

@click.command()
@click.option('--attend', help='Attend integer value')
@click.option('--file', prompt='SqLite file', help='SqLite file to read')
@click.option('--name', help='Participant name')
@click.option('--hhmm', help='hour:minute')
@click.option('--yyyymmdd', help='Year-month-day')
def run(file, name, yyyymmdd, hhmm, attend):
    conn = sqlite3.connect(file)
    result = rsvp(name, yyyymmdd, hhmm, attend, conn)
    conn.commit()
    conn.close()
    return result

if __name__ == '__main__':
    run()
