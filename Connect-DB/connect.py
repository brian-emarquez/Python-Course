# -*- coding: utf-8 -*-
import pyodbc
 
SERVIDOR = "brian"
DATABASE = "SIE"
USUARIO = "briandb"
PASSWORD = "briandb"
 
 
def get_producto_por_sku(sku):
    if not sku:
        return {}
 
    cnxn = None
    try:
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={SERVIDOR};'
            f'DATABASE={DATABASE};'
            #f'UID={USUARIO};'
            #f'PWD={PASSWORD}'
            'Trusted_Connection=yes'
        )
 
        query = """
            SELECT p.Sku, p.Descripcion,
                m.codigo AS codMarca,
                c.Codigo AS codClasi,
                dep.Codigo AS codDep
            FROM SIE.dbo.Producto p
            INNER JOIN SIE.dbo.Marca m ON m.Id = p.Marca_Id
            INNER JOIN SIE.dbo.Clasificacion c ON p.Clasificacion_Id = c.Id
            INNER JOIN SIE.dbo.Departamento dep ON dep.Id = c.Departamento_Id
            WHERE p.Sku = ?
        """
 
        cursor = cnxn.cursor()
        cursor.execute(query, (sku,))
        row = cursor.fetchone()
 
        if not row:
            print("⚠️ --->SKU no encontrado o sin acceso")
            return {}
 
        return {
            'sku': row[0],
            'descripcion': row[1],
            #'marca': row[2],
            #'clasificacion': row[3],
            #'departamento': row[4],
        }
 
    except Exception as e:
        print("❌ Error:", str(e))
        return {}
 
    finally:
        if cnxn:
            cnxn.close()
 
 
if __name__ == "__main__":
    resultado = get_producto_por_sku("002086453")
    print(resultado)