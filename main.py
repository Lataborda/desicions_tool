import streamlit as st
from PIL import Image


image = Image.open('Logos3.png')
st.image(image)



#Titulo
st.write("""
# Herramienta para un análisis económico de la producción de yuca y chips secos de yuca

Esta herramienta permite analizar la rentabilidad de la producción de raíces y chips secos de yuca. Con esta herramienta, se podrá realizar interacciones con diferentes variables de la producción tales como: costos de producción, rendimientos, precios de venta en función a parámetros de calidad materia seca, y otros. Mediante este análisis, un productor de yuca podrá examinar su sistema de producción y/o transformación, a fin de tomar decisiones que maximicen la rentabilidad de sus operaciones.  
""")

Menubar = st.selectbox('Seleccione el sistema de producción de su interes:', options=['Producción de raíces frescas de yuca','Producción de chips secos de yuca'], index=0)

header = st.container() 

if Menubar == 'Producción de raíces frescas de yuca':
	st.subheader('Por favor indique los costos de producción por hectárea para cada una de las siguientes categorías de gastos generales:')
	
	st.subheader('***Gastos generales por hectárea:***')

	#insumos y costos generales
	
	Alq = st.number_input('Alquiler de una (1) hectárea "civilizada" o "sin civilizar" ($):',0,5000000)

	Ara = st.number_input('Preparación de la tierra: Costos de arado, pase de rastra, caballoneo, u otro si aplica ($):', 0,5000000)

	Sem = st.number_input('Semilla de yuca industrial para una hectárea, ($):', 0,5000000)

	Ins = st.number_input('Insumos (fertilizantes, biocontroladores, plaguicidas, otros), ($):', 0,5000000)

	#Mano de obra

	st.subheader('***Mano de obra (costos por hectárea):***')
	
	cj = st.number_input('Costo de un jornal ($):', 0,200000)

	js = st.number_input('Cantidad de jornales para la siembra (por hectárea):', 0,200)

	jo = st.number_input('Cantidad de jornales para las aplicaciones y otras labores de campo(por hectárea):', 0,200)
	
	jc = st.number_input('Cantidad de jornales para la cosecha(por hectárea):', 0,200)

	#Costos totales producción por hectárea

	st.subheader('**Costos totales de producción por hectárea:**')
	Tot= (Alq + Ara + Sem + Ins + (cj * js) + (cj * jo) + (cj * jc))

	st.info(f"**Costos totales por hectárea: ${Tot:,}**")

	# Rendimiento en Ton/ha
	st.markdown('***Por favor indique la cantidad promedio de toneladas de yuca cosechadas por hectárea:***')

	my_range8 = range(5,36)
	re = st.select_slider('Rendimiento de cosecha (ton/ha):', options=my_range8, value=17)

	CPT = int(Tot)/ int(re)

	st.subheader('**Costos totales de producción por tonelada:**')
	st.info(f"**Costos totales por tonelada de yuca: ${round(CPT,1)}**")

	#transporte 
	st.subheader('***Costos de transporte por tonelada de yuca:***')

	
	tp = st.number_input('Costos de transporte de 1 tonelada de raíces frescas (puesta en planta), ($):', 0,5000000)

	
	ot = st.number_input('Otros costos por transporte de racies (transporte desde el cultivo hasta el camión, cargue, descargue, empaque, otros) por tonelada de yuca (en miles de pesos $):', 0,5000000)

	tt= (int(tp) + int(ot))
	st.info(f"**Costos totales de transporte por tonelada de yuca: ${tt:,}**")

	#transporte + producción

	st.subheader('**Costos totales de producción + costos de transporte por tonelada de yuca:**')
	tc = int(tt) + int(CPT)

	st.info(f"**Costos totales de producción + transporte de raices de yuca: ${tc:,}**")

	#precio de venta 
	st.subheader('Por favor indique el precio de venta (referencia) de raíces por tonelada:')

	pr = st.number_input('Precio de venta de racies/Ton ($):', 0,3000000)

	#rentabilidad bruta

	rb = (int(pr)) - int(tc)
	rbh= int(rb)* int(re)
	
	if float(rbh)<1000000:
		st.error(f"**Rentabilidad bruta en la venta de una tonelada de raices frescas: ${rb:,}**")

	elif 1000000.01 <= float(rbh) <= 1500000:
		st.warning(f"**Rentabilidad bruta en la venta de una tonelada de raíces frescas: ${rb:,}**")

	elif float(rbh)>= 1500001:
		st.success(f"**Rentabilidad bruta en la venta de una tonelada de raíces frescas: ${rb:,}**")

	
	if float(rbh)<1000000:
		st.error(f"**Rentabilidad bruta total por hectárea: ${rbh:,}**")

	elif 1000000.01 <= float(rbh) <= 1500000:
		st.warning(f"**Rentabilidad bruta total por hectárea: ${rbh:,}**")

	elif float(rbh)>= 1500001:
		st.success(f"**Rentabilidad bruta total por hectárea: ${rbh:,}**")


	st.write('**Nota**: *La utilidad bruta* de una empresa es la ganancia que se obtiene de la venta de un producto luego de restarle los costos asociados a su producción. Por otra parte, a fin de determinar la *utilidad neta* es necesario considerar otros costos fijos, operativos y de inversión.')

