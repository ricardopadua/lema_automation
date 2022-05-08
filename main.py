import email
import imaplib
import logger_config
logger = logger_config.logger
from dotenv import load_dotenv

load_dotenv()


'''
Faz acesso ao e-mail e a caixa de entrada.
'''
def email_acess():    
    logger.info('email_acess')
    return None

''''
Faz a busca pelo e-mail desejado por título e data.
'''
def email_search():    
    logger.info('email_search')
    return None
    
'''
Faz o download da planilha em anexo no e-mail desejado.
'''
def extract_worksheet():    
    logger.info('extract_worksheet')
    return None

''' 
Faz o upload da planilha (no formato desejado) no google Drive.
'''
def drive_upload_file():    
    logger.info('drive_upload_file')
    return None

''''
Faz a conversão do arquivo para o formato desejado (Ex: .XLSX para .CSV).
'''
def convert_worksheet_format():    
    logger.info('convert_worksheet_format')
    return None

'''
Faz o upload do arquivo desejado em um ambiente web.
'''
def file_upload_to_web_admin():
    logger.info('file_upload_to_web_admin')
    return None

''''
Faz a limpeza (delete) do arquivo no diretório local, após ter armazenado na pasta de backup e upado na web.
'''
def clear_local_directory():
    logger.info('clear_local_directory')
    return None


def main():
    try:
        set_return = email_acess()
        set_return = email_search()
        set_return = extract_worksheet()
        set_return = drive_upload_file()
        set_return = convert_worksheet_format()
        set_return = file_upload_to_web_admin()
        set_return = clear_local_directory()
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()