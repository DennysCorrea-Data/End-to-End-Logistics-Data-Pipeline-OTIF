# End-to-End-Logistics-Data-Pipeline-OTIF
Diseño de Pipeline End-to-End (Python, SQL Server, SSIS, Power BI) para procesar +1.2M de registros y optimizar el indicador logístico OTIF en el sector industrial.
 Análisis Logístico y Optimización del Indicador OTIF: Pipeline End-to-End de Datos
Autor: Dennys Junior Correa Meza

Rol: Arquitecto de Datos / Data Analyst

Sector: Industria Química B2B

Volumen de Datos Procesado: +1.2 Millones de registros históricos

Resumen Ejecutivo
El presente proyecto documenta el diseño e implementación de un ecosistema integral de Inteligencia de Negocios e Ingeniería de Datos. El objetivo central fue diagnosticar, medir y proponer soluciones a la eficiencia operativa de la cadena de suministro, enfocándose en la métrica OTIF (On-Time In-Full). Se desarrolló una arquitectura completa que abarca desde la generación sintética de la muestra hasta la integración automatizada (ETL) y el despliegue de visualizaciones gerenciales interactivas.

Planteamiento del Problema Comercial
En la distribución de productos químicos industriales, el incumplimiento de la promesa de entrega paraliza las cadenas de producción de los clientes (B2B), generando penalidades financieras y daño reputacional. El desafío consistía en diagnosticar una aparente ineficiencia logística generalizada, procesando más de un millón de registros transaccionales para identificar si el cuello de botella residía en la falta de inventario, fallas de la flota de transporte externa, o procesos internos de despacho.

Arquitectura de la Solución Técnica
El flujo de datos se estructuró en cuatro fases críticas para garantizar escalabilidad, trazabilidad y limpieza de la información:

Generación de Datos: Desarrollo de scripts empleando Python para simular un volumen masivo de transacciones logísticas, controlando variables estadísticas como lead times, capacidades de flota y restricciones por sede logística.

Almacenamiento: Modelado de base de datos relacional y creación de vistas optimizadas para pre-procesar cálculos a nivel de servidor, reduciendo la carga computacional en la capa analítica.

Integración y ETL: Implementación de tuberías de datos mediante SQL Server Integration Services. Se automatizaron los procesos de extracción, transformación y carga, gestionando rigurosamente la corrección de codificación de caracteres especiales y la validación de tipos de datos.

Modelado Analítico: Diseño del modelo de datos en esquema de estrella, desarrollo de medidas analíticas complejas mediante DAX y creación de una interfaz de usuario en modo oscuro para maximizar el contraste y la legibilidad ejecutiva.

Hallazgos y Análisis de Causa Raíz
El procesamiento del modelo reveló información crítica que redefine la estrategia logística:

Diagnóstico de Crisis (OTIF Global): Se identificó un rendimiento crítico del 20.81% en el cumplimiento general.

Aislamiento del Cuello de Botella: La desagregación del KPI demostró un éxito operativo en la disponibilidad de inventario (80.17% In-Full), pero una deficiencia severa en la puntualidad de entrega (26.02% On-Time).

Desmitificación de Proveedores Tercerizados: El análisis comparativo demostró una varianza de error estadísticamente nula entre las múltiples empresas de transporte tercerizadas y la flota propia. Esto descarta a los transportistas como causa raíz.

Soluciones Estratégicas Planteadas
A partir de los datos analizados, se proponen las siguientes acciones correctivas:

Auditoría de Rampas: Dado que todos los transportistas presentan el mismo nivel de retraso, se recomienda auditar los tiempos de espera y procesos de estiba y carga en las plantas de origen.

Ajuste de Lead Times en ERP: Recalibrar la fecha de entrega prometida en el sistema comercial, añadiendo un margen de 24 a 48 horas operativas para alinear las expectativas del cliente con la capacidad logística real de la planta.

Establecimiento de Línea Base: Implementar el presente dashboard como herramienta de monitoreo diario para supervisar la convergencia hacia la meta corporativa estándar del 85% de cumplimiento OTIF.

Estructura del Repositorio
/Python_Scripts: Código fuente para la generación estadística del dataset inicial.

/SSIS_ETL: Documentación técnica y flujos de control en Integration Services.

/SQL_Queries: Scripts DDL y DML para la estructuración y consultas en SQL Server.

/PowerBI_Dashboard: Archivo fuente de la solución final.

Aviso Legal: El presente proyecto es un caso de estudio. Todos los datos, nombres de plantas y cifras presentadas son información sintética generada exclusivamente para demostrar competencias técnicas en arquitectura de datos y análisis de negocio. No contienen información confidencial de ninguna entidad real.
