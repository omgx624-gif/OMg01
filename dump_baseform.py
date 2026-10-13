s=open('myapp/forms.py',encoding='utf-8').read()
i=s.find('class _UserBaseForm')
chunk=s[i:i+2400]
j=chunk.find('    def __init__')
open('dump_init.txt','w',encoding='utf-8').write(chunk[j:j+1400])
print('ok')