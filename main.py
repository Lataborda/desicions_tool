import streamlit as st
from PIL import Image


image = Image.open('Logos3.png')
st.image(image)



#Titulo
st.write("""
# Herramienta para un análisis económico de la producción de yuca y chips secos de yuca

Esta herramienta permite analizar la rentabilidad de la producción de raíces y chips secos de yuca. Con esta herramienta, se podrá realizar interacciones con diferentes variables de la producción tales como: costos de producción, rendimientos, precios de venta en función a parámetros de calidad materia seca, y otros. Mediante este análisis, un productor de yuca podrá examinar su sistema de producción y/o transformación, a fin de tomar decisiones que maximicen la rentabilidad de sus operaciones.  
""")

Menubar = st.selectbox('Seleccione el sistema de producción de su interes:', options=['Producción de raíces frescas de yuca','Producción de raíces y chips secos de yuca','Producción de chips secos de yuca'], index=0)

header = st.container() 

if Menubar == 'Producción de raíces frescas de yuca':
	st.subheader('Por favor indique los costos de producción por hectárea para cada una de las siguientes categorías de gastos generales:')
	
	st.subheader('***Gastos generales por hectárea:***')

	#insumos y costos generales
	
	Alq = st.number_input('Alquiler de una (1) hectárea "civilizada" o "sin civilizar" ($)',0,5000000)

	Ara = st.number_input('Preparación de la tierra: Costos de arado, pase de rastra, caballoneo, u otro si aplica ($)', 0,5000000)

	Sem = st.number_input('Semilla de yuca industrial para una hectárea, ($)', 0,5000000)

	Ins = st.number_input('Insumos (fertilizantes, biocontroladores, plaguicidas, otros), ($)', 0,5000000)

	#Mano de obra

	st.subheader('***Mano de obra (costos por hectárea):***')
	
	ms = st.number_input('Siembra ($)', 0,5000000)

	ma = st.number_input('Aplicaciones: fertilización, aplicaciones de Control, otras...($)', 0,5000000)

	mc = st.number_input('Cosecha ($)', 0,5000000)

	#Costos totales producción por hectárea

	st.subheader('**Costos totales de producción por hectárea:**')
	Tot= (Alq + Ara + Sem + Ins + ms + ma + mc)

	st.info(f"**Costos totales por hectárea: ${Tot:,}**")

	# Rendimiento en Ton/ha
	st.markdown('***Por favor indique la cantidad promedio de toneladas de yuca cosechadas por hectárea:***')

	my_range8 = range(5,36)
	re = st.select_slider('Rendimiento de cosecha (ton/ha):', options=my_range8, value=17)

	CPT = int(Tot)/ int(re)

	st.subheader('**Costos totales de producción por tonelada:**')
	st.info(f"**Costos totales por tonelada de yuca: ${CPT:,}**")

	#transporte 
	st.subheader('***Costos de transporte por tonelada de yuca:***')

	
	tp = st.number_input('Costos de transporte de 1 tonelada de raíces frescas (puesta en planta), ($):', 0,5000000)

	
	ot = st.number_input('Otros costos por transporte de racies (transporte desde el cultivo hasta el camion, cargue, descargue, empaque, otros) por tonelada de yuca (en miles de pesos $):', 0,5000000)

	tt= (int(tp) + int(ot))
	st.info(f"**Costos totales de transporte por tonelada de yuca: ${tt:,}**")

	#transporte + producción

	st.subheader('**Costos totales de producción + costos de transporte por tonelada de yuca:**')
	tc = int(tt) + int(CPT)

	st.info(f"**Costos totales de producción + transporte de raices de yuca: ${round(tc:,),1}**")

	#precio de venta 
	st.subheader('Por favor indique el precio de venta (referencia) de raices por tonelada:')

	pr = st.number_input('Precio de venta de racies/Ton ($):', 0,3000000)

	#rentabilidad bruta

	rb = (int(pr)) - int(tc)
	st.success(f"**Rentabilidad bruta en la venta de una tonelada de raices frescas: ${rb:,}**")

	rbh= int(rb)* int(re)
	st.success(f"**Rentabilidad bruta total por hectárea: ${rbh:,}**")

	st.write('**Nota**: *La utilidad bruta* de una empresa es la ganancia que se obtiene de la venta de un producto luego de restarle los costos asociados a su producción. Por otra parte, a fin de determinar la *utilidad neta* es necesario considerar otros costos fijos, operativos y de inversión.')

