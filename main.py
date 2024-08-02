import streamlit as st

# Streamlit app
st.title("Verhaaltje voor het slapen gaan")

contact_form = """
<form action="https://api.web3forms.com/submit" method="POST">
	<!-- Replace with your Access Key -->
	<input type="hidden" name="access_key" value="69c64411-1307-4e08-b9cd-fdf76f46d456">
	<!-- Form Inputs. Each input must have a name="" attribute -->
	<label for="Name of main character">Wat is de naam van het hoofdpersonage?</label><br>
	<input type="text" name="Name of main character" placeholder="ex. Emma, Lily, ..." required>
	<label for="Characteristics of main character">Wat zijn specifieke kenmerken van het hoofdpersonage? Denk aan haarkleur, geslacht, leeftijd, favoriete kledij, ...</label><br>
	<input type="text" name="Characteristics of main character" placeholder="ex. 3-jarig blond meisje dat graag een roze jurk draagt." required>
	<label for="Elements of the story">Welke elementen moeten er zeker voorkomen in het verhaal? Denk aan een broertje/zusje, huisdier, een specifieke locatie of gebeurtenis, ...</label><br>
	<input type="text" name="Elements of the story" placeholder="ex. Flappy haar bruin hondje waarmee ze vaak in de tuin speelt." required>
	<label for="language">In welke taal zou je het verhaaltje graag lezen?:</label><br>
	<input type="text" name="language" placeholder="Nederlands" required>
	<label for="email">Naar welk email adres moeten we het verhaal opsturen?:</label><br>
	<input type="email" name="email" placeholder="email@email.com" required>
	<button type="submit">Submit Form</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./style/style.css")
 


 