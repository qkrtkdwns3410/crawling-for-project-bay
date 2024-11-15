import logging
import os

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

import crawling.logging.logging_config as logging_config

# 로깅 설정
logging_config.setup_logging()
logger = logging.getLogger(__name__)

# .env 파일 로드
load_dotenv()

# 이메일 비밀번호 호출
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

logger.info(f'EMAIL, PASSWORD: {EMAIL}, {PASSWORD}')

# chromeDriver 위치설정
