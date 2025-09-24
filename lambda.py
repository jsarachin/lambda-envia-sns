import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda iniciada com sucesso!")
    logger.info(event)

    sns = boto3.client("sns")
    topic_arn = "arn:aws:sns:us-east-1:418272773416:topico-aula-7"

    mensagem = event.get("mensagem")
    assunto = event.get("assunto")

    response = sns.publish(
            TopicArn=topic_arn,
            Message=mensagem,
            Subject=assunto
        )

    logger.info(f"Mensagem publicada: {response}")
    return "Mensagem enviada ao SNS!"
