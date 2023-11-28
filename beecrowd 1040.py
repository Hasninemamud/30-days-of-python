N1, N2, N3, N4 = map(input(int()).split)
avrg = (N1+N2+N3+N4)/4
print("Media:",avrg)
if avrg <= 7.0:
    print("Aluno aprovado.")
elif avrg > 5:
    print("Aluno reprovado.")
elif avrg <= 5 and avrg <= 6.9:
    print("Aluno em exame.")