elif Menubar == 'Producción de raíces y chips secos de yuca':

	st.subheader('Por favor indique los costos de producción por hectárea para cada una de las siguientes categorías de gastos generales:')
	st.subheader('***Gastos generales por hectárea:***')

	#insumos y costos generales

	my_range1b = range(0,951)
	Alqb = st.select_slider('Alquiler de una (1) hectárea "civilizada" o "sin civilizar" (en miles de pesos $)', options=my_range1b, value=750)

	my_range2b = range(0,651)
	Arab = st.select_slider('Preparación de la tierra: Costos de arado, pase de rastra, caballoneo, u otro si aplica (en miles de pesos $)', options=my_range2b, value=450)

	my_range3b = range(0,501)
	Semb = st.select_slider('Semilla de yuca industrial para una hectárea, (en miles de pesos $)', options=my_range3b, value=80)

	my_range4b = range(0,701)
	Insb = st.select_slider('Insumos (fertilizantes, biocontroladores, plaguicidas, otros), (en miles de pesos $)', options=my_range4b, value=450)

	#Mano de obra

	st.subheader('***Mano de obra labores de campo (por hectárea):***')
	
	my_range5b = range(0,801)
	msb = st.select_slider('Siembra (en miles de pesos $)', options=my_range5b, value=400)

	my_range6b = range(0,801)
	mab = st.select_slider('Aplicaciones: fertilización, aplicaciones de Control, otras...(en miles de pesos $)', options=my_range6b, value=350)

	my_range7b = range(0,801)
	mcb = st.select_slider('Cosecha (en miles de pesos $)', options=my_range7b, value=600)

	#Costos totales producción por hectárea

	st.subheader('**Costos totales de producción por hectárea:**')
	Totb= (Alqb + Arab + Semb + Insb + msb + mab + mcb)*1000

	st.error(f"**Costos totales por hectárea: ${round(Totb,1)}**")

	# Rendimiento en Ton/ha
	st.markdown('***Por favor indique la cantidad promedio de toneladas de yuca cosechadas por hectárea:***')

	my_range8b = range(5,35)
	reb = st.select_slider('Rendimiento de cosecha (ton/ha):', options=my_range8b, value=17)

	#costos totales de producción/ton raices
	CPTb = int(Totb)/ int(reb)

	st.subheader('**Costos totales de producción por tonelada de raíces:**')
	st.error(f"**Costos totales por tonelada de yuca: ${round(CPTb,1)}**")

	#transporte 

	st.subheader('***Costos de transporte por tonelada de raíces frescas de yuca:***')

	my_range9b = range(0,201)
	tpb = st.select_slider('Costos de transporte de una (1) tonelada de racíces frescas hasta el patio de secado (en miles de pesos $):', options=my_range9b, value=80)

	##Costos de secado
	st.subheader('***Costos de secado:***')

	my_range10b = range(100,10001)
	areb = st.select_slider('Área disponible para el secado de chips (en mt2)', options=my_range10b, value=2700)

	st.write('**Nota**: *Para un secado adecuado se recomienda esparcir hasta 10 kg de chips por cada metro cuadrado (mt2).*')

	vol_ab = (int(areb)*10)/1000

	#capacidad de secado
	st.write(f"**-Teniendo el anterior argumento como referencia, la cantidad aproximada de toneladas de raices que podrá secar en su patio en cada batch es: {round(vol_ab,1)}ton**")

	#cantidad de ha a cosechar par 1 batch
	hacob = float(vol_ab) / float(reb)

	st.write(f"**-De acuerdo con el rendimiento de producción reportado anteriormente (ton/ha), la cantidad de hectáreas de yuca que debería cosechar para secar un (1) batch de raíces en su patio es: {round(hacob,1)}ha**")

	#No de días de secado/batch
	my_range12b = range(0,12)
	nds = st.select_slider('Número de días que requiere en promedio para secar un batch', options=my_range12b, value=3)

	#costo de 1 dia de secado
	my_range11b = range(0,150)
	c1d = st.select_slider('Costo de 1 día de secado por mano de obra (dependerá del costo de un jornal y del número de personas empleadas para picar y secar/día) (en miles de pesos)', options=my_range11b, value=60)

	#costo de secado por batch
	csbb = (int(c1d) * int(nds))*1000
	st.write(f"**-El costo de secar 1 batch en su patio es: ${round(csbb,1)}**")

	#ratio conversión
	my_range13b = range(1500,5001)
	ratiob = st.select_slider('Cantidad de kilos (Kg) de raices de yuca fresca para obtener 1000 Kg (1ton) de chips secos de yuca', options=my_range13b, value=2500)

	#Ton chips a producir por batch
	tch_b = float(vol_ab)/(float(ratiob)/1000)
	st.write(f"**-La cantidad de chips secos a producir en un batch es: {round(tch_b,1)}ton**")

	#costo de secado de 1 ton de chips
	cs1tch = float(csbb)/float(tch_b)
	st.error(f"**Costos totales de secado por 1 tonelada de chips: ${round(cs1tch,1)}**")

	#Costos totales 1 ton chips secos por hectárea

	st.subheader('**Costos totales para obtener 1 ton de chips secos:**')
	Tot_chip= (float(CPTb) * (float(ratiob)/1000)) + ((float(tpb)*1000) * (float(ratiob)/1000)) + float(cs1tch)
	st.error(f"**Costos totales producción de 1 ton de chips secos = costo de producción de X Ton de raíces frescas (según ratio de conversión) + transporte de X Ton de raíces frescas (según ratio de conversión) hasta el patio + secado de 1 ton de chips: ${round(Tot_chip,1)}**")

	#precio de venta de los chips secos
	my_range14b = range(850,1601)
	pr_ch = st.select_slider('Precio de venta de 1 Ton de chips secos (en miles de pesos, es decir que al precio se le agregan 3 ceros $):', options=my_range14b, value=1200)

	#rentabilidad bruta ton de chip
	rbchip= (int(pr_ch)*1000) - int(Tot_chip)
	st.success(f"**Rentabilidad bruta total por ton de chips secos vendida: ${round(rbchip,1)}**")

	st.write('**Nota**: *La utilidad bruta* de una empresa es la ganancia que se obtiene de la venta de un producto luego de restarle los costos asociados a su producción. Por otra parte, a fin de determinar la *utilidad neta* es necesario considerar otros costos fijos, operativos y de inversión.')


