import pyodbc

# Mismos datos que tu application.properties de Spring Boot
SERVER = "localhost,1433"
DATABASE = ""
USERNAME = ""
PASSWORD = ""
TABLA = ""

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"   # igual que "Trust Server Certificate" en SSMS
)


def main():
    try:
        with pyodbc.connect(conn_str, timeout=5) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {TABLA}")

            columnas = [col[0] for col in cursor.description]
            filas = cursor.fetchall()

            print(" | ".join(columnas))
            print("-" * 60)
            for fila in filas:
                print(" | ".join(str(valor) for valor in fila))

            print(f"\nTotal de registros: {len(filas)}")

    except pyodbc.Error as e:
        print("Error al conectar o consultar:", e)


if __name__ == "__main__":
    main()