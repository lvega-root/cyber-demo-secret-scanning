#!/usr/bin/env python3
"""
Demo de Secret Scanning - GitHub Advanced Security
Este script muestra ejemplos de diferentes tipos de secretos que pueden ser detectados
por GitHub Advanced Security Secret Scanning.
"""

import yaml
import boto3
import os
from typing import Dict, Any

# Credenciales hardcodeadas (BAD PRACTICE - Para demo)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def load_credentials() -> Dict[str, Any]:
    """
    Carga las credenciales desde el archivo YAML.
    """
    try:
        with open('credentials.yml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    except FileNotFoundError:
        print("Error: credentials.yml no encontrado")
        return {}
    except yaml.YAMLError as e:
        print(f"Error al parsear YAML: {e}")
        return {}

def connect_to_aws(access_key: str, secret_key: str, region: str = 'us-east-1'):
    """
    Simula conexión a AWS usando las credenciales.
    """
    try:
        # Esto es solo para demo - no se conecta realmente
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        
        # Simular cliente S3
        s3_client = session.client('s3')
        print(f"✓ Simulando conexión a AWS con región: {region}")
        return s3_client
    except Exception as e:
        print(f"Error al conectar con AWS: {e}")
        return None

def simulate_database_connection(db_config: Dict[str, Any]):
    """
    Simula conexión a base de datos.
    """
    print(f"✓ Simulando conexión a DB: {db_config['host']}:{db_config['port']}")
    print(f"  Usuario: {db_config['username']}")
    # La password no se imprime por seguridad (aunque es dummy)

def main():
    """
    Función principal que demuestra el uso de credenciales.
    """
    print("=== Demo de Secret Scanning ===")
    print("Este código contiene varios tipos de secretos que GitHub Advanced Security puede detectar:")
    print()
    
    # Cargar credenciales desde archivo
    credentials = load_credentials()
    
    if not credentials:
        print("❌ No se pudieron cargar las credenciales")
        return
    
    # Usar credenciales de AWS
    aws_config = credentials.get('aws', {})
    if aws_config:
        print("1. Credenciales de AWS desde archivo:")
        connect_to_aws(
            aws_config['access_key_id'],
            aws_config['secret_access_key'],
            aws_config['region']
        )
    
    # Usar credenciales hardcodeadas (mala práctica)
    print("\n2. Credenciales hardcodeadas en código:")
    connect_to_aws(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    
    # Simular conexión a base de datos
    db_config = credentials.get('database', {})
    if db_config:
        print("\n3. Credenciales de base de datos:")
        simulate_database_connection(db_config)
    
    # Mostrar otros tipos de secretos
    api_keys = credentials.get('api_keys', {})
    if api_keys:
        print("\n4. Tokens y API Keys detectados:")
        for key, value in api_keys.items():
            print(f"  - {key}: {value[:20]}...")
    
    services = credentials.get('services', {})
    if services:
        print("\n5. Claves de servicios externos:")
        for service, key in services.items():
            print(f"  - {service}: {key[:20]}...")
    
    print("\n=== Fin de la demo ===")
    print("GitHub Advanced Security debería detectar estos secretos en:")
    print("- credentials.yml")
    print("- Este archivo Python")
    print("- Cualquier commit que los contenga")

if __name__ == "__main__":
    main()
