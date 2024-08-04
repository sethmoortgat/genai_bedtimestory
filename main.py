import streamlit as st

st.set_page_config(layout="wide")

###############
#
# FORMATTING
#
###############
st.markdown("""
<style>
    .stButton button {
        background-color: #e3f4ef;
        justify-content: left;
        font-weight: bold;
        color: black;
        width: 100%;
        height: 50px;
        border: 0px;
    }

    .stButton button:hover {
        background-color:#42deb1;
        color: white;
    }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #e3f4ef;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<style>.big-font {font-size:20px !important;}</style>', unsafe_allow_html=True)

###############
#
# SESSION STATE VARIABLES
#
###############

if "current_page" not in st.session_state.keys():
		st.session_state.current_page = "Welcome"


###############
#
# NAVIGATION SIDEBAR
#
###############

def change_page_welcome():
	st.session_state.current_page = "Welcome"
	
def change_page_request():
	st.session_state.current_page = "Request"

def change_page_faq():
	st.session_state.current_page = "FAQ"

def change_page_examples():
	st.session_state.current_page = "Examples"

with st.sidebar:
    st.button("Welkom",key="welcome", on_click=change_page_welcome)
    st.button("Maak een verhaaltje",key="request", on_click=change_page_request)
    st.button("FAQ",key="faq", on_click=change_page_faq)
    st.button("Voorbeelden",key="examples", on_click=change_page_examples)

###############
#
# WELCOME
#
###############

if st.session_state.current_page == "Welcome":

	st.title("AI Bedtime Stories")
	st.subheader("Gepersonaliseerde verhaaltjes voor het slapen gaan.")
	
	st.divider() 
	
	st.header("Welkom!")
	st.markdown("""
AI bedtime stories is een geautomatiseerde service die door middel van artificiële intelligentie gepersonaliseerde verhaaltjes en illustraties kan maken. Op basis van de gegevens die jij ingeeft (naam & kenmerken van je kind en andere elementen die je graag in het verhaal wil verwerken), zal een kort verhaaltje met bijpassende illustratie naar jouw e-mail adres gestuurd worden.
	""")
	
	
	
	st.header("Woe werkt het?")
	st.markdown("""
Door hieronder te klikken op "Maak een verhaaltje" wordt je naar een formulier gestuurd waar je enkele vragen dient in te vullen die nodig zijn om het verhaal te personaliseren. Nadat je dit formulier hebt ingediend zal je binnen 24u (mogelijks al een stuk sneller) een e-mail ontvangen waarin je je persoonlijke verhaaltje met bijgevoegde illustratie kan terugvinden. Dat verhaaltje en de foto zijn volledig aan de hand van AI (artificiële intelligentie) gegenereerd.
	""")
	
	st.info("""
	Disclaimer:
	De verhaaltjes en bijgevoegde illustraties worden automatisch via artificiële intelligentie gemaakt, op basis van de input die jij doorgeeft. Wij kunnen nooit verantwoordelijk gehouden worden voor onverwachte of aanstootgevende uitkomsten!
	""",icon="❗")
	
	col1, col2, col3 = st.columns(3)

	with col1:
		st.button("Maak een verhaaltje",key="request_from_welcome", on_click=change_page_request)

	with col2:
		st.button("Frequently Asked Questions",key="faq_from_welcome", on_click=change_page_faq)
	
	with col3:
		st.button("Voorbeelden",key="examples_from_welcome", on_click=change_page_examples)
	
	st.header("Wil je dit initiatief graag steunen?")
	st.markdown("""
	In eerste instantie is het mijn doel om een lach te toveren op de gezichten van jullie kindjes. Vandaar is de service voorlopig helemaal gratis!
	In tweede instantie hoop ik dat ik ook het level van jullie als ouder wat eenvoudiger maak tijdens de avondroutine voor het slapen gaan.
	
	Als dat is gelukt, en je wil dit initiatief graag steunen, dan kan dat op twee manieren:
	  * [Stuur me een e-mail](mailto:seth.moortgat@gmail.com) met je hopelijke leuke ervaring en eventuele constructieve feedback, dat zal een lach op mijn gezicht toveren!
	  * Je kan ook een vrijwillige donatie maken via [deze link](https://www.paypal.com/donate/?hosted_button_id=U6D6FC5LSCPWY) of onderstaande QR code. Dit geld zal ik gebruiken om de kosten te dekken die nodig zijn om dit initiatief te onderhouden. Als er dan nog iets over blijft gaat dat rechtstreeks in het spaarvarkentje van mijn twee dochtertjes.
	""")
	
	st.image("img/qr.png",caption="Doneer door deze QR code te scannen")





###############
#
# SUBMIT
#
###############

elif st.session_state.current_page == "Request":
	
	st.info("""
	Vul onderstaande informatie zo nauwkeurig mogelijk in. Hoe meer details je meegeeft, hoe beter de kwaliteit van het verhaal en de bijhorende illustratie zal zijn.
	""",icon="❗")
	
	contact_form = """
	<form action="https://api.web3forms.com/submit" method="POST">
		<!-- Replace with your Access Key -->
		<input type="hidden" name="access_key" value="69c64411-1307-4e08-b9cd-fdf76f46d456">
		<!-- Form Inputs. Each input must have a name="" attribute -->
		<label for="Name of main character">Wat is de naam van het hoofdpersonage?</label><br>
		<input type="text" name="Name of main character" placeholder="bvb. Emma, Lily, Arthur, ..." required>
		<label for="Characteristics of main character">Wat zijn specifieke kenmerken van het hoofdpersonage? Denk aan haarkleur, geslacht, leeftijd, favoriete kledij, ...</label><br>
		<input type="text" name="Characteristics of main character" placeholder="bvb. 3-jarig blond meisje dat graag een roze jurk draagt." required>
		<label for="Elements of the story">Welke elementen moeten er zeker voorkomen in het verhaal? Denk aan een broertje/zusje, huisdier, een specifieke locatie of gebeurtenis, iets dat je je kind probeert aan te leren, ... </label><br>
		<input type="text" name="Elements of the story" placeholder="bvb. Flappy haar bruin hondje waarmee ze vaak in de tuin speelt." required>
		<label for="language">In welke taal zou je het verhaaltje graag lezen?</label><br>
		<input type="text" name="language" placeholder="Nederlands" required>
		<label for="email">Naar welk email adres moeten we het verhaal opsturen?</label><br>
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
 

###############
#
# FAQ
#
###############
 
if st.session_state.current_page == "FAQ":

	st.title("Frequently Asked Questions")
	
	with st.expander("Ik wacht al meer dan 24u maar heb nog geen email ontvangen?"):
		st.markdown('''
Het spijt me dat je nog geen verhaaltje hebt ontvangen, normaal zou je binnen 24u zeker een email moeten hebben ontvangen. Het automatisch genereren van een verhaal en bijgevoegde illustratie is afhankelijk van verschillende externe services. Er kan altijd iets mis lopen, zowel bij de externe services als ergens anders. Wat je alvast kan proberen is het volgende:
  * Kijk even je spam na
  * Kijk na of je inbox niet vol zit
  * Probeer het gewoon nog een keer, misschien lukt het deze keer wel

Als je toch nog steeds niets ontvangt aarzel dan niet om contact op te nemen door [een e-mail te sturen](mailto:seth.moortgat@gmail.com)!
		''')
	
	with st.expander("Het verhaal en/of de illustratie komen niet goed overeen met mijn beschrijving, hoe komt dat?"):
		st.markdown('''
Helaas hebben we weinig controle over wat de AI algoritmes genereren, en kan het soms gebeuren dat het resultaat (text of beeld) niet helemaal overeen komt met wat je zou verwachten. Het helpt om het formulier met zo veel mogelijk detail in te vullen, dus probeer het gerust nog een keer met een nieuwe, gedetailleerde beschrijving van wat je graag wil zien/horen!
		''')
	
	with st.expander("Hoe weet ik of mijn aanvraag goed verzonden is?"):
		st.markdown('''
Als je onderstaand scherm te zien krijgt weet je dat je aanvraag goed verzonden is. Er kan echter nog altijd iets mislopen in het process waardoor je toch geen email ontvangt binnen de 24u. Als dat zo zou zijn, kijk dan even naar de gerelateerde vraag hierboven.
		''')
		st.image("img/Success.png")

###############
#
# Examples
#
###############
 
if st.session_state.current_page == "Examples":

	st.title("Voorbeelden")
	
	st.markdown("## Input")
	
	st.markdown("""
	| Vraag | Antwoord|
	--------|-------- |
	| Naam | Lily |
	| Kenmerken| 2-jarig meisje met donkerbruin haar en staartje bovenop haar hoofd. Ze draagt een groene t-shirt met een smiley op. |
	| Elementen in het verhaal | Lily gaat graag naar de dierentuin. |
	| Taal | Nederlands |
	
	""")
	
	st.divider() 
	
	st.markdown("## Resultaat")
	
	
	
	col1, col2 = st.columns([0.3, 0.7])

	with col1:
		st.markdown("### Lily bij de Flamingo's")
		st.image("img/Image1.png")

	with col2:
		st.markdown("""
		
Er was eens een klein meisje genaamd Lily. Ze was twee jaar oud, had donkerbruin haar dat in een grappig staartje bovenop haar hoofd stond. Lily droeg altijd haar favoriete groene t-shirt met een grote smiley erop. Ze vond het geweldig om naar de dierentuin te gaan en was altijd vol enthousiasme.

Op een zonnige dag mocht Lily samen met haar ouders naar de zoo. Ze huppelde vrolijk van het ene dierenverblijf naar het andere. Ze bewonderde de olifanten, lachte om de grappige aapjes en zwaaide naar de majestueuze leeuwen.

Toen gebeurde er iets spannends. Terwijl Lily naar de kleurrijke papegaaien keek, liep ze per ongeluk een beetje te ver weg van haar ouders. Plotseling stond ze alleen bij het hek van de flamingo's. Lily keek om zich heen, maar zag haar ouders nergens. Haar hartje begon sneller te kloppen.

Net op dat moment hoorde ze een zachte stem: "Lily, waar ben je?" Het was haar moeder! Met een opgelucht gevoel rende ze naar de stem toe en viel in de warme armen van haar moeder. Haar ouders waren gewoon een paar meter verderop geweest en hadden haar de hele tijd in de gaten gehouden.

Die avond, veilig in haar bedje, droomde Lily over alle prachtige dieren en wist ze dat alles altijd goed zou komen zolang ze dicht bij haar ouders bleef. En met dat geruststellende gevoel, viel ze snel in slaap.

		""")

