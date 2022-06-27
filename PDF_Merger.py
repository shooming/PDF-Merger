import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

pdf_setting_options = 0

while(True):

    pdf_setting_options = int(input('''사용하실 옵션을 선택해 주세요
    [1] pdf 통합하기
    [2] pdf 분할하기
    [3] 종료
    > '''))
    
    if(pdf_setting_options < 3 and pdf_setting_options > 0):
        break

if(pdf_setting_options == 1):
    file_folder = input('현재 py파일이 있는 위치에 통합을 원하시는 파일이 있는 폴더를 놓고 폴더명을 적어주세요 : ')
    inte_file_name = input('통합하실 pdf의 파일 이름을 입력해주세요 (파일은 py파일이 있는 위치에 생성됩니다.) : ')

    inte_option = int(input('''통합 옵션선택
    [1] 일반통합 (별도 필요한 부분을 삭제하지 않고 전부 통합합니다.)
    [2] 동일한 페이지 제거(ex: 모든 파일 1페이지 2페이지가 표지일 경우 2입력시 모든 파일의 1페이지 2페이지 제거)
    > '''))

    files_path = os.getcwd()+'/'+file_folder
    files = sorted(os.listdir(files_path))

    merger = PdfMerger()

    if(inte_option == 1):
        for pdf in files:
            merger.append('./'+ file_folder + '/' + pdf)

        merger.write(inte_file_name + '.pdf')

    if(inte_option == 2):
        expcept_page = int(input('제거하실 페이지 범위 입력 : '))
        # division_page = int(input('''중간 구분페이지 추가하기
        # [1] 예 (구분페이지 추가시 파일 이름을 기준으로 파일이름이 들어간 페이지를 삽입합니다.)
        # [2] 아니오
        # > '''))
        for pdf in files:
            pdf_reader = PdfReader('./'+ file_folder + '/' + pdf)
            pages = len(pdf_reader.pages)
            # if(division_page == 1):

            merger.append(fileobj=pdf_reader, pages=(expcept_page, pages))

        merger.write(inte_file_name + '.pdf')

