/* PROYECTO: Dashboard de Control Logístico - Operaciones Químicas
   DESCRIPCIÓN: Creación de la vista para el cálculo de indicadores OTIF
   AUTOR: Dennys Junior Correa Meza
*/

CREATE VIEW VW_Indicadores_OTIF AS
SELECT 
    ID_Guia_Remision,
    Fecha_Pedido,
    Fecha_Entrega_Real,
    Fecha_Entrega_Prometida,
    Transportista,
    Planta_Origen,
    Producto_Quimico,
    Cliente_Destino,
    Toneladas_Despachadas,
    
    -- Flag para On-Time (A tiempo): 1 si se entregó antes o igual a la fecha prometida
    CASE 
        WHEN Fecha_Entrega_Real <= Fecha_Entrega_Prometida THEN 1 
        ELSE 0 
    END AS OnTime_Flag,
    
    -- Flag para In-Full (Completo): Simulación basada en cumplimiento de carga
    -- (En un caso real se compararía Cantidad Pedida vs Cantidad Entregada)
    InFull_Flag, 
    
    -- Cálculo de OTIF: 1 si se cumple tiempo Y cantidad, de lo contrario 0
    CASE 
        WHEN (CASE WHEN Fecha_Entrega_Real <= Fecha_Entrega_Prometida THEN 1 ELSE 0 END) = 1 
             AND InFull_Flag = 1 THEN 1 
        ELSE 0 
    END AS OTIF_Flag,

    -- Contador de despachos para métricas de volumen
    1 AS Total_Despachos

FROM Fact_Logistica; -- Reemplaza con el nombre real de tu tabla base si es diferente
