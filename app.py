import streamlit as st
from pag1 import main as  pag1
from pag2 import main as  pag2
from pag3 import main as  pag3
from pag4 import main as  pag4
from pag5_business_plan import main as  pag5_business_plan
from pag5 import main as  pag5
from pag6 import main as  pag6
#from pagxx import main as pagxx


def main():
		
	pag_name = ["Introduzione","Avvio dell'app","Dati raccolti","Analisi Covid", "Ipotesi di Business plan", "Implementazione su Raspberry", "Conclusioni"]
	
	OPTIONS = pag_name

	sim_selection = st.sidebar.selectbox("Seleziona la pagina", OPTIONS)

	if sim_selection == pag_name[0]:
		pag1()
	elif sim_selection == pag_name[1]:
		pag2()
	elif sim_selection == pag_name[2]:
		pag3()
	elif sim_selection == pag_name[3]:
		pag4()
	elif sim_selection == pag_name[4]:
		pag5_business_plan()
	elif sim_selection == pag_name[5]:
		pag5()
	elif sim_selection == pag_name[6]:
		pag6()
	else:
		st.markdown("Something went wrong. We are looking into it.")



if __name__ == '__main__':
	main()