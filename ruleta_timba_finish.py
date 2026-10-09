import tkinter as tk
import random
import time
from tkinter import messagebox
import winsound

# =====================================================
# BANCO DE PREGUNTAS
# =====================================================
BANCO_PREGUNTAS = {
    "Redes": {
        "facil": [
            {
                "pregunta": "¿Qué significa IP?",
                "opciones": ["Internet Process", "Internal Program", "Internet Protocol", "International Port"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué hace un router?",
                "opciones": ["Imprime documentos", "Dirige datos entre redes", "Reproduce musica", "Guarda archivos"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué es un protocolo de red?",
                "opciones": ["Un juego", "Un conjunto de reglas de comunicación", "Un hardware", "Un cable"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué es una topología de red?",
                "opciones": ["Forma de conexión de una red", "Un antivirus", "Un navegador", "Un archivo"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué es internet?",
                "opciones": ["Una red mundial de redes", "Un videojuego", "Un cable", "Un sistema operativo"],
                "correcta": 0
            }
        ],
        "medio": [
            {
                "pregunta": "¿Para qué sirve una dirección IP?",
                "opciones": ["Guardar archivos", "Identificar un dispositivo en una red", "Crear videojuegos", "Aumentar señal Wi-Fi"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué tipo de conexión suele ofrecer un router doméstico?",
                "opciones": ["Bluetooth", "Wi-Fi", "HDMI", "USB"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué protocolo se usa para navegar en sitios web?",
                "opciones": ["HTTP", "MP3", "JPG", "PNG"],
                "correcta": 0
            },
            {
                "pregunta": "¿En qué topología todos los equipos se conectan a un punto central?",
                "opciones": ["Anillo", "Bus", "Estrella", "Malla"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué significan las siglas WWW?",
                "opciones": ["World Wide Web", "Web World Work", "Wireless Web World", "World Web Wide"],
                "correcta": 0
            }
        ],
        "dificil": [
            {
                "pregunta": "¿Qué versión de IP utiliza direcciones de 128 bits?",
                "opciones": ["IPv4", "IPv5", "IPv6", "IPv3"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué dispositivo conecta normalmente el router para brindar acceso a internet?",
                "opciones": ["Un módem", "Un teclado", "Un monitor", "Una impresora"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué protocolo se utiliza para transferir archivos entre computadoras?",
                "opciones": ["FTP", "HTML", "RAM", "CPU"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué topología sigue funcionando aunque falle una conexión entre dos nodos gracias a múltiples rutas?",
                "opciones": ["Bus", "Malla", "Anillo", "Estrella"],
                "correcta": 1
            },
            {
                "pregunta": "¿Quién es considerado el creador de la World Wide Web?",
                "opciones": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Elon Musk"],
                "correcta": 2
            }
        ]
    },
    "Ciberseguridad": {
        "facil": [
            {
                "pregunta": "¿Qué es un malware?",
                "opciones": ["Programa malicioso", "Antivirus", "Hardware", "Router"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué busca el phishing?",
                "opciones": ["Mejorar internet", "Robar datos", "Actualizar Windows", "Aumentar FPS"],
                "correcta": 1
            },
            {
                "pregunta": "¿Cuál es una contraseña segura?",
                "opciones": ["123456", "password", "M@t!4s#89X", "abc123"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué hace un firewall?",
                "opciones": ["Bloquea accesos no autorizados", "Aumenta FPS", "Descarga juegos", "Limpia teclado"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué es un ataque DDoS?",
                "opciones": ["Antivirus", "Ataque que satura servidores", "Hardware", "Navegador"],
                "correcta": 1
            }
        ],
        "medio": [
            {
                "pregunta": "¿Qué tipo de malware puede replicarse automáticamente?",
                "opciones": ["Spyware", "Gusano", "Adware", "Rootkit"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué característica suele tener un correo phishing?",
                "opciones": ["Diseño profesional solamente", "Archivos de música", "Enlaces sospechosos y urgencia", "Buen rendimiento"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué método mejora la seguridad de una contraseña?",
                "opciones": ["Autenticación en dos pasos", "Compartirla con amigos", "Usar solo números", "Escribirla en papel"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué hace un firewall de red?",
                "opciones": ["Mejora gráficos", "Borra virus automáticamente", "Instala programas", "Filtra tráfico entrante y saliente"],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué objetivo tiene un ataque de fuerza bruta?",
                "opciones": ["Mejorar internet", "Adivinar contraseñas", "Limpiar archivos", "Actualizar drivers"],
                "correcta": 1
            }
        ],
        "dificil": [
            {
                "pregunta": "¿Qué malware cifra archivos para pedir rescate?",
                "opciones": ["Spyware", "Troyano", "Keylogger", "Ransomware"],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué técnica suplanta una web legítima para robar datos?",
                "opciones": ["Spoofing", "Minería", "Sniffing", "Debugging"],
                "correcta": 0
            },
            {
                "pregunta": "¿Cuál es la función principal de un hash en contraseñas?",
                "opciones": ["Mostrar la contraseña", "Compartir datos", "Almacenar contraseñas de forma segura", "Aumentar velocidad"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué protocolo se utiliza comúnmente en firewalls para filtrar tráfico web seguro?",
                "opciones": ["FTP", "HTTPS", "SMTP", "POP3"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué significa DDoS?",
                "opciones": ["Distributed Denial of Service", "Data Download System", "Digital Defense Service", "Direct Domain Server"],
                "correcta": 0
            }
        ]
    },
    "IA": {
        "facil": [
            {
                "pregunta": "¿Cómo aprende un algoritmo de Machine Learning a reconocer patrones?",
                "opciones": ["Se lo memoriza porque viene programado de fábrica.", "Buscando en diccionarios físicos.", "Analizando miles de ejemplos y datos históricos.", "Adivinando al azar en cada intento."],
                "correcta": 2
            },
            {
                "pregunta": "¿A qué se parecen vagamente las Redes Neuronales Artificiales en su estructura básica?",
                "opciones": ["A las neuronas del cerebro humano.", "A las páginas de un libro.", "A una fila de supermercado.", "A las piezas de un motor de combustión."],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué es principalmente ChatGPT?",
                "opciones": ["Un buscador de internet como Google.", "Un modelo de lenguaje en formato de chat interactivo.", "Un juego de estrategia en línea.", "Un programa para editar fotos profesionales."],
                "correcta": 1
            },
            {
                "pregunta": "Si un brazo robótico en una fábrica coloca siempre la misma pieza en un auto sin intervención humana, ¿qué está haciendo?",
                "opciones": ["Automatizando una tarea repetitiva.", "Alucinando datos.", "Aprendiendo por refuerzo.", "Hackeando el sistema."],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué tipo de archivos o contenido puede crear una IA Generativa?",
                "opciones": ["Solo texto plano.", "Solo archivos de audio comprimido.", "Solo hojas de cálculo matemáticas.", "Textos, imágenes, música y videos nuevos."],
                "correcta": 3
            }
        ],
        "medio": [
            {
                "pregunta": "¿Qué diferencia al Machine Learning del software tradicional?",
                "opciones": ["El software tradicional es mucho más rápido para cualquier tarea.", "En ML la computadora descubre las reglas a partir de los datos, en vez de recibir las reglas ya programadas.", "El Machine Learning no utiliza código de programación.", "El software tradicional solo funciona si está conectado a internet."],
                "correcta": 1
            },
            {
                "pregunta": "¿Cómo se llaman las etapas internas de una Red Neuronal que procesan la información entre la entrada y la salida?",
                "opciones": ["Capas superficiales.", "Capas visibles.", "Capas ocultas (Hidden layers).", "Capas terminales."],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué significan las siglas 'GPT' en ChatGPT?",
                "opciones": ["Generative Pre-trained Transformer.", "General Protocol Technology.", "Graphical Program Text.", "Global Process Turing."],
                "correcta": 0
            },
            {
                "pregunta": "¿Cuál es un beneficio clave de la Automatización con IA en comparación con la automatización clásica basada en reglas fijas?",
                "opciones": ["Que consume mucha menos energía eléctrica.", "Que puede adaptarse a cambios en el entorno y tomar decisiones ante situaciones imprevistas.", "Que nunca requiere mantenimiento de software.", "Que es completamente gratuita de implementar."],
                "correcta": 1
            },
            {
                "pregunta": "¿A qué se refiere el conceptó de 'Alucinación' en una IA generativa?",
                "opciones": ["A cuando el sistema se congela por falta de memoria RAM.", "A un efecto visual tridimensional en la pantalla.", "A cuando la IA genera información incorrecta o falsa pero la redacta con total seguridad.", "Al proceso de apagado automático por sobrecalentamiento."],
                "correcta": 2
            }
        ],
        "dificil": [
            {
                "pregunta": "En Machine Learning, ¿qué ocurre cuando un modelo sufre de 'Overfitting' (Sobreajuste)?",
                "opciones": ["El modelo es demasiado simple y no aprende nada de los datos.", "El modelo memoriza tanto los datos de entrenamiento que falla al intentar predecir con datos nuevos.", "El modelo borra su propia base de datos por seguridad.", "El algoritmo tarda demasiados días en terminar de procesar."],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué algoritmo se utiliza principalmente para entrenar redes neuronales ajustando los pesos según el error obtenido?",
                "opciones": ["Backpropagation (Retropropagación).", "Algoritmo de Dijkstra.", "Ordenamiento Burbuja (Bubble Sort).", "Búsqueda Binaria Indexada."],
                "correcta": 0
            },
            {
                "pregunta": "¿Cuál es la tecnología o arquitectura base que permitió el desarrollo de ChatGPT y sus capacidades actuales?",
                "opciones": ["Redes Neuronales Convolucionales (CNN).", "Máquinas de Vectores de Soporte (SVM).", "Arquitectura Transformer (Transformadores).", "Filtros de Bayes Markovianos."],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué es la 'RPA' (Automatización Robótica de Procesos) when combined with AI?",
                "opciones": ["Un robot físico que limpia servidores.", "Un sistema que solo copia y pega archivos de texto simples.", "Una técnica para hackear plataformas web mediante bots masivos.", "Automatización Inteligente que imita acciones humanas en software e interpreta pantallas complejas."],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué tipo de modelos matemáticos compiten entre sí (un generador y un discriminador) para crear imágenes realistas en IA generativa?",
                "opciones": ["Modelos de Regresión Logística Lineal.", "Redes Generativas Antagónicas (GANs).", "Árboles de Decisión Profundos.", "Redes Neuronales Recurrentes (RNN)."],
                "correcta": 1
            }
        ]
    },
    "Linux": {
        "facil": [
            {
                "pregunta": "¿Qué es Linux principalmente?",
                "opciones": ["Un antivirus creado por Microsoft.", "Un sistema operativo de código abierto.", "Un programa para editar videos.", "Un tipo de memoria RAM."],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué comando se utiliza para listar archivos y carpetas en Linux?",
                "opciones": ["ls", "dirlinux", "openfiles", "showfolder"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué representa el símbolo '/' en Linux?",
                "opciones": ["Un archivo oculto del sistema.", "Un usuario administrador.", "El directorio raíz del sistema.", "Un disco duro externo."],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué comando se utiliza para cambiar de directorio?",
                "opciones": ["move", "changepath", "switchdir", "cd"],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué tipo de sistema es Linux?",
                "opciones": ["Exclusivo para videojuegos.", "Multiusuario y multitarea.", "Diseñado solo para celulares.", "Privado y totalmente cerrado."],
                "correcta": 1
            }
        ],
        "medio": [
            {
                "pregunta": "¿Qué comando permite crear una nueva carpeta en Linux?",
                "opciones": ["mkdir", "newfolder", "makedirfile", "foldercreate"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué hace el comando 'chmod'?",
                "opciones": ["Elimina archivos dañados.", "Reinicia permisos automáticamente.", "Modifica permisos de archivos y carpetas.", "Crea usuarios root."],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué usuario tiene control total del sistema en Linux?",
                "opciones": ["adminlinux", "root", "superpc", "masteruser"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué comando muestra la ruta actual del directorio?",
                "opciones": ["whereami", "locate", "pathdir", "pwd"],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué gestor de paquetes utiliza Ubuntu y Debian?",
                "opciones": ["APT", "InstallEX", "DNF-Windows", "PackSystem"],
                "correcta": 0
            }
        ],
        "dificil": [
            {
                "pregunta": "¿Qué comando se utiliza para buscar texto dentro de archivos en Linux?",
                "opciones": ["searchtxt", "grep", "filehunt", "textscan"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué significa que Linux sea 'Open Source'?",
                "opciones": ["Que su código fuente puede ser modificado y distribuido.", "Que Linux solo funciona online.", "Que no necesita licencia.", "Que únicamente empresas pueden usarlo."],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué comando permite cambiar el propietario de un archivo?",
                "opciones": ["owneredit", "chmoduser", "chown", "fileadmin"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué sistema de permisos utiliza Linux principalmente?",
                "opciones": ["Seguridad por huella digital.", "Acceso mediante IP dinámica.", "Claves de hardware interno.", "Permisos de lectura, escritura y ejecución."],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué componente de Linux actúa como núcleo del sistema operativo?",
                "opciones": ["Bash Ultimate", "Kernel", "Linux Loader", "Terminal Engine"],
                "correcta": 1
            }
        ]
    },
    "Desarrollo": {
        "facil": [
            {
                "pregunta": "¿Qué significa HTML?",
                "opciones": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "High Text Machine Language", "Hyper Tool Multi Language"],
                "correcta": 1
            },
            {
                "pregunta": "¿Cuál de estos lenguajes se usa principalmente para estilos en páginas web?",
                "opciones": ["Python", "Java", "CSS", "SQL"],
                "correcta": 2
            },
            {
                "pregunta": "En Python, ¿qué símbolo se usa normalmente para comentar una línea?",
                "opciones": ["//", "/*", "#", "--"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué hace una base de datos?",
                "opciones": ["Diseña imágenes", "Almacena y organiza información", "Compila programas", "Crea redes sociales"],
                "correcta": 1
            },
            {
                "pregunta": "¿Cuál de estos es un sistema operativo?",
                "opciones": ["Git", "Linux", "MySQL", "JavaScript"],
                "correcta": 1
            }
        ],
        "medio": [
            {
                "pregunta": "¿Qué comando de Git se utiliza para guardar cambios en el repositorio local?",
                "opciones": ["git push", "git commit", "git clone", "git branch"],
                "correcta": 1
            },
            {
                "pregunta": "En programación, ¿qué estructura se usa para repetir instrucciones?",
                "opciones": ["Condicional", "Variable", "Bucle", "Clase"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué significa SQL?",
                "opciones": ["Structured Query Language", "Simple Query Link", "System Question Language", "Sequential Quick Language"],
                "correcta": 0
            },
            {
                "pregunta": "¿Qué paradigma se basa en objetos y clases?",
                "opciones": ["Programación funcional", "Programación orientada a objetos", "Programación lógica", "Programación estructurada"],
                "correcta": 1
            },
            {
                "pregunta": "¿Qué protocolo se usa normalmente para navegar páginas web?",
                "opciones": ["FTP", "SMTP", "HTTP", "SSH"],
                "correcta": 2
            }
        ],
        "dificil": [
            {
                "pregunta": "¿Qué estructura de datos utiliza el principio FIFO?",
                "opciones": ["Pila", "Árbol", "Cola", "Grafo"],
                "correcta": 2
            },
            {
                "pregunta": "En una tabla hash bien implementada, ¿cuál es la complejidad temporal promedio de búsqueda?",
                "opciones": ["O(n²)", "O(log n)", "O(n)", "O(1)"],
                "correcta": 3
            },
            {
                "pregunta": "¿Qué hace el proceso de compilación?",
                "opciones": ["Ejecuta directamente el programa", "Convierte código fuente en código máquina o ejecutable", "Diseña interfaces gráficas", "Almacena datos en memoria RAM"],
                "correcta": 1
            },
            {
                "pregunta": "¿Cuál de estos patrones separa lógica, interfaz y control?",
                "opciones": ["Singleton", "Factory", "MVC", "Observer"],
                "correcta": 2
            },
            {
                "pregunta": "¿Qué comando SQL se usa para combinar filas de dos tablas relacionadas?",
                "opciones": ["MERGE", "JOIN", "CONNECT", "UNION ONLY"],
                "correcta": 1
            }
        ]
    }
}

# =====================================================
# CONFIGURACIÓN PRINCIPAL
# =====================================================

ventana = tk.Tk()
ventana.title("🚀 TRIVIA ARCADE")
ventana.geometry("1920x1080")
ventana.attributes("-fullscreen", True)
ventana.config(bg="#0F172A")

# =====================================================
# VARIABLES GLOBALES DE JUEGO
# =====================================================
menu = "principal"
num_jugadores = 1
jugador_actual = 0
puntajes = [0, 0]
preguntas_usadas = set()
tiempo_restante = 30
tiempo_partida_restante = 300
timer_id = None
ruleta_after_id = None
match_timer_id = None
pregunta_actual = None
dificultad_actual = ""
categoria_actual = ""
girando = False

CATEGORIA_MAP = {
    "Linux": "Linux",
    "Desarrollo Software": "Desarrollo",
    "Ciberseguridad": "Ciberseguridad",
    "Redes": "Redes",
    "Inteligencia Artificial": "IA"
}

# =====================================================
# FUNCIONES DEL MENÚ
# =====================================================

def cambiar_menu():
    global menu

    # =========================
    # PRINCIPAL -> REGLAS
    # =========================
    if menu == "principal":
        btn_jugar.pack_forget()
        btn_reglas.pack_forget()
        btn_salir.pack_forget()

        titulo.config(
            text="📜 REGLAS DEL JUEGO",
            fg="#00F0FF"
        )

        texto_info.config(
            text="Seleccione una regla para ver información."
        )

        btn_turnos.pack(pady=4)
        btn_puntajes.pack(pady=4)
        btn_respuestas.pack(pady=4)
        btn_tiempo.pack(pady=4)
        btn_finalizacion.pack(pady=4)
        btn_volver.pack(pady=15)

        texto_info.pack(
            pady=15,
            fill="both",
            expand=True
        )

        menu = "reglas"

    # =========================
    # REGLAS -> PRINCIPAL
    # =========================
    elif menu == "reglas":
        btn_turnos.pack_forget()
        btn_puntajes.pack_forget()
        btn_respuestas.pack_forget()
        btn_tiempo.pack_forget()
        btn_finalizacion.pack_forget()
        btn_volver.pack_forget()
        texto_info.pack_forget()

        titulo.config(
            text="⚡ MENÚ PRINCIPAL",
            fg="#FF007F"
        )

        btn_jugar.pack(pady=12)
        btn_reglas.pack(pady=12)
        btn_salir.pack(pady=12)

        menu = "principal"

# =====================================================
# FUNCIÓN JUGAR Y CONFIGURACIÓN DE PARTIDA
# =====================================================

def jugar():
    global menu
    # Ocultar menú principal
    btn_jugar.pack_forget()
    btn_reglas.pack_forget()
    btn_salir.pack_forget()

    titulo.config(
        text="👥 SELECCIONAR JUGADORES",
        fg="#00F0FF"
    )

    # Mostrar opciones de jugadores
    btn_1_jugador.pack(pady=15)
    btn_2_jugadores.pack(pady=15)
    btn_volver_seleccion.pack(pady=15)

    menu = "seleccion_jugadores" # programa sabe en que pantalla esta

def volver_desde_seleccion(): #  presiona vuelve menu principal
    btn_1_jugador.pack_forget()
    btn_2_jugadores.pack_forget()
    btn_volver_seleccion.pack_forget()
    volver_al_menu_principal() # llama a otra funcion

def iniciar_juego_con(cant): # recibe parametro 
    global num_jugadores
    num_jugadores = cant # guarda cantidad
    iniciar_partida()

def iniciar_partida(): # funcion importante
    global menu, puntajes, jugador_actual, preguntas_usadas, tiempo_partida_restante
    
    # Ocultar selección de jugadores
    btn_1_jugador.pack_forget()
    btn_2_jugadores.pack_forget()
    btn_volver_seleccion.pack_forget()

    # Reiniciar estado de la partida
    puntajes = [0, 0]
    jugador_actual = 0 # jugador 1 empieza
    preguntas_usadas = set() # saca registro de preguntas usadas
    
    # Asignar tiempo restante: 5 min (1 jug) o 10 min (2 jug)
    if num_jugadores == 1:
        tiempo_partida_restante = 300 # 5 minutos
    else:
        tiempo_partida_restante = 600 # 10 minutos

    titulo.config(
        text="🎡 RULETAGAME",
        fg="#39FF14"
    )

    # Mostrar marcador, tiempo y turno
    actualizar_marcador() 
    label_marcador.pack(pady=2) # muestra
    
    mins = tiempo_partida_restante // 60 # covierte sg min
    label_tiempo_partida.config(text=f"⏱️ Tiempo de Partida: {mins:02d}:00") # inicial
    label_tiempo_partida.pack(pady=2) # reloj
    
    label_turno.pack(pady=2)

    # Mostrar canvas de ruleta
    canvas.pack(pady=5)

    # Mostrar botón de girar (centrado dinámicamente debajo del canvas sin superponerse)
    boton_girar.pack(pady=10)

    menu = "ruleta" # en que pantalla estamos
    
    # Comenzar temporizador general de la partida
    iniciar_timer_partida()

def detener_todos_los_timers():
    global timer_id, ruleta_after_id, match_timer_id
    if timer_id: # verifica si existe
        ventana.after_cancel(timer_id) # cancela
        timer_id = None # lo vacia 
    if ruleta_after_id:
        ventana.after_cancel(ruleta_after_id)
        ruleta_after_id = None
    if match_timer_id:
        ventana.after_cancel(match_timer_id)
        match_timer_id = None

def volver_al_menu_principal():
    global menu
    
    # Cancelar todos los timers activos
    detener_todos_los_timers()

    # Ocultar todo lo relacionado al juego
    canvas.pack_forget()
    boton_girar.pack_forget()
    label_marcador.pack_forget()
    label_tiempo_partida.pack_forget()
    label_turno.pack_forget()
    panel_dificultad.pack_forget()
    panel_pregunta.pack_forget()
    panel_victoria.pack_forget()
    btn_1_jugador.pack_forget()
    btn_2_jugadores.pack_forget()
    btn_volver_seleccion.pack_forget()

    
    titulo.config(
        text="⚡ MENÚ PRINCIPAL",
        fg="#FF007F"
    )

    btn_jugar.pack(pady=12)
    btn_reglas.pack(pady=12)
    btn_salir.pack(pady=12)

    menu = "principal"

# =====================================================
# TEMPORIZADOR GENERAL DE PARTIDA
# =====================================================

def iniciar_timer_partida(): # total
    global tiempo_partida_restante, match_timer_id
    if menu in ["ruleta", "seleccion_dificultad", "pregunta"]: # cuando se juega
        if tiempo_partida_restante > 0:
            tiempo_partida_restante -= 1
            mins = tiempo_partida_restante // 60 # calcula
            secs = tiempo_partida_restante % 60 # calcula
            label_tiempo_partida.config(text=f"⏱️ Tiempo de Partida: {mins:02d}:{secs:02d}") # actualiza reloj
            match_timer_id = ventana.after(1000, iniciar_timer_partida) # funciona correcto el reloj
        else:
            finalizar_por_tiempo() # termina partida

def finalizar_por_tiempo():
    global menu
    
    # Detener todos los procesos
    detener_todos_los_timers()
    
    # Ocultar todos los widgets del juego activo
    canvas.pack_forget()
    boton_girar.pack_forget()
    label_marcador.pack_forget()
    label_tiempo_partida.pack_forget()
    label_turno.pack_forget()
    panel_pregunta.pack_forget()
    panel_dificultad.pack_forget()
    
    if num_jugadores == 1: # verifica
        # Para 1 jugador, agotar el tiempo NO es victoria
        titulo.config(
            text="⌛ TIEMPO AGOTADO ⌛",
            fg="#FF007F"
        )
        lbl_victoria_titulo.config(text="😢 FIN DE PARTIDA 😢", fg="#FF007F")
        texto_resultado = f"Se ha terminado el tiempo de la partida.\nTu puntaje final es de {puntajes[0]} / 200 puntos.\n¡Inténtalo de nuevo para llegar a los 200!"
        
        # Sonido de derrota
        try: # intenta reproducir
            winsound.Beep(293, 300)
            winsound.Beep(220, 500)
        except Exception:
            pass
    else:
        # Para 2 jugadores, es una victoria por puntos de quien tenga la puntuación más alta
        titulo.config(
            text="🏆 FIN DEL JUEGO 🏆",
            fg="#FACC15"
        )
        
        if puntajes[0] > puntajes[1]:
            lbl_victoria_titulo.config(text="🎉 ¡VICTORIA! 🎉", fg="#FACC15")
            texto_resultado = f"🏆 ¡El tiempo ha terminado!\n¡Gana el Jugador 1 con {puntajes[0]} pts frente a {puntajes[1]} pts del Jugador 2!"
            # Sonido de victoria
            try:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 300)
            except Exception:
                pass
        elif puntajes[1] > puntajes[0]:
            lbl_victoria_titulo.config(text="🎉 ¡VICTORIA! 🎉", fg="#FACC15")
            texto_resultado = f"🏆 ¡El tiempo ha terminado!\n¡Gana el Jugador 2 con {puntajes[1]} pts frente a {puntajes[0]} pts del Jugador 1!"
            # Sonido de victoria
            try:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 300)
            except Exception:
                pass
        else:
            lbl_victoria_titulo.config(text="🤝 EMPATE 🤝", fg="#00F0FF")
            texto_resultado = f"¡El tiempo ha terminado!\nAmbos jugadores empataron con {puntajes[0]} puntos."
            # Sonido de empate
            try:
                winsound.Beep(392, 200)
                winsound.Beep(392, 200)
            except Exception:
                pass
            
    panel_victoria.pack(pady=50, fill="both", expand=True)
    lbl_victoria_texto.config(text=texto_resultado) # muestra mensaje
    menu = "victoria" # programa esta en pantalla final

# =====================================================
# ACTUALIZAR MARCADOR
# =====================================================

def actualizar_marcador(): # puntos y turno
    if num_jugadores == 1:
        label_marcador.config(text=f"Puntaje: {puntajes[0]} / 200", fg="#00F0FF")
        label_turno.config(text="¡Consigue 200 puntos para ganar!", fg="#E2E8F0") # muestra instruccion
    else:
        label_marcador.config(
            text=f"Jugador 1: {puntajes[0]} pts  |  Jugador 2: {puntajes[1]} pts",
            fg="#00F0FF"
        )
        color_turno = "#39FF14"  if jugador_actual == 0 else "#FF007F"
        label_turno.config(text=f"👉 Turno de: Jugador {jugador_actual + 1}", fg=color_turno)

# =====================================================
# SALIR 
# =====================================================

def salir_con_confirmacion(): # cerrar programa
    respuesta = messagebox.askyesno(
        title="Salir",
        message="¿Seguro que deseas salir?"
    )
    if respuesta:
        ventana.destroy() # cierra

# Asocia
ventana.bind("<Escape>", lambda e: salir_con_confirmacion())

# =====================================================
# FUNCIONES REGLAS
# =====================================================

def mostrar_turnos():
    texto_info.config(
        text="""
🔄 REGLA: TURNOS

Cada jugador:
1. Gira la ruleta.
2. Responde preguntas.
3. Gana puntos.
"""
    )

def mostrar_puntajes():
    texto_info.config(
        text="""
🏆 SISTEMA DE PUNTAJES

Fácil  → +10
Media  → +20
Difícil → +30
"""
    )

def mostrar_respuestas():
    texto_info.config(
        text="""
✅ RESPUESTA CORRECTA
• Ganas puntos

❌ RESPUESTA INCORRECTA
• Pierdes turno
"""
    )

def mostrar_tiempo():
    texto_info.config(
        text="""
⏳ TIEMPO

30 segundos por pregunta.
"""
    )

def mostrar_finalizacion():
    texto_info.config(
        text="""
🏁 FINAL

El juego termina:
• al llegar a 200 puntos
• o cuando termina el tiempo
"""
    )

# =====================================================
# SELECCIÓN Y PROCESAMIENTO DE PREGUNTAS
# =====================================================

def obtener_pregunta_no_repetida(cat_id, dif):
    global preguntas_usadas
    preguntas_disponibles = BANCO_PREGUNTAS[cat_id][dif]
    indices_disponibles = [i for i in range(len(preguntas_disponibles)) if (cat_id, dif, i) not in preguntas_usadas]
    
    if not indices_disponibles:
        # Si se usaron todas, vaciamos el registro de esta categoría/dificultad
        preguntas_usadas = {x for x in preguntas_usadas if x[0] != cat_id or x[1] != dif}
        indices_disponibles = list(range(len(preguntas_disponibles)))
        
    idx = random.choice(indices_disponibles)
    preguntas_usadas.add((cat_id, dif, idx))
    return preguntas_disponibles[idx]

def mostrar_seleccion_dificultad(categoria):
    global categoria_actual, menu
    categoria_actual = categoria
    
    # Ocultar ruleta y marcador
    canvas.pack_forget()
    boton_girar.pack_forget()
    label_marcador.pack_forget()
    label_turno.pack_forget()
    
    # Mostrar panel de dificultades
    panel_dificultad.pack(pady=40, fill="both", expand=True)
    lbl_dif_cat.config(text=f"📁 CATEGORÍA: {categoria.upper()}")
    
    menu = "seleccion_dificultad"

def iniciar_pregunta_con_dificultad(dificultad):
    global dificultad_actual, pregunta_actual, tiempo_restante, timer_id, menu
    
    # Ocultar panel de dificultad
    panel_dificultad.pack_forget()
    
    dificultad_actual = dificultad
    cat_id = CATEGORIA_MAP.get(categoria_actual, "Redes")
    
    # Cargar pregunta correspondiente
    pregunta_actual = obtener_pregunta_no_repetida(cat_id, dificultad_actual)
    
    # Mostrar panel de preguntas
    panel_pregunta.pack(pady=10, fill="both", expand=True)
    
    # Configurar cabecera e indicador de turno activo
    if num_jugadores == 1:
        lbl_turno_pregunta.config(text="👤 JUGADOR ÚNICO", fg="#38BDF8")
    else:
        color_turno = "#39FF14" if jugador_actual == 0 else "#FF007F"
        lbl_turno_pregunta.config(text=f"👉 TURNO DE: JUGADOR {jugador_actual + 1}", fg=color_turno)

    dif_texto = dificultad_actual.upper()
    dif_color = "#39FF14" if dificultad_actual == "facil" else ("#FACC15" if dificultad_actual == "medio" else "#FF007F")
    
    lbl_cat_dif.config(text=f"📁 CATEGORÍA: {categoria_actual.upper()}   |   🔥 DIFICULTAD: {dif_texto}", fg=dif_color)
    lbl_pregunta_texto.config(text=pregunta_actual["pregunta"])
    
    # Habilitar y actualizar botones de opciones
    opciones = pregunta_actual["opciones"]
    for i, boton in enumerate(botones_opciones):
        boton.config(
            text=opciones[i],
            bg="#1E293B",
            fg="#E2E8F0",
            state="normal",
            relief="flat",
            activebackground="#334155",
            activeforeground="#F8FAFC"
        )
    
    # Iniciar cuenta regresiva de la pregunta (30 segundos)
    tiempo_restante = 30
    lbl_timer.config(text=f"⏳ {tiempo_restante}", fg="#00F0FF")
    
    btn_continuar_pregunta.pack_forget()
    iniciar_cuenta_regresiva()
    
    menu = "pregunta"

def iniciar_cuenta_regresiva():
    global tiempo_restante, timer_id
    if tiempo_restante > 0:
        tiempo_restante -= 1
        color = "#00F0FF" if tiempo_restante > 15 else ("#FACC15" if tiempo_restante > 5 else "#FF007F")
        lbl_timer.config(text=f"⏳ {tiempo_restante}", fg=color)
        timer_id = ventana.after(1000, iniciar_cuenta_regresiva)
    else:
        procesar_respuesta(-1)

def procesar_respuesta(opcion_seleccionada):
    global timer_id, puntajes, jugador_actual
    
    if timer_id:
        ventana.after_cancel(timer_id)
        timer_id = None
        
    for boton in botones_opciones:
        boton.config(state="disabled")
        
    correcta = pregunta_actual["correcta"]
    
    if opcion_seleccionada == correcta:
        try:
            winsound.Beep(880, 150)
            winsound.Beep(1109, 150)
            winsound.Beep(1318, 300)
        except Exception:
            pass
            
        puntos_ganados = 10 if dificultad_actual == "facil" else (20 if dificultad_actual == "medio" else 30)
        puntajes[jugador_actual] += puntos_ganados
        
        botones_opciones[correcta].config(bg="#22C55E", fg="white", disabledforeground="white")
        lbl_resultado.config(text=f"¡CORRECTO! 🎉 +{puntos_ganados} puntos", fg="#39FF14")
    else:
        try:
            winsound.Beep(330, 200)
            winsound.Beep(262, 300)
        except Exception:
            pass
            
        botones_opciones[correcta].config(bg="#22C55E", fg="white", disabledforeground="white")
        
        if opcion_seleccionada != -1:
            botones_opciones[opcion_seleccionada].config(bg="#EF4444", fg="white", disabledforeground="white")
            lbl_resultado.config(text="¡INCORRECTO! ❌ Pierdes el turno", fg="#FF007F")
        else:
            lbl_resultado.config(text="¡TIEMPO AGOTADO! ⏳ Pierdes el turno", fg="#FACC15")
            
    # Mostrar el botón continuar
    btn_continuar_pregunta.pack(pady=10)

def confirmar_continuar():
    global jugador_actual, menu, ruleta_after_id
    
    # Limpiar pantalla de preguntas
    panel_pregunta.pack_forget()
    lbl_resultado.config(text="")
    
    # Comprobar si hay victoria por puntaje de 200 puntos
    if puntajes[jugador_actual] >= 200:
        mostrar_victoria(jugador_actual)
        return
        
    # Cambiar turno si hay 2 jugadores
    if num_jugadores == 2:
        jugador_actual = 1 - jugador_actual
        
    # Volver a la ruleta
    titulo.config(
        text="🎡 RULETAGAME",
        fg="#39FF14"
    )
    
    actualizar_marcador()
    label_marcador.pack(pady=2)
    label_tiempo_partida.pack(pady=2)
    label_turno.pack(pady=2)
    
    canvas.pack(pady=5)
    boton_girar.config(state="normal")
    boton_girar.pack(pady=10)
    menu = "ruleta"
    
    # Iniciar automáticamente el giro de la ruleta para la siguiente ronda tras 1 segundo
    ruleta_after_id = ventana.after(1000, girar)

# =====================================================
# PANTALLA DE VICTORIA / RESOLUCIÓN (SE LLEGA A 200 PTS)
# =====================================================

def mostrar_victoria(ganador_idx):
    global menu
    
    detener_todos_los_timers()
    
    canvas.pack_forget()
    boton_girar.pack_forget()
    label_marcador.pack_forget()
    label_tiempo_partida.pack_forget()
    label_turno.pack_forget()
    panel_pregunta.pack_forget()
    
    titulo.config(
        text="🏆 FIN DEL JUEGO 🏆",
        fg="#FACC15"
    )
    
    lbl_victoria_titulo.config(text="🎉 ¡VICTORIA! 🎉", fg="#FACC15")
    panel_victoria.pack(pady=50, fill="both", expand=True)
    
    if num_jugadores == 1:
        texto_victoria = "¡Felicidades! 🎉\nHas alcanzado los 200 puntos y completado la Trivia con éxito."
    else:
        texto_victoria = f"🏆 ¡Felicidades Jugador {ganador_idx + 1}! 🏆\nHas ganado la partida al alcanzar los {puntajes[ganador_idx]} puntos."
        
    lbl_victoria_texto.config(text=texto_victoria)
    
    # Sonido triunfal
    try:
        winsound.Beep(523, 150)
        winsound.Beep(659, 150)
        winsound.Beep(784, 150)
        winsound.Beep(1047, 150)
        winsound.Beep(1318, 150)
        winsound.Beep(1568, 400)
    except Exception:
        pass
        
    menu = "victoria"

def volver_al_menu_desde_victoria():
    panel_victoria.pack_forget()
    volver_al_menu_principal()

# =====================================================
# TÍTULO PRINCIPAL
# =====================================================

titulo = tk.Label(
    ventana,
    text="⚡ MENÚ PRINCIPAL",
    font=("Segoe UI Black", 24, "italic"),
    fg="#FF007F",
    bg="#0F172A"
)
titulo.pack(pady=25)

# =====================================================
# ÁREA DE TEXTO (REGLAS)
# =====================================================

texto_info = tk.Label(
    ventana,
    text="¿Listo para jugar?",
    font=("Consolas", 11, "bold"),
    fg="#39FF14",
    bg="#1E293B",
    width=55,
    height=7,
    justify="left",
    anchor="nw",
    highlightthickness=2,
    highlightbackground="#38BDF8",
    padx=20,
    pady=20
)

# =====================================================
# ESTILOS DE BOTONES
# =====================================================

estilo_botones_menu = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": "#38BDF8",
    "fg": "#0F172A",
    "relief": "flat",
    "activebackground": "#0EA5E9",
    "activeforeground": "#FFFFFF",
    "width": 28,
    "bd": 0,
    "cursor": "hand2"
}

estilo_botones_reglas = {
    "font": ("Segoe UI", 10, "bold"),
    "bg": "#1E293B",
    "fg": "#94A3B8",
    "relief": "flat",
    "activebackground": "#334155",
    "activeforeground": "#F8FAFC",
    "width": 32,
    "bd": 0,
    "cursor": "hand2"
}

# =====================================================
# BOTONES MENÚ PRINCIPAL
# =====================================================

btn_jugar = tk.Button(
    ventana,
    text="🎮 EMPEZAR PARTIDA",
    command=jugar,
    **estilo_botones_menu
)
btn_jugar.config(
    bg="#39FF14",
    activebackground="#22C55E"
)

btn_reglas = tk.Button(
    ventana,
    text="📜 REGLAS",
    command=cambiar_menu,
    **estilo_botones_menu
)

btn_salir = tk.Button(
    ventana,
    text="❌ SALIR",
    command=salir_con_confirmacion,
    **estilo_botones_menu
)
btn_salir.config(
    bg="#FF007F",
    fg="white",
    activebackground="#DF123E"
)

# =====================================================
# BOTONES SELECCIÓN DE JUGADORES
# =====================================================

btn_1_jugador = tk.Button(
    ventana,
    text="👤 1 JUGADOR",
    command=lambda: iniciar_juego_con(1),
    **estilo_botones_menu
)

btn_2_jugadores = tk.Button(
    ventana,
    text="👥 2 JUGADORES",
    command=lambda: iniciar_juego_con(2),
    **estilo_botones_menu
)

btn_volver_seleccion = tk.Button(
    ventana,
    text="⬅ VOLVER AL MENÚ",
    command=volver_desde_seleccion,
    font=("Segoe UI", 10, "bold"),
    bg="#FF007F",
    fg="white",
    relief="flat",
    activebackground="#DF123E",
    activeforeground="white",
    width=20
)

# =====================================================
# BOTONES SECCIÓN REGLAS
# =====================================================

btn_turnos = tk.Button(
    ventana,
    text="🔄 TURNOS",
    command=mostrar_turnos,
    **estilo_botones_reglas
)

btn_puntajes = tk.Button(
    ventana,
    text="🏆 PUNTAJES",
    command=mostrar_puntajes,
    **estilo_botones_reglas
)

btn_respuestas = tk.Button(
    ventana,
    text="✅ RESPUESTAS",
    command=mostrar_respuestas,
    **estilo_botones_reglas
)

btn_tiempo = tk.Button(
    ventana,
    text="⏳ TIEMPO",
    command=mostrar_tiempo,
    **estilo_botones_reglas
)

btn_finalizacion = tk.Button(
    ventana,
    text="🏁 FINALIZACIÓN",
    command=mostrar_finalizacion,
    **estilo_botones_reglas
)

btn_volver = tk.Button(
    ventana,
    text="⬅ VOLVER",
    command=cambiar_menu,
    bg="#00F0FF",
    fg="#0F172A",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=20
)

# =====================================================
# MARCADORES DE JUEGO (LABELS)
# =====================================================

label_marcador = tk.Label(
    ventana,
    text="",
    font=("Segoe UI", 16, "bold"),
    fg="#00F0FF",
    bg="#0F172A"
)

label_tiempo_partida = tk.Label(
    ventana,
    text="",
    font=("Segoe UI", 14, "bold"),
    fg="#FACC15",
    bg="#0F172A"
)

label_turno = tk.Label(
    ventana,
    text="",
    font=("Segoe UI", 14, "bold"),
    fg="#39FF14",
    bg="#0F172A"
)

# =====================================================
# CANVAS RULETA (OPTIMIZADO PARA PANTALLAS DE CUALQUIER TAMAÑO)
# =====================================================

canvas = tk.Canvas(
    ventana,
    width=800,
    height=450,
    bg="#0F172A",
    highlightbackground="#0F172A",
    bd=0
)

# Círculo centrado perfectamente en el canvas de 800x450:
# Diámetro de 400 píxeles.
ruleta = canvas.create_oval(
    200,
    25,
    600,
    425,
    fill="black",
    outline="#0F172A",
    width=5
)

# Texto en el centro exacto (400, 225)
texto_ruleta = canvas.create_text(
    400,
    225,
    text="GIRAR",
    font=("Segoe UI Black", 28, "italic"),
    fill="white"
)

# =====================================================
# LISTA DE CATEGORÍAS
# =====================================================

categorias = [
    "Linux",
    "Desarrollo Software",
    "Ciberseguridad",
    "Redes",
    "Inteligencia Artificial"
]

# =====================================================
# FUNCIÓN GIRAR RULETA
# =====================================================

def girar():
    global girando

    if girando:
        return

    # Deshabilitar el botón de girar durante el giro
    boton_girar.config(state="disabled")
    girando = True
    velocidad = 50

    for i in range(30):
        premio = random.choice(categorias)
        canvas.itemconfig(texto_ruleta, text=premio)

        color = random.choice([
            "#FF007F", # Rosa Neón
            "#00F0FF", # Cian Neón
            "#39FF14", # Verde Neón
            "#FACC15", # Amarillo Neón
            "#8B5CF6", # Violeta
            "#F97316"  # Naranja
        ])

        canvas.itemconfig(ruleta, fill=color)

        frecuencia = max(37, int(1000 - velocidad * 2))
        try:
            winsound.Beep(frecuencia, 30)
        except Exception:
            pass

        ventana.update()
        time.sleep(velocidad / 1000)
        velocidad += 10

    # Sonido de victoria al detenerse la ruleta
    try:
        winsound.Beep(523, 100)  # Do
        winsound.Beep(659, 100)  # Mi
        winsound.Beep(784, 100)  # Sol
        winsound.Beep(1047, 250) # Do (Octava alta)
    except Exception:
        pass

    girando = False
    # NO re-habilitar aquí: el botón se reactiva solo cuando vuelve la ruleta tras responder
    
    # Obtener el premio/categoría en la que se detuvo
    premio_final = canvas.itemcget(texto_ruleta, "text")
    
    # Esperar un momento y mostrar la selección de dificultad
    global ruleta_after_id
    ruleta_after_id = ventana.after(1000, lambda: mostrar_seleccion_dificultad(premio_final))

# =====================================================
# BOTÓN GIRAR
# =====================================================

boton_girar = tk.Button(
    ventana,
    text="🎡 GIRAR RULETA",
    font=("Segoe UI", 20, "bold"),
    bg="#39FF14",
    fg="black",
    command=girar,
    relief="flat",
    cursor="hand2"
)

# =====================================================
# PANEL DE SELECCIÓN DE DIFICULTAD
# =====================================================

panel_dificultad = tk.Frame(
    ventana,
    bg="#0F172A"
)

lbl_dif_cat = tk.Label(
    panel_dificultad,
    text="",
    font=("Segoe UI Black", 24, "italic"),
    fg="#00F0FF",
    bg="#0F172A"
)
lbl_dif_cat.pack(pady=15)

lbl_dif_instruccion = tk.Label(
    panel_dificultad,
    text="Selecciona la dificultad de la pregunta:",
    font=("Segoe UI", 16, "bold"),
    fg="#FFFFFF",
    bg="#0F172A"
)
lbl_dif_instruccion.pack(pady=10)

frame_dif_botones = tk.Frame(
    panel_dificultad,
    bg="#0F172A"
)
frame_dif_botones.pack(pady=10)

btn_dif_facil = tk.Button(
    frame_dif_botones,
    text="🟢 FÁCIL (+10 pts)",
    font=("Segoe UI", 12, "bold"),
    bg="#1E293B",
    fg="#39FF14",
    relief="flat",
    activebackground="#334155",
    activeforeground="#39FF14",
    width=30,
    height=1,
    bd=0,
    cursor="hand2",
    command=lambda: iniciar_pregunta_con_dificultad("facil")
)
btn_dif_facil.pack(pady=6)

btn_dif_medio = tk.Button(
    frame_dif_botones,
    text="🟡 MEDIO (+20 pts)",
    font=("Segoe UI", 12, "bold"),
    bg="#1E293B",
    fg="#FACC15",
    relief="flat",
    activebackground="#334155",
    activeforeground="#FACC15",
    width=30,
    height=1,
    bd=0,
    cursor="hand2",
    command=lambda: iniciar_pregunta_con_dificultad("medio")
)
btn_dif_medio.pack(pady=6)

btn_dif_dificil = tk.Button(
    frame_dif_botones,
    text="🔴 DIFÍCIL (+30 pts)",
    font=("Segoe UI", 12, "bold"),
    bg="#1E293B",
    fg="#FF007F",
    relief="flat",
    activebackground="#334155",
    activeforeground="#FF007F",
    width=30,
    height=1,
    bd=0,
    cursor="hand2",
    command=lambda: iniciar_pregunta_con_dificultad("dificil")
)
btn_dif_dificil.pack(pady=6)

# =====================================================
# PANEL DE PREGUNTA (CUSTOM FRAME OPTIMIZADO)
# =====================================================

panel_pregunta = tk.Frame(
    ventana,
    bg="#0F172A"
)

# Indicador de turno activo en la pregunta
lbl_turno_pregunta = tk.Label(
    panel_pregunta,
    text="",
    font=("Segoe UI", 14, "bold"),
    bg="#0F172A"
)
lbl_turno_pregunta.pack(pady=5)

lbl_cat_dif = tk.Label(
    panel_pregunta,
    text="",
    font=("Segoe UI", 12, "bold"),
    fg="#00F0FF",
    bg="#0F172A"
)
lbl_cat_dif.pack(pady=3)

lbl_timer = tk.Label(
    panel_pregunta,
    text="",
    font=("Consolas", 24, "bold"),
    fg="#00F0FF",
    bg="#0F172A"
)
lbl_timer.pack(pady=2)

lbl_pregunta_texto = tk.Label(
    panel_pregunta,
    text="",
    font=("Segoe UI", 15, "bold"),
    fg="#FFFFFF",
    bg="#1E293B",
    width=65,
    wraplength=700,
    justify="center",
    highlightthickness=2,
    highlightbackground="#38BDF8",
    padx=20,
    pady=15
)
lbl_pregunta_texto.pack(pady=10)

frame_opciones = tk.Frame(
    panel_pregunta,
    bg="#0F172A"
)
frame_opciones.pack(pady=5)

botones_opciones = []
for i in range(4):
    btn = tk.Button(
        frame_opciones,
        text="",
        font=("Segoe UI", 11, "bold"),
        bg="#1E293B",
        fg="#E2E8F0",
        relief="flat",
        activebackground="#334155",
        activeforeground="#F8FAFC",
        width=55,
        bd=0,
        cursor="hand2",
        wraplength=480,  # wrap automático de texto en 480 píxeles
        command=lambda idx=i: procesar_respuesta(idx)
    )
    btn.pack(pady=4)
    botones_opciones.append(btn)

lbl_resultado = tk.Label(
    panel_pregunta,
    text="",
    font=("Segoe UI", 14, "bold"),
    bg="#0F172A"
)
lbl_resultado.pack(pady=5)

btn_continuar_pregunta = tk.Button(
    panel_pregunta,
    text="CONTINUAR ➔",
    font=("Segoe UI", 12, "bold"),
    bg="#39FF14",
    fg="#0F172A",
    relief="flat",
    width=20,
    height=1,
    bd=0,
    cursor="hand2",
    command=confirmar_continuar
)

# =====================================================
# PANEL DE VICTORIA / RESOLUCIÓN (SE LLEGA A 200 PTS)
# =====================================================

panel_victoria = tk.Frame(
    ventana,
    bg="#0F172A"
)

lbl_victoria_titulo = tk.Label(
    panel_victoria,
    text="",
    font=("Segoe UI Black", 36, "italic"),
    fg="#FACC15",
    bg="#0F172A"
)
lbl_victoria_titulo.pack(pady=20)

lbl_victoria_texto = tk.Label(
    panel_victoria,
    text="",
    font=("Segoe UI", 18, "bold"),
    fg="#FFFFFF",
    bg="#1E293B",
    width=50,
    height=6,
    justify="center",
    highlightthickness=2,
    highlightbackground="#FACC15",
    padx=20,
    pady=20
)
lbl_victoria_texto.pack(pady=20)

btn_volver_menu = tk.Button(
    panel_victoria,
    text="🏠 VOLVER AL MENÚ",
    font=("Segoe UI", 12, "bold"),
    bg="#00F0FF",
    fg="#0F172A",
    relief="flat",
    width=25,
    height=2,
    bd=0,
    cursor="hand2",
    command=volver_al_menu_desde_victoria
)
btn_volver_menu.pack(pady=20)

# =====================================================
# INICIO
# =====================================================

btn_jugar.pack(pady=12)
btn_reglas.pack(pady=12)
btn_salir.pack(pady=12)

ventana.mainloop()