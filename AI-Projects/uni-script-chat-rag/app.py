import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq



st.set_page_config(page_title="Uni-Skript Chatbot", page_icon="📚")

st.title("📚 Chatte mit deinem Skript")
api_key = st.sidebar.text_input("🔑 Dein Groq API Key:", type="password")
if not api_key:
    st.sidebar.warning("Bitte gib deinen API Key ein, um zu chatten.")
st.write("Willkommen! Bald kannst du hier PDFs hochladen und befragen.")



# --- NEUER CODE BLOCK ---
st.divider() # Zieht eine schöne Trennlinie
st.subheader("📄 Schritt 1: Dokument hochladen")

# Der Streamlit File-Uploader
uploaded_file = st.file_uploader("Lade dein Uni-Skript hoch (nur PDF)", type="pdf")

if uploaded_file is not None:
    st.success(f"Erfolg! Datei '{uploaded_file.name}' wurde hochgeladen.")
    
    # 1. Datei temporär auf der Festplatte speichern
    with open("temp_skript.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
        
    # 2. PDF einlesen (LangChain PyPDFLoader)
    st.info("Lese PDF ein...")
    loader = PyPDFLoader("temp_skript.pdf")
    pages = loader.load()
    st.write(f"📄 Das PDF hat **{len(pages)}** Seiten.")
    
    # 3. Text in Chunks zerschneiden
    st.info("Zerschneide Text in Chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(pages)
    
    st.success(f"✂️ Das Skript wurde in **{len(chunks)}** Text-Blöcke zerschnitten!")
    
    st.info("🧠 Verwandle Text in Vektoren (Das kann kurz dauern)...")
    
    # 4. Wir laden ein kostenloses, lokales Embedding-Modell
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 5. Wir erstellen die Vektor-Datenbank
    vector_store = Chroma.from_documents(chunks, embeddings)
    
    st.success("✅ Vektor-Datenbank erfolgreich erstellt! Das Skript ist jetzt 'wissend'.")

    st.divider()
    st.subheader("💬 Schritt 2: Frag dein Skript")

    # 1. Chat-Gedächtnis anlegen, falls es noch nicht existiert
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 2. Alten Chat-Verlauf auf dem Bildschirm anzeigen
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 3. Das Eingabefeld für den User
    if prompt := st.chat_input("Stelle eine Frage zu deinem Skript..."):
        
        # Die Frage des Users anzeigen und im Gedächtnis speichern
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

       # --- ECHTE RAG LOGIK START ---
        if not api_key:
            antwort = "Bitte gib zuerst links deinen Groq API Key ein!"
        else:
            try:
                # 1. RETRIEVAL (Suchen): Wir suchen die 3 passendsten Text-Blöcke aus der Datenbank
                st.session_state.messages.append({"role": "assistant", "content": "Suche im Skript..."})
                gefundene_chunks = vector_store.similarity_search(prompt, k=3)
                
                # Wir kleben die gefundenen Text-Blöcke zu einem großen Kontext-Text zusammen
                kontext = "\n\n".join([doc.page_content for doc in gefundene_chunks])
                
                # 2. PROMPT (Anweisung): Wir bauen den geheimen Befehl für das LLM
                system_prompt = f"""Du bist ein brillanter Tutor für Studenten. 
                Beantworte die Frage NUR basierend auf dem folgenden Skript-Kontext. 
                Wenn die Antwort nicht im Kontext steht, sag: 'Das steht nicht im Skript.'
                
                KONTEXT:
                {kontext}
                """
                
                # 3. GENERATION (Antworten): Wir rufen das Llama-3 Modell über Groq auf
                llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama-3.1-8b-instant")
                
                # Wir schicken den Befehl und die Frage des Users an die KI
                messages_for_llm = [
                    ("system", system_prompt),
                    ("human", prompt)
                ]
                
                ai_response = llm.invoke(messages_for_llm)
                antwort = ai_response.content
                
                # Entferne die "Suche im Skript..." Lade-Nachricht wieder
                st.session_state.messages.pop() 
                
            except Exception as e:
                antwort = f"Es gab einen Fehler: {e}"
                st.session_state.messages.pop()
        # --- ECHTE RAG LOGIK ENDE ---


        # Die Antwort der KI anzeigen und speichern
        with st.chat_message("assistant"):
            st.markdown(antwort)
        st.session_state.messages.append({"role": "assistant", "content": antwort})