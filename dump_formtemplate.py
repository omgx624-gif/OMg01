p='myapp/templates/user/user_form.html'
s=open(p,encoding='utf-8').read()
lines=s.splitlines()
for i in range(275,305):
    print(i+1, lines[i])