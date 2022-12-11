lahtefail = input("Palun kirjuta lähtefaili nimi:")
tulemusfail = input("Palun kirjuta tulemusfaili nimi:")
fail_sisse = open(lahtefail, "rt")
fail_valja = open(tulemusfail, "wt")
for line in fail_sisse:
	fail_valja.write(line.replace('Hello', 'Tere'))
fail_sisse.close()
fail_valja.close()
# https://pythonexamples.org/python-replace-string-in-file/