import sqlite3
#Import database
database = "database.db"
class DB:
    def ejecutar_consulta(self,consulta,parametros = ()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(consulta,parametros)
            conn.commit()
            return result

