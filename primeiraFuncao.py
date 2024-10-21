def lambda_handler(event, context):
    # Mensagem simples para teste
    return {
        'statusCode': 200,
        'body': 'Hello, World! Este é o meu teste de Lambda!',
        'ambiente': 'MINHA_VAR'
    }