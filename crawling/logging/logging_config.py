import logging


# 로깅 설정 함수
def setup_logging():
    # 기본 로깅 설정
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("app.log"),  # 로그를 파일에 기록
                            logging.StreamHandler()  # 로그를 콘솔에도 출력
                        ])
