import os
a = os.system("pandoc -s zuoxichen_2000012103.tex -o zuoxichen_2000012103.docx")
if a == 0:
    print("success")
    os.startfile("zuoxichen_2000012103.docx")
else:
    print(f"error!\nErrorType:{a}")
os.system("pause")