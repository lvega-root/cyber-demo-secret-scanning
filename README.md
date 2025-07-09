# Demo de Secret Scanning - GitHub Advanced Security

Este proyecto está diseñado para demostrar las capacidades del módulo de **Secret Scanning** de GitHub Advanced Security. Contiene varios tipos de secretos y credenciales dummy que deberían ser detectados por la herramienta.

## ⚠️ ADVERTENCIA
**TODAS las credenciales en este proyecto son DUMMY/FALSAS y están destinadas únicamente para propósitos de demostración. NO utilizar en producción.**

## Tipos de Secretos Incluidos

Este proyecto contiene ejemplos de los siguientes tipos de secretos que GitHub Advanced Security puede detectar:

### 1. Credenciales de AWS
- AWS Access Key ID: `AKIAIOSFODNN7EXAMPLE`
- AWS Secret Access Key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

### 2. Tokens de GitHub
- GitHub Personal Access Token: `ghp_*`

### 3. Claves de API de Servicios
- Stripe Secret Key: `sk_test_*`
- Slack Webhook URL
- Twilio Auth Token

### 4. Credenciales de Base de Datos
- Conexiones PostgreSQL con credenciales embebidas

## Archivos con Secretos

Los secretos están distribuidos en varios archivos para simular diferentes escenarios:

1. **`credentials.yml`** - Archivo de configuración YAML con múltiples tipos de credenciales
2. **`main.py`** - Código Python con credenciales hardcodeadas
3. **`.env.example`** - Variables de entorno con secretos
4. **`package.json`** - Metadatos con API keys

## Instalación y Ejecución

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la demo
python main.py
```

## Qué Esperar de GitHub Advanced Security

Cuando este código se suba a un repositorio con GitHub Advanced Security habilitado, debería detectar:

- ✅ AWS Access Keys y Secret Keys
- ✅ GitHub Personal Access Tokens  
- ✅ Stripe API Keys
- ✅ Slack Webhook URLs
- ✅ Credenciales de base de datos
- ✅ Otros patrones de secretos conocidos

## Resultados de la Demo

Al ejecutar `python main.py`, verás:

1. Simulación de conexión a AWS usando credenciales del archivo YAML
2. Uso de credenciales hardcodeadas (mala práctica)
3. Simulación de conexión a base de datos
4. Listado de otros tipos de tokens detectados

## Mejores Prácticas de Seguridad

Este proyecto demuestra **qué NO hacer**. En un entorno real:

- ❌ **Nunca** hardcodear credenciales en el código fuente
- ❌ **Nunca** subir archivos de configuración con secretos reales
- ❌ **Nunca** incluir credenciales en variables de entorno versionadas
- ✅ **Usar** servicios de gestión de secretos (AWS Secrets Manager, Azure Key Vault, etc.)
- ✅ **Usar** variables de entorno no versionadas
- ✅ **Habilitar** GitHub Advanced Security Secret Scanning
- ✅ **Revisar** regularmente los hallazgos de seguridad

## Estructura del Proyecto

```
cyber-demo-secret-scanning/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias Python
├── main.py                  # Script principal con credenciales dummy
├── credentials.yml          # Archivo YAML con múltiples secretos
├── .env.example            # Variables de entorno con secretos
└── package.json            # Metadatos con API keys
```

## Recursos Adicionales

- [GitHub Advanced Security Documentation](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning)
- [Secret Scanning Partner Patterns](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns)
- [Best Practices for Managing Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

**Nota**: Este proyecto es únicamente educativo. Todas las credenciales son ficticias y no proporcionan acceso a ningún servicio real.
