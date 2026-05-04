import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración del volumen de datos para el caso de estudio
num_registros = 1200000
fecha_inicio = datetime(2023, 1, 1)

# Listas de datos maestros (anonimizadas para el portafolio)
plantas = ['Planta Norte', 'Planta Sur', 'Planta Este', 'Planta Oeste']
productos = ['Cloro Líquido', 'Soda Cáustica', 'Ácido Clorhídrico', 'Fosfato Bicálcico', 'Sulfato Férrico']
transportistas = ['Transportes Cruz', 'Dinet Logística', 'Flota Propia', 'Logística del Pacífico', 'Transportes Ransa']

# Generación del dataset sintético
data = {
    'ID_Guia_Remision': range(1000001, 1000001 + num_registros),
    'Planta_Origen': np.random.choice(plantas, num_registros),
    'Producto_Quimico': np.random.choice(productos, num_registros),
    'Transportista': np.random.choice(transportistas, num_registros),
    'Toneladas_Despachadas': np.random.uniform(5, 30, num_registros).round(2)
}

df = pd.DataFrame(data)

# Lógica de fechas y simulación de tiempos de entrega
df['Fecha_Pedido'] = [fecha_inicio + timedelta(days=np.random.randint(0, 850)) for _ in range(num_registros)]
df['Fecha_Entrega_Prometida'] = df['Fecha_Pedido'] + timedelta(days=2)

# Simulación de la problemática detectada (Bajo On-Time)
retraso_prob = 0.74
df['Dias_retraso'] = np.where(np.random.rand(num_registros) < retraso_prob, np.random.randint(1, 5), 0)
df['Fecha_Entrega_Real'] = df['Fecha_Entrega_Prometida'] + pd.to_timedelta(df['Dias_retraso'], unit='D')

# Flag de In-Full (80% de cumplimiento de inventario)
df['InFull_Flag'] = np.where(np.random.rand(num_registros) < 0.80, 1, 0)

# El dataset está listo para ser exportado y procesado vía SSIS a SQL Server
# print(df.head())
