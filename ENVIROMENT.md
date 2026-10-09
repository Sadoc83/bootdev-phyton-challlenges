# 🛠️ Reporte de Configuración de Entorno Local y Mitigación de Riesgos

## 📝 Resumen del Caso
Durante el despliegue inicial de la estación de trabajo local en una arquitectura **Mac Intel Core i5**, se identificaron bloqueos críticos en el sistema operativo debido a solicitudes excesivas de almacenamiento (20 GB a 40 GB) por parte de las dependencias nativas de Apple (Xcode Command Line Tools). 

Este documento registra la estrategia heurística aplicada para aislar el entorno, mitigar los riesgos de falta de espacio en disco y validar el funcionamiento de **Git** y **Python 3** bajo un consumo menor a **300 MB**.

---

## 🔍 Diagnóstico de Bloqueos e Incidentes (Troubleshooting)

### ❌ Incidente 1: Conflicto de Dependencias en Git
* **Síntoma:** Visual Studio Code arrojaba un error persistente exigiendo la instalación completa de herramientas de desarrollo de Apple.
* **Causa Raíz:** Falta de una ruta explícita hacia el binario de Git local.
* **Estrategia de Mitigación:** Se detectó que la aplicación **GitHub Desktop** ya contaba con un motor de Git embebido. Se procedió a reutilizar dicha dependencia editando el archivo de configuración global `settings.json` en VS Code para evitar la redundancia de software.
* **Ruta Enlazada:** `/Applications/GitHub Desktop.app/Contents/Resources/app/git/bin/git`

### ❌ Incidente 2: Simulación de Descarga Masiva (Python 3)
* **Síntoma:** El comando trampa del sistema (`/usr/bin/python3`) interceptaba la consola y exigía 20 GB de espacio en disco.
* **Estrategia de Mitigación:** Descarga e inyección del paquete binario ligero oficial desde Python.org, junto con la ejecución manual del script de seguridad `Install Certificates.command` para habilitar conexiones seguras (SSL).

### ❌ Incidente 3: Excepción por Error de Sintaxis (ZSH)
* **Síntoma:** Error de consola `zsh: command not found: wich`.
* **Análisis de QA:** Error de tipografía (*typo*) en la entrada de datos del usuario. Se corrigió la sintaxis al comando estándar de UNIX `which` para auditar las variables de entorno de forma exitosa.

---

## 🟢 Validación Final del Entorno (Smoke Test)

Para garantizar la integridad del entorno antes de iniciar el desarrollo en **Boot.dev** y **TripleTen**, se ejecutó una auditoría de rutas logrando los siguientes resultados exitosos:

1. **Verificación de Origen de Python:**
   * **Comando:** `which python3`
   * **Resultado Obtenido:** `/Library/Frameworks/Python.framework/Versions/3.x/bin/python3`
   * **Estado:** **EXITOSO** (Entorno aislado y ligero confirmado).

2. **Verificación de Conectividad SSL:**
   * **Comando:** `import urllib.request`
   * **Resultado Obtenido:** Conexión exitosa a servidores de producción sin excepciones de certificados.
   * **Estado:** **EXITOSO**.

---

## 💡 Lecciones Aprendidas para el Rol de QA
1. **Heurística sobre Fuerza Bruta:** No siempre la instalación por defecto es la mejor; analizar los recursos limitados del cliente (almacenamiento en disco) permite encontrar soluciones más eficientes.
2. **Importancia de la Sintaxis:** Un solo carácter erróneo rompe la comunicación con el sistema operativo. La precisión en los comandos de consola es equivalente a la precisión requerida al escribir scripts de prueba automatizados.