elif Menubar == 'Producción de chips secos de yuca':

	st.subheader('Por favor indique los costos de producción para cada una de las siguientes categorías de gastos generales:')
	
	cry = st.number_input('Costos de producción (o compra) de una (1) tonelada de raíces frescas ($)',0,5000000)
	
	tpr = st.number_input('Costos de transporte de una (1) tonelada de raíces frescas hasta el patio de secado ($):', 0,5000000)
	
	ratio = st.slider('Cantidad de toneladas de racies frescas para obtener una (1) tonelada de chips secos:', min_value=1.8, max_value=6.6, value=2.5, step=0.1)
	cs = st.number_input('Costos de secado (mano de obra y energía) de una (1) tonelada de chips secos de yuca ($):', 0,5000000)
	
	thp = st.number_input('Costos de transporte de una (1) tonelada de chips secos hasta la industria ($):', 0,5000000)
	
	#costos totales de producir una tonelada de chips secos 
	
	ctch= (int(cry) * float(ratio)) + (int(tpr) * float(ratio)) + int(cs) + int (thp)

	st.info(f"**Costos totales de producción y transporte de una (1) tonelada chips secos de yuca: ${ctch:,}**")

	st.subheader('Por favor indique el precio de venta (referencia) de una (1) tonelada de chips secos de yuca:')

	pch = st.number_input('Precio de venta de una (1) tonelada de chips secos de yuca ($):', 0,3000000)
	
	#rentabilidad bruta chips
	
	rch = int(pch) - int(ctch)
	
	if float(pch)<(int(ctch)*1.1):
		st.error(f"**Rentabilidad bruta en la venta de una tonelada de chips secos: ${rch:,}**")

	elif (int(ctch)*1.1) <= float(pch) <= (int(ctch)*1.20):
		st.warning(f"**Rentabilidad bruta en la venta de una tonelada de chips secos: ${rch:,}**")

	elif float(pch)>= (int(ctch)*1.21):
		st.success(f"**Rentabilidad bruta en la venta de una tonelada de chips secos: ${rch:,}**")

	st.write('**Nota**: *La utilidad bruta* de una empresa es la ganancia que se obtiene de la venta de un producto luego de restarle los costos asociados a su producción. Por otra parte, a fin de determinar la *utilidad neta* es necesario considerar otros costos fijos, operativos y de inversión.')
	
st.markdown('**Agradecimientos por suministrar información y orientación: Angela Vasquez (AGROSAVIA), Juan Carlos Martinez (Agrosavia), Alberto Garcia (CLAYUCA), Bernardo Ospina (CLAYUCA)**')	
st.markdown('*Copyright (C) 2022 AGROSAVIA, CIRAD & CIAT*')
st.markdown('**Autores: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Katia Contreras (kcontreras@agrosavia.co), Shirley Perez (AGROSAVIA), Thierry Tran (thierry.tran@cirad.fr)**')

	
	







	


