import streamlit as st

# Streamlit app
st.title("Verhaaltje voor het slapen gaan")

contact_form = """
<form action="https://formsubmit.co/test.automation.1992.sm@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <label for="name">Wat is de naam van het hoofdpersonage?</label><br>
     <input type="text" name="name" placeholder="ex. Emma, Lily, ..." required>
     <label for="characteristics">Wat zijn specifieke kenmerken van het hoofdpersonage? Denk aan haarkleur, geslacht, leeftijd, favoriete kledij, ...</label><br>
     <input type="text" name="characteristics" placeholder="ex. 3-jarig blond meisje dat graag een roze jurk draagt." required>
     <label for="elements">Welke elementen moeten er zeker voorkomen in het verhaal? Denk aan een broertje/zusje, huisdier, een specifieke locatie of gebeurtenis, ...</label><br>
     <input type="text" name="characteristics" placeholder="ex. Flappy haar bruin hondje waarmee ze vaak in de tuin speelt." required>
     <label for="language">In welke taal zou je het verhaaltje graag lezen?:</label><br>
     <input type="text" name="language" placeholder="Nederlands" required>
     <label for="email">Naar welk email adres moeten we het verhaal opsturen?:</label><br>
     <input type="email" name="email" placeholder="email@email.com" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./style/style.css")



 