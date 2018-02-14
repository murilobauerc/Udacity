# Módulo I - Aula 3


# extraindo apenas o link de uma página (href...)

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')


start_link = page.find('<a href=') # encontrar a posição do link
start_quote = page.find("", start_link)  # apenas o que estiver dentro das aspas, partindo da posição de start_link ('<a href=')
end_quote = page.find("", start_quote + 1) # encontrar o fim das aspas, por isso precisamos pular a primeira aspas (start_quote + 1) resulta somente na segunda ocorrencia de aspas
url = page[start_quote + 1: end_quote] # por fim, a variavel url terá apenas a url http://udacity.com
