from flask import Flask, request, redirect, url_for, render_template, flash
import sqlite3

app = Flask(__name__, template_folder="templates")
app.secret_key = "super_secret_key"  # Per abilitare i messaggi flash

# Funzione per inizializzare il database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            cognome TEXT NOT NULL,
            password TEXT NOT NULL,
            data_nascita TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route per la registrazione
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    password = request.form.get('password')
    data_nascita = request.form.get('data')

    if not all([username, nome, cognome, password, data_nascita]):
        flash("Tutti i campi sono obbligatori!")
        return redirect(url_for('register_page'))

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, nome, cognome, password, data_nascita)
            VALUES (?, ?, ?, ?, ?)
        """, (username, nome, cognome, password, data_nascita))
        conn.commit()
        conn.close()
        flash("Registrazione completata con successo! Effettua il login.")
        return redirect(url_for('login_page'))  # Reindirizza a login
    except sqlite3.IntegrityError:
        flash("Il nome utente è già in uso.")
        return redirect(url_for('register_page'))  # Ritorna alla pagina di registrazione in caso di errore

# Route per il login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username, password]):
        flash("Tutti i campi sono obbligatori!")
        return redirect(url_for('login_page'))

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user[1] == password:
        # Successo nel login, reindirizza alla dashboard
        return redirect(url_for('dashboard_page'))
    else:
        flash("Credenziali non valide!")
        return redirect(url_for('login_page'))

# Route per servire le pagine HTML
@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template('registrati.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

# Avvio dell'applicazione
if __name__ == '__main__':
    init_db()  # Inizializza il database alla prima esecuzione
    app.run(debug=True, port=5000)  # Avvia il server Flask sulla porta 5000