elif Menubar == 'Producción de chips secos de yuca':
	
	#precio de venta 
	st.subheader('Por favor indique el precio de compra de raices de yuca por tonelada:')

	my_range1c = range(100,701)
	pr3 = st.select_slider('Precio de compra de racies de yuca (en miles de pesos $):', options=my_range1c, value=450)

	#transporte 
	st.subheader('***Costos de transporte por tonelada de raíces frescas de yuca:***')
	my_range9c = range(0,101)
	tpc = st.select_slider('Costos de transporte de una (1) tonelada de racíces frescas hasta el patio de secado (en miles de pesos $):', options=my_range9c, value=30)

	##Costos de secado
	st.subheader('***Costos de secado:***')

	my_range10c = range(100,10001)
	arec = st.select_slider('Área disponible para el secado de chips (en mt2)', options=my_range10c, value=2700)

	st.write('**Nota**: *Para un secado adecuado se recomienda esparcir hasta 10 kg de chips por cada metro cuadrado (mt2).*')

	vol_ac = (int(arec)*10)/1000

	#capacidad de secado
	st.write(f"**-Teniendo el anterior argumento como referencia, la cantidad aproximada de toneladas de raices que podrá secar en su patio en cada batch es: {round(vol_ac,1)}ton**")

	#No de días de secado/batch
	my_range12c = range(0,12)
	ndsc = st.select_slider('Número de días que requiere en promedio para secar un batch', options=my_range12c, value=3)

	#costo de 1 dia de secado
	my_range11c = range(0,150)
	c1dc = st.select_slider('Costo de 1 día de secado por mano de obra (dependerá del costo de un jornal y del número de personas empleadas para picar y secar/día) (en miles de pesos)', options=my_range11c, value=60)

	#costo de secado por batch
	csbc = (int(c1dc) * int(ndsc))*1000
	st.write(f"**-El costo de secar 1 batch en su patio es: ${round(csbc,1)}**")

	#ratio conversión
	my_range13c = range(1500,5001)
	ratioc = st.select_slider('Cantidad de kilos (Kg) de raices de yuca fresca para obtener 1000 Kg (1ton) de chips secos de yuca', options=my_range13c, value=2500)

	#Ton chips a producir por batch
	tch_c = float(vol_ac)/(float(ratioc)/1000)
	st.write(f"**-La cantidad de chips secos a producir en un batch es: {round(tch_c,1)}ton**")

	#costo de secado de 1 ton de chips
	cs1tch3 = float(csbc)/float(tch_c)
	st.error(f"**Costos totales de secado por 1 tonelada de chips: ${round(cs1tch3,1)}**")

	#Costos totales 1 ton chips secos por hectárea

	st.subheader('**Costos totales para obtener 1 ton de chips secos:**')
	Tot_chipc= (((float(pr3)*1000))*(float(ratioc)/1000)) + ((float(tpc)*1000) * (float(ratioc)/1000)) + float(cs1tch3)
	st.error(f"**Costos totales producción de 1 ton de chips secos = costo de compra de X Ton de raíces frescas (según ratio de conversión) + transporte X Ton de raíces frescas (según ratio de conversión) hasta el patio + costos de secado de 1 ton de chips: ${round(Tot_chipc,1)}**")

	#precio de venta de los chips secos
	my_range14b = range(850,1601)
	pr_chc = st.select_slider('Precio de venta de 1 Ton de chips secos (en miles de pesos, $):', options=my_range14b, value=1200)

	#rentabilidad bruta ton de chip
	rbchipc= (int(pr_chc)*1000) - int(Tot_chipc)
	st.success(f"**Rentabilidad bruta total por ton de chips secos vendida: ${round(rbchipc,1)}**")

	st.write('**Nota**: *La utilidad bruta* de una empresa es la ganancia que se obtiene de la venta de un producto luego de restarle los costos asociados a su producción. Por otra parte, a fin de determinar la *utilidad neta* es necesario considerar otros costos fijos, operativos y de inversión.')

st.markdown('**Agradecimientos por suministrar información y orientación: Shirley Perez (AGROSAVIA), Angela Vasquez (AGROSAVIA), Juan Carlos Martinez (Agrosavia), Alberto Garcia (CLAYUCA), Bernardo Ospina (CLAYUCA)**')
st.markdown('*Copyright (C) 2022 AGROSAVIA, CIRAD & CIAT*')
st.markdown('**Autores: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Katia Contreras (kcontreras@agrosavia.co), Thierry Tran (thierry.tran@cirad.fr)**')









	


