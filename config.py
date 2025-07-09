# Configuración adicional con más secretos para la demo

# Conexión a base de datos con credenciales en la URL
DATABASE_CONNECTION = "postgresql://dbuser:mypassword123@db.example.com:5432/production_db"

# Token de autenticación API
API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Claves privadas RSA (dummy)
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4qI2C8H6r9oIsxM7WB5mRPz+9sP0rEp/xBm1Z5mYDPxBkJz8
xYGt2PbCnHCbE1E8mRQ8kPzLt6E5H4YpQkZb4kqHgFoS8xhDlE8E9PdG5pRzJ6s5
-----END RSA PRIVATE KEY-----"""

class DatabaseConfig:
    """Configuración de la base de datos con credenciales hardcodeadas"""
    
    def __init__(self):
        # Más ejemplos de malas prácticas
        self.db_password = "admin123456"
        self.redis_url = "redis://:mypassword@redis.example.com:6379/0"
        self.mongo_uri = "mongodb://admin:secretpass@mongodb.example.com:27017/mydb"
        
        # Token de Telegram Bot
        self.telegram_bot_token = "1234567890:AAEJlaT-8BZ2E8HJ7KVLhJ5VB2E8HJ7KVLN"
        
        # Webhook de Discord
        self.discord_webhook = "https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678"

def get_secret_key():
    """Función que retorna una clave secreta hardcodeada"""
    return "sk_live_51234567890abcdef1234567890abcdef12345678901234567890abcdef"
