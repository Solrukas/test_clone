from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re

path = input('PDF 파일 경로 : ')

#pdf 환경
rsrcmgr = PDFResourceManager() 
retstr = StringIO()
codec = 'utf-8'
laparams = LAParams()

#파일오픈
fout = open('./pdf.txt', 'wb')
device = TextConverter(rsrcmgr, fout, codec=codec, laparams=laparams)
fp = open(path, 'rb')
interpreter = PDFPageInterpreter(rsrcmgr, device)

#pdf 설정 값
password = ""
maxpages = 0 
caching = True
pagenos=set()

for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
   interpreter.process_page(page)

fp.close()
device.close()
str = retstr.getvalue()
retstr.close()
fout.close()

#필터링
ft = open('./pdf.txt','r')
txt = ft.read()
st = txt

fter1 = "((?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))-?[1-4][0-9]{6})" # 주민 등록 번호 정규 표현식
fter2 = "(01[016789]-?[0-9]{3,4}-?[0-9]{4})" # 전화 번호 정규 표현식
#fter1 = "((?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))-?[1-4][0-9]{6})(\D)" # 주민 등록 번호 정규 표현식
#fter2 = "(01[016789]-?[0-9]{3,4}-?[0-9]{4})(\D)" # 전화 번호 정규 표현식

print('유출이 의심되는 주민등록번호 : ', re.findall(fter1, st))
print('유출이 의심되는 전화번호 : ', re.findall(fter2, st))
#print('유출이 의심되는 주민등록번호 : ', [x[0] for x in re.findall(fter1, st)]) # 제일 앞 튜플만 출력
#print('유출이 의심되는 전화번호 : ', [x[0] for x in re.findall(fter2, st)])
