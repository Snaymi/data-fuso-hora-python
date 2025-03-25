from datetime import date, datetime, time, timedelta

#DATE TIME - Lidando com a data e hora
#Criando um objeto de DATA
hoje = date.today() #Retorna a data atual
print ("data de hoje", hoje)

#Criando um objeot de data e hora
agora = datetime.now() #Retorna a data e a hora atuais
print("Data e hora atuais: ", agora)

#Criando um objeto de hora
hora_especifica = time (14, 30, 0) # Define uma hora específica.
print("Hora específica: ", hora_especifica)

# __________________________\\ ________________________________

# Manipulando datas com "timedelta"
# Usaod para adicionar ousubtrair períodos de tempo e objetos

hoje = datetime.now()
daqui_a_7_dias = hoje + timedelta(days = 7)
print("Data daqui a 7 dias: ", daqui_a_7_dias)
#Muito usado para criar cronogramas, calcular prazos ou verificar diferença entre datas.

#____________________________\\ ________________________________

# Formatando e convertendo datas com strptime e strftime

#strftime - formatando datas e horários
#É usado para formatas um objeto de data ou hora em uma string formatada.
#Personalização \ "%d" - dia do mes \ "%m" - Mês \ "%Y" - Ano completo \ "%H" - hora (24h) \ "%M" - minuto

agora = datetime.now()
formato = agora.strftime("%d/%m/%Y %H:%M")
print("Data e hora formatados: ", formato)

#strptime - Convertendo strings para objetos de data
#Deve especificar o formato par agarantir que a conversão seja correta

data_str =  "25/03/2025 16:45"
formato = "%d/%m/%Y %H:%M"
data_convertida = datetime = datetime.strptime(data_str, formato)
print("Objeto datetime: ", data_convertida)

#Otimo para criar relatorios com datas legiveis.

#__________________________\\ _________________________

#Trabalhando com TIMEZONE
#pytz fornece informações sobre todos os fusos horários reconhecidos globalmente
#datetime podem ser "naive" (sem inf. sobre fuso horario) ou "aware" (com inf. do fuso.)

import pytz

#Fuso horário UTC
utc = pytz.UTC
agora_utc = datetime.now(utc)
print("Data e hora do UTC:", agora_utc)

#Fuso horario especficico (são paulo)
fuso_sp = pytz.timezone("America/Sao_Paulo")
agora_sp = agora_utc.astimezone(fuso_sp)
print("Data e hora em SP: ", agora_sp)

#_____________________\\______________________