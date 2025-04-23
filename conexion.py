import pymysql
import script_consulta_horarios
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='prueba')
	try:
		with conexion.cursor() as cursor:
			
			
			cursor.execute(script_consulta_horarios.consulta)
 
			# Con fetchall traemos todas las filas
			prueba = cursor.fetchall()
 
			# Recorrer e imprimir
			for nombres in prueba:
				print(nombres)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)