## Ievade
1. Programma sagatavo slepeno skaitli.
2. Programma pajautā spēlētājam ievadīt minējumu.

## Apstrāde
3. Programma salīdzina spēlētāja minējumu ar slepeno skaitli.
4. Programma aprēķina iztērēto mēģinājumu skaitu.

## Izvade
5. Programma parāda spēlētājam paziņojumu par minējuma rezultātu.
6. Programma parāda spēlētājam kopējo mēģinājumu skaitu.


##  | Mainīgā vārds          | Datu tips         | Ko glabā                                                           |
### | :--------------------- | :---------------- :| --- --------------------:                                         |
### | `speletaja_vards`      | `str`              | Spēlētāja ievadīto vārdu                                          |
### | `maksimalais_skaitlis` | `int`              | Lielāko iespējamo minamo skaitli                                  |
### | `meginajumu_skaits`    | `int`              | Cik reizes spēlētājs jau ir minējis                               |
### | `punkti`               | `float`            | Spēlētāja nopelnīto punktu skaitu                                 |

### Formula
`punkti = maksimalais_skaitlis / meginajumu_skaits`

### Mainīgo izcelsme
* **No `input()` nāk:** `speletaja_vards`, `maksimalais_skaitlis`
* **Tiek izrēķināts:** `punkti` (un `meginajumu_skaits` palielinās pēc katra minējuma)

