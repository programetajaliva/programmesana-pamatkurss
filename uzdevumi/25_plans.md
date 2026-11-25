## Ievade
1. Programma pajautā spēlētājam ievadīt vārdu.
2. Programma pajautā spēlētājam ievadīt lielāko minamo skaitli.
3. Programma sagatavo slepeno skaitli.
4. Programma pajautā spēlētājam ievadīt minējumu.

## Apstrāde
5. Programma salīdzina spēlētāja minējumu ar slepeno skaitli.
6. Programma aprēķina iztērēto mēģinājumu skaitu.
7. Programma aprēķina iegūtos punktus.

## Izvade
8. Programma parāda spēlētājam paziņojumu par minējuma rezultātu.
9. Programma parāda spēlētājam kopējo mēģinājumu skaitu un punktus.

## Mainīgie

## | Mainīgā vārds | Datu tips | Ko glabā |
### | :--------------| :----------: | ------------------------:|
### | speletaja_vards | int | Spēlētāja ievadīto vārdu |
### | maksimalais_skaitlis | int | Lielāko iespējamo minamo skaitli |
### | meginajumu_skaits | int | Cik reizes spēlētājs jau ir minējis |
### | punkti` | int | Spēlētāja nopelnīto punktu skaitu |

### Formula
`punkti = maksimalais_skaitlis / meginajumu_skaits`

### Mainīgo izcelsme
* **No `input()` nāk:** `speletaja_vards`, `maksimalais_skaitlis`
* **Tiek izrēķināts:** `punkti` (un `meginajumu_skaits` palielinās pēc katra minējuma)


## Formulas pārbaude (testa vērtības)
* **Mazs komplekts:** `maksimalais_skaitlis = 10`, `meginajumu_skaits = 2` -> Rezultāts ar roku: `punkti = 5.0`
* **Vidējs komplekts:** `maksimalais_skaitlis = 50`, `meginajumu_skaits = 4` -> Rezultāts ar roku: `punkti = 12.5`
* **Liels komplekts:** `maksimalais_skaitlis = 1000`, `meginajumu_skaits = 8` -> Rezultāts ar roku: `punkti = 125.0`

### Secinājums
Formulu ir vērts pārbaudīt ar roku pirms programmas rakstīšanas, lai laikus pamanītu aprēķinu vai loģikas kļūdas (piemēram, dalīšanu ar nulli) un pārliecinātos, ka dators dod pareizu rezultātu.

