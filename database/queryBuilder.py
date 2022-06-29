def selectBySku(key):
    args = {
        "sku": key
    }

    query = """
    SELECT r.Articulo_ID, a.NOMBRE, SUM(CASE WHEN r.TIPO_MOVTO = 'E' THEN r.UNIDADES * 1 ELSE r.UNIDADES * -1 END) AS final_inventory
    FROM DOCTOS_IN_DET r
    INNER JOIN ARTICULOS a ON r.ARTICULO_ID = a.ARTICULO_ID
    Group by r.ARTICULO_ID, a.NOMBRE
    Where r.ARTICULO_ID={sku}
    """.format(**args)

    return query
