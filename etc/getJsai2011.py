import commands
for i in range(1000):
    commands.getstatusoutput("wget https://kaigi.org/jsai/webprogram/2011/pdf/" + str(i) + ".pdf")

