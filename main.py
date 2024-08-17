import streamlit as st
from content import lang_dict, content

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
<style>.element-container:has(#button-after) + div button {
justify-content: left;
font-size: 20px;
 }</style>""", unsafe_allow_html=True)

st.markdown("""
<style>
	.stLinkButton a {
		background-color: #e3f4ef;
		font-weight: bold;
		color: black;
		width: 100%;
		height: 50px;
		border: 0px;
	}

	.stLinkButton a:hover {
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


###############
#
# SESSION STATE VARIABLES
#
###############

if "current_page" not in st.session_state.keys():
		st.session_state.current_page = "Welcome"

if "language" not in st.session_state.keys():
		st.session_state.language = "NL"


###############
#
# HEADER
#
###############

def change_language():
	st.session_state.language = lang_dict[st.session_state.new_language]

col1, col2 = st.columns([0.85,0.15])
with col2:
	lang = st.selectbox(
		"",
		(lang_dict.keys()),
		index=0,
		key="new_language",
		on_change=change_language,
	)



###############
#
# NAVIGATION SIDEBAR
#
###############

def change_page(page):
	st.session_state.current_page = page


with st.sidebar:
	st.title(content.get(f"sidebar_title_{st.session_state.language}"))
	st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
	st.button(content.get(f"sidebar_button_welcome_{st.session_state.language}"),key="welcome", on_click=change_page, args=('Welcome',))
	st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
	st.button(content.get(f"sidebar_button_request_{st.session_state.language}"),key="request", on_click=change_page, args=('Request',))
	st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
	st.button(content.get(f"sidebar_button_faq_{st.session_state.language}"),key="faq", on_click=change_page, args=('FAQ',))
	st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
	st.button(content.get(f"sidebar_button_examples_{st.session_state.language}"), on_click=change_page, args=('Examples',))
	st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
	st.button(content.get(f"sidebar_button_support_{st.session_state.language}"),key="support", on_click=change_page, args=('Support',))


###############
#
# WELCOME
#
###############



if st.session_state.current_page == "Welcome":

	st.markdown("# AI Bedtime Stories")

	col1, col2 = st.columns([0.13,0.87])

	with col1:
		st.image("img/Logo-removebg.png")

	with col2:
		#"## Gepersonaliseerde verhaaltjes voor het slapen gaan."
		print(f"subtitle_welcome_{st.session_state.language}")
		st.markdown(content.get(f"subtitle_welcome_{st.session_state.language}"), help=content.get(f"subtitle_welcome_help_{st.session_state.language}"))

		st.button(content.get(f"welcome_request_from_welcome_top_{st.session_state.language}"),key="request_from_welcome_top", on_click=change_page, args=('Request',), type="primary")

	st.divider() 

	st.markdown(content.get(f"welcome_intro_{st.session_state.language}"))

	st.markdown(content.get(f"welcome_how_does_it_work_{st.session_state.language}"))

	st.info(content.get(f"welcome_info_disclaimer_{st.session_state.language}"), icon="ℹ️")

	col1, col2, col3 = st.columns(3)

	with col1:
		st.button(content.get(f"welcome_request_from_welcome_{st.session_state.language}"), key="request_from_welcome", on_click=change_page, args=('Request',))

	with col2:
		st.button(content.get(f"welcome_faq_from_welcome_{st.session_state.language}"), key="faq_from_welcome", on_click=change_page, args=('FAQ',))

	with col3:
		st.button(content.get(f"welcome_examples_from_welcome_{st.session_state.language}"), key="examples_from_welcome", on_click=change_page, args=('Examples',))

	st.markdown(content.get(f"welcome_expectation_details_{st.session_state.language}"))

	col1, col2 = st.columns(2)

	with col1:
		st.markdown(content.get(f"welcome_automated_free_{st.session_state.language}"), unsafe_allow_html=True)
		st.image(f"img/raw_story_{st.session_state.language}.jpg")

	with col2:
		st.markdown(content.get(f"welcome_request_paid_{st.session_state.language}"), unsafe_allow_html=True)
		st.image(f"img/formatted_story_{st.session_state.language}.jpg")

	st.markdown(content.get(f"welcome_support_heading_{st.session_state.language}"))
	st.button(content.get(f"welcome_support_from_welcome_{st.session_state.language}"), key="support_from_welcome", on_click=change_page, args=('Support',))





###############
#
# REQUEST
#
###############

elif st.session_state.current_page == "Request":

	st.markdown(content.get(f"request_title_{st.session_state.language}"))

	st.info(content.get(f"request_info_{st.session_state.language}"), icon="ℹ️")

	st.divider()
	
	if st.session_state.language =="NL":
		contact_form = """
		<form action="https://api.web3forms.com/submit" method="POST">
			<!-- Replace with your Access Key -->
			<input type="hidden" name="access_key" value="69c64411-1307-4e08-b9cd-fdf76f46d456">
			<!-- Form Inputs. Each input must have a name="" attribute -->
			<label for="Name of main character"><font style="font-size:15pt;">Wat is de <font color="#26b29d"><b>naam</b></font> van het hoofdpersonage?</font></label><br>
			<input type="text" name="Name of main character" placeholder="bvb. Emma, Lily, Arthur, ..." required>
			<label for="Characteristics of main character"><font style="font-size:15pt;">Wat zijn specifieke <font color="#26b29d"><b>kenmerken</b></font> van het hoofdpersonage? Denk aan haarkleur, geslacht, leeftijd, favoriete kledij, ...</font></label><br>
			<input type="text" name="Characteristics of main character" placeholder="bvb. 3-jarig blond meisje dat graag een roze jurk draagt." required>
			<label for="Elements of the story"><font style="font-size:15pt;">Welke <font color="#26b29d"><b>elementen</b></font> moeten er zeker voorkomen in het verhaal? Denk aan een broertje/zusje, huisdier, een specifieke locatie of gebeurtenis, iets dat je je kind probeert aan te leren, ... </font></label><br>
			<input type="text" name="Elements of the story" placeholder="bvb. Ze speelt graag op het strand met haar hondje Flappy (een bruine golden retriever), maar is soms een beetje wild." required>
			<label for="language"><font style="font-size:15pt;">In welke <font color="#26b29d"><b>taal</b></font> zou je het verhaaltje graag lezen?</font></label><br>
			<input type="text" name="language" placeholder="Nederlands" required>
			<label for="email"><font style="font-size:15pt;">Naar welk <font color="#26b29d"><b>email adres</b></font> moeten we het verhaal opsturen?</font></label><br>
			<input type="email" name="email" placeholder="email@email.com" required>
			<button type="submit"><font style="font-size:15pt;">Submit Form</font></button>
		</form>
		"""
	
	elif st.session_state.language =="EN":
		contact_form = """
		<form action="https://api.web3forms.com/submit" method="POST">
			<!-- Replace with your Access Key -->
			<input type="hidden" name="access_key" value="69c64411-1307-4e08-b9cd-fdf76f46d456">
			<!-- Form Inputs. Each input must have a name="" attribute -->
			<label for="Name of main character"><font style="font-size:15pt;">What is the <font color="#26b29d"><b>name</b></font> of the main character?</font></label><br>
			<input type="text" name="Name of main character" placeholder="ex. Emma, Lily, Arthur, ..." required>
			<label for="Characteristics of main character"><font style="font-size:15pt;">What are some of the most profound <font color="#26b29d"><b>characteristics</b></font> of the main character? Think about hair color, gender, age, favorite clothing, ...</font></label><br>
			<input type="text" name="Characteristics of main character" placeholder="ex. 3 year old blonde girl that likes to wear a pink dress." required>
			<label for="Elements of the story"><font style="font-size:15pt;">Which <font color="#26b29d"><b>elements</b></font> have to appear in the story? This about a brother/sister, a pet, a specific location or event, something you are trying to teach your child, ... </font></label><br>
			<input type="text" name="Elements of the story" placeholder="ex. She likes to play on the beach with het dog Flappy (a brown golden retriever), but she plays a bit rough sometimes." required>
			<label for="language"><font style="font-size:15pt;">In what <font color="#26b29d"><b>language</b></font> would you like to read the story?</font></label><br>
			<input type="text" name="language" placeholder="English" required>
			<label for="email"><font style="font-size:15pt;">To which <font color="#26b29d"><b>email address</b></font> do you want us to send the story?</font></label><br>
			<input type="email" name="email" placeholder="email@email.com" required>
			<button type="submit"><font style="font-size:15pt;">Submit Form</font></button>
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

	st.title(content.get(f"faq_title_{st.session_state.language}"))

	with st.expander(content.get(f"faq_expander1_title_{st.session_state.language}")):
		st.markdown(content.get(f"faq_expander1_content_{st.session_state.language}"))

	with st.expander(content.get(f"faq_expander2_title_{st.session_state.language}")):
		st.markdown(content.get(f"faq_expander2_content_{st.session_state.language}"))

	with st.expander(content.get(f"faq_expander3_title_{st.session_state.language}")):
		st.markdown(content.get(f"faq_expander3_content_{st.session_state.language}"))
		st.image("img/Success.png")

###############
#
# Examples
#
###############

if st.session_state.current_page == "Examples":

	st.title(content.get(f"examples_title_{st.session_state.language}"))

	st.markdown(content.get(f"examples_input_header_{st.session_state.language}"))

	st.markdown(content.get(f"examples_input_table_{st.session_state.language}"))

	st.divider()

	st.markdown(content.get(f"examples_result_header_{st.session_state.language}"))

	col1, col2 = st.columns([0.3, 0.7])

	with col1:
		st.markdown(content.get(f"examples_result_subheader_{st.session_state.language}"))
		st.image("img/Image1.png")

	with col2:
		st.markdown(content.get(f"examples_result_story_{st.session_state.language}"))

	st.markdown(content.get(f"examples_formatted_version_header_{st.session_state.language}"))

	col1, col2 = st.columns([0.6, 0.4])
	with col1:
		st.markdown(content.get(f"examples_formatted_version_description_{st.session_state.language}"))

	with col2:
		st.image(f"img/formatted_story_{st.session_state.language}.jpg")

###############
#
# Support
#
###############

if st.session_state.current_page == "Support":

	st.markdown(content.get(f"support_title_{st.session_state.language}"))

	st.markdown(content.get(f"support_description_{st.session_state.language}"))

	col1, col2 = st.columns([0.3, 0.7])
	with col1:
		st.link_button(content.get(f"support_donate_button_{st.session_state.language}"), "https://www.paypal.com/donate/?hosted_button_id=U6D6FC5LSCPWY")
		st.image("img/qr.png", caption=content.get(f"support_qr_caption_{st.session_state.language}"), use_column_width="always")