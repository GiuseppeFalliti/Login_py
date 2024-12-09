```markdown
# Applicazione Web di Login e Registrazione

Questa applicazione è un semplice sistema di login e registrazione basato su **Flask** e **SQLite**. Consente agli utenti di registrarsi, accedere e visualizzare una dashboard dopo l'accesso.

---

## Struttura del Progetto

```
app/
├── app.py                   # File principale dell'applicazione Flask
├── templates/        # Directory contenente i template HTML
│   ├── index.html           # Pagina di login
│   ├── registrati.html      # Pagina di registrazione
│   ├── dashboard.html       # Pagina della dashboard
├── static/                  # File statici (CSS, immagini, ecc.)
│   ├── style.css            # Stile per la pagina di login
│   ├── style2.css           # Stile per la pagina di registrazione
└── users.db                 # Database SQLite (generato automaticamente)
```

---

## Requisiti

- Python 3.11 o versione successiva
- Librerie Python:
  - Flask
  - SQLite (incluso di default in Python)

---

## Installazione

1. **Clona il progetto**:
   ```bash
   git clone https://github.com/tuo-username/app-login-registrazione.git
   cd app-login-registrazione
   ```

2. **Installa i requisiti**:
   Se non hai Flask installato, usa il seguente comando:
   ```bash
   pip install flask
   ```

3. **Avvia il server Flask**:
   ```bash
   python app.py
   ```

4. **Visita l'applicazione**:
   Apri il browser e vai su [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Funzionalità

1. **Login**:
   - Inserisci il nome utente e la password per accedere.
   - Verifica delle credenziali tramite il database SQLite.

2. **Registrazione**:
   - Consente agli utenti di creare un account fornendo:
     - Nome utente
     - Nome
     - Cognome
     - Password (deve contenere almeno 8 caratteri, una lettera e un numero)
     - Data di nascita
   - I dati vengono salvati nel database SQLite.

3. **Dashboard**:
   - Mostra un messaggio di benvenuto agli utenti autenticati.

4. **Gestione degli errori**:
   - Campi mancanti o credenziali errate generano un messaggio di errore.

---

## Configurazione

- **Modifica della porta**:
  Per avviare l'applicazione su una porta diversa, modifica questa riga in `app.py`:
  ```python
  app.run(debug=True, port=5000)
  ```

- **Cartelle dei template e dei file statici**:
  I template HTML si trovano nella cartella `templates/`, e gli stili CSS nella cartella `static/`.

---

## Note Tecniche

- Il database viene inizializzato automaticamente alla prima esecuzione di `app.py` tramite la funzione `init_db()`.
- I messaggi di errore e successo utilizzano il sistema **Flash** di Flask.
- Il database `users.db` contiene la seguente tabella:
  ```sql
  CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      nome TEXT NOT NULL,
      cognome TEXT NOT NULL,
      password TEXT NOT NULL,
      data_nascita TEXT NOT NULL
  );
  ```

---

## Autore

**Giuseppe Falliti**  
E-mail: giuseppe.falliti5@gmail.com 
GitHub: [GiuseppeFalliti](https://github.com/GiuseppeFalliti)

---

## Licenza

Questo progetto è distribuito sotto la licenza **MIT**.
```
