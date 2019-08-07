import sqlite3
import datetime


connection = sqlite3.connect('teke.db')
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                alias TEXT,
                mention TEXT NOT NULL,
                sex INTEGER DEFAULT 0,
                lvl INTEGER DEFAULT 1,
                exp INTEGER DEFAULT 0,
                gold INTEGER DEFAULT 0,
                social REAL DEFAULT 0.00 CHECK(social >= -100.00 AND social <= 100.00),
                teke_cont INTEGER DEFAULT 0,
                "cumple" TEXT
    )""")


def crear_usuario(id, name, mention):
    sql = """INSERT INTO users (id, name, mention) VALUES ("{}", "{}", "{}")""".format(id, name, mention)
    try:
        c.execute(sql)
        print("Se inserto a: {}".format(name))
    except:
        pass
    connection.commit()


def alias_set(id, alias):
    sql = """UPDATE users SET alias = {} WHERE id = "{}" """.format(alias, id)
    c.execute(sql)
    connection.commit()


def sex_set(id, sex):
    sql = """UPDATE users SET sex = {} WHERE id = "{}" """.format(sex, id)
    c.execute(sql)
    connection.commit()


def cumple_set(id, cumple: datetime.date):
    sql = """UPDATE users SET cumple = "{}" WHERE id = {} """.format(str(cumple), id)
    c.execute(sql)
    connection.commit()


def lvl_add(id, lvl):
    sql = """UPDATE users SET lvl = lvl+{} WHERE id = "{}" """.format(lvl, id)
    c.execute(sql)
    connection.commit()


def exp_add(id, exp):
    sql = """UPDATE users SET exp = exp+{} WHERE id = "{}" """.format(exp, id)
    c.execute(sql)
    connection.commit()


def gold_add(id, gold):
    sql = """UPDATE users SET gold = gold+{} WHERE id = "{}" """.format(gold, id)
    c.execute(sql)
    connection.commit()


def teke_cont_add(id, teke_cont):
    sql = """UPDATE users SET teke_cont = teke_cont+{} WHERE id = "{}" """.format(teke_cont, id)
    c.execute(sql)
    connection.commit()


def social_add(id, social):
    sql = """UPDATE users SET social = social+{} WHERE id = "{}" """.format(social, id)
    c.execute(sql)
    connection.commit()


def get_user(id):
    sql = """SELECT * FROM users WHERE id = "{}" """.format(id)
    c.execute(sql)
    return (c.fetchone())


def get_campo(id, campo: str):
    sql = """SELECT {} FROM users WHERE id = "{}" """.format(campo, id)
    c.execute(sql)
    return (c.fetchone()[0])


def get_cumple(id):
    sql = """SELECT {} FROM users WHERE id = "{}" """.format('cumple', id)
    c.execute(sql)
    fecha = c.fetchone()[0]
    if fecha != None:
        fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')

    return fecha


def get_today_cumple():
    sql = "SELECT id FROM users WHERE strftime('%m-%d', cumple) = strftime('%m-%d', 'now')"
    c.execute(sql)
    return c.fetchall()


def check_mujer(id):
    sql = """SELECT sex FROM users WHERE id = "{}" """.format(id)
    c.execute(sql)
    return bool(c.fetchone()[0])


def top(campo: str):
    sql = """SELECT id, name, {} FROM users ORDER BY {} DESC LIMIT 5 """.format(campo, campo)
    c.execute(sql)
    return c.fetchall()


# Test
# print(check_mujer(349902467636527104))
# print(check_mujer(475845470808440854))
# print(check_mujer(297375724774490112))
print(top('teke_cont'))
