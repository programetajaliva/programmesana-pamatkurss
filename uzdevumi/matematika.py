print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 3)

mantas = int(input("Cik mantu ir? "))
somas_ietilpiba = int(input("Cik mantu ietilpst somā? "))
pilnas = mantas // somas_ietilpiba
pari = mantas % somas_ietilpiba
print(pari)
print(pilnas)
print(f"Vajag {pilnas} somas un {pari} mantas paliks pāri.")
videji = mantas / somas_ietilpiba
print(f"Vidēji {videji:.1f} somas")
# Figūriekavās pierakstīts 1f nozīmē, ka dati tiek formatēti kā peldošā komata skaitlis ar precīzi vienu zīmi aiz komata 
