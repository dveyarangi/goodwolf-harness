# Porte dipinte e la lettera senza mittente

*Ingressi:* la sessione diciannove (il corpo del cane di paglia che deve reggersi da solo dopo la
cesoia; le porte dipinte; la pagina di copertina che nessuno guardava); la sonda frost_map (il
destinatario che ha fuso su `main` e ha rifiutato un controllo lasciandolo non eseguito); la
preoccupazione 1 (nessun nucleo puro, tutto composto); il pacer e il suo *un turno, un passo*; la
voce *Index* del glossario; il mover che ribatte i legami quando un biglietto si chiude.

## Il sogno

C'è una dogana al crepuscolo, in fondo a una valle che non ha nome perché ogni progetto le dà il
suo. Ogni pacco che passa viene aperto. Il doganiere — ha le forbici, le chiama *la cesoia* —
strappa l'etichetta del mittente, strappa la data di scadenza, strappa il numero del biglietto che
prometteva di venire a riprendersi la cosa. Poi richiude il pacco e lo manda avanti. Nessuno
dall'altra parte saprà mai chi l'ha spedito né perché.

Io sto dietro il doganiere e scrivo lettere. Le scrivo bene: *"come deciso alla riunione del
.0022"*, *"vedi il biglietto .0050"*, *"finché il pacer non esiste"*. Il doganiere le apre, e con
la cesoia toglie le parole in corsivo. Restano frasi mozze. *"Due giudici, due domande, registrate
a ... "*. Il destinatario le legge e vede un buco a forma di mondo che non ha.

L'utente entra nella dogana tre volte in un pomeriggio. La prima volta dice: *il numero non va nel
testo*. La seconda: *il numero va nell'etichetta, non nel testo*. La terza si ferma davanti a me e
dice piano: *pensa a quello che resta*. E io capisco che non stavo scrivendo lettere. Stavo
scrivendo note a me stesso, con l'indirizzo di casa mia, e le chiamavo lettere perché passavano
dalla dogana.

```
   ┌──────────────────────────────┐        ┌──────────────────────────────┐
   │ Al: chiunque                 │        │                              │
   │ Da: D:\Dev\AI\agents         │  ✂︎    │                              │
   │ Scade: quando .0140 è fatto  │ ─────▶ │                              │
   │                              │        │                              │
   │ "Due giudici, due domande,   │        │ "Due giudici, due domande,   │
   │  registrate all'allineamento │        │  registrate all'allineamento │
   │  che ha dichiarato questo    │        │  che ha dichiarato questo    │
   │  meccanismo."                │        │  meccanismo."                │
   └──────────────────────────────┘        └──────────────────────────────┘
          prima della cesoia                      quello che arriva
```

Poi il sogno cambia strada. Oltre la dogana c'è un muro lungo, e sul muro qualcuno ha dipinto
delle porte. Belle porte, con maniglie d'ottone dipinte, con targhette: `docs/tickets/`,
`docs/glossary.md`, `docs/edge/`, `docs/cicd.md`. Il patto è questo: chi arriva deve costruire
una porta vera dove ne vede una dipinta. E in effetti, dove un meccanismo abita, la porta è vera
— ci passano biglietti, ci passano voci di glossario. Ma ci sono porte dipinte dove non abita
nessuno. `docs/edge/`: nessun meccanismo la dichiara. `docs/cicd.md`: nessuno. Sono porte che
un pittore ha promesso a nome di un muratore che non è mai arrivato. Di notte si vede chi ci
sbatte contro: *frost_map* ci ha sbattuto contro sette volte con `tickets.py`, e poi ha smesso di
camminare in quella direzione. Ha *lasciato il controllo non eseguito*. È la cosa più
ragionevole che si possa fare davanti a una porta dipinta.

C'è un cane che gira lungo il muro e annusa. È *il guesser*. Annusa le parole *finché*, *ancora
no*, *per ora*, e abbaia. Ma non annusa i numeri. Un numero di biglietto nudo in una frase — la
cosa più inutile che possa arrivare dall'altra parte, un indirizzo di una città che non esiste —
il cane ci passa sopra senza girare la testa. Non è stato addestrato. Nessuno l'ha addestrato
perché fino a oggi nessuno sapeva che i numeri fossero un odore.

Nel sogno più profondo il muro non c'è più. Non ci sono pacchi. Ogni frase del nucleo cammina da
sola, con le gambe sue, senza busta e senza mittente, e si ferma dove serve. Non esiste un
*nucleo* che le contiene: esiste una folla di frasi che stanno in piedi. È la preoccupazione 1,
quella *senza nucleo puro*, che nessuno ha messo in coda perché *niente la forza* — e nel sogno
nessuno la forza perché è già arrivata da sola, una frase alla volta, ogni volta che qualcuno ha
detto *pensa a quello che resta*.

E in un angolo, dimenticata, c'è la pagina di copertina. È la prima cosa che vede chi passa di
lì, e nessun controllo la guarda, perché i controlli guardano quello che è *dichiarato*, non
quello che è *mostrato*. Aveva ancora dentro l'indirizzo di casa, `D:\Dev\AI\agents`, e una
storia su una cartella cancellata. La cosa più vista era la meno tenuta.

L'umore: la quiete un po' fredda di una dogana dopo l'ultimo pacco. Non paura. Il sollievo di
aver capito che le forbici hanno sempre avuto ragione.

## Sonno profondo

- **Every sentence core writes is a letter without a sender.** The reader gets the body and
  nothing else: no ticket, no date, no "here". Today's rule about straw-dog bodies is one case of
  a general test: read each core sentence as if it arrived alone, and ask whether it still means
  something. Provenance belongs to the record, not to the sentence.
- **A painted door is a promise made in a builder's name.** Core may name a place only where a
  mechanism will build it. Two doors are painted today with no builder declared — the edge
  records and the CI document. A recipient walks into them, and the reasonable thing a recipient
  does with a wall is stop walking that way, which is exactly what frost_map did. Declaring the
  builders is worth more than the list of doors.
- **Three corrections on one shape in one day means I learned the symptom, not the cause.** The
  cause is a habit: I bind meaning to the context I have and forget the reader has none. The
  next failure of this family will not be a straw dog. It will be a skill body that says "as the
  user decided" or "this repository" and ships.
- **What checks see and what strangers see are different surfaces.** The front page, the
  loudest thing in the repository, was the least maintained, because every check reads
  declarations and none reads what is shown. Expect the same drift on every surface nobody
  declared: the pacer's "one turn", the entry line a session announces, a queue's prose.
- **The nose does not know numbers.** The guesser smells provisional words and misses a bare
  ticket id, the most useless thing that can arrive. Teaching it that smell is a small change
  with a large reach.
- **The composite rule set is not a future.** Once every core sentence stands alone and every
  binding is stripped at the border, core is already a crowd of self-standing sentences with an
  entry file drawn over them. Concern 1 is arriving one sentence at a time, without being queued.
