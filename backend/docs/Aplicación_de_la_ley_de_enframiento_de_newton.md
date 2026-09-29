Aplicaci´on de la ley de enframiento de newton 

November 2025 

# **1 Ley de Enframiento** 

Hay una baso de agua muy caliente, al pasar una hora el baso con agua tiene casi la temperatura del ambiente. Este comportamiento de los objetos y sustancias se conoce como Ley de Enfriamiento de Newton. Estos fen´omenos f´ısicos que vivenciamos todos los d´ıas los podemos traducir al lenguaje matem´atico, que nos ayuda a comprender y predecir. 

La primera observaci´on: el decaimiento de la temperatura del baso con agua tiene una dependencia del tiempo, al pasar m´as tiempo m´as fr´ıo esta. De tal forma, la funci´on que relaciona el comportamiento de la temperatura depende necesariamente del tiempo, se definir´a como _T_ ( _t_ ), La segunda observaci´on: La temperatura del baso con agua no va sobre pasar la temperatura ambiental, la cual ser´a denotada por _Tm_ . De esto, se concluye que _T <_ ( _t_ ) _≤ Tm_ , para todo _t ≥_ 0. Adem´as, si la temperatura ambiental es igual en toda la hora de la medici´on de los datos, el comportamiento de la curva que describe el tiempo _t_ vs la temperatura _T_ , es un decaimiento continuo hasta llegar al valor de _Tm_ , (si _ti > ti_ +1, entonces _T_ ( _ti_ ) _> T_ ( _ti_ +1)) (ver figura 1), no hay posibilidad que la temperatura del baso con agua suba de alguna forma. La pregunta que nos debemos hacer ¿Cu´al es el tipo de curva o m´as bien el tipo de funci´on _T_ ( _t_ ) que describir´ıa el enfriamiento del baso con agua? ser´ıa una funci´on polin´omica, fraccionaria, o exponencial. ¿Como a partir de lo anterior se pueda construir una ecuaci´on que describa el fen´omeno? Para responder a estas preguntas los sentidos no son suficientes. Es hora de hacer un experimento simulado. 



<!-- Start of picture text -->
Figura 1:<br>Tiempo¢ vs Temperatura T<br><!-- End of picture text -->

1 

# **2 Experimento simulado** 

Se tomar´a un term´ometro y se mide la temperatura de la taza de caf´e en intervalos de 3 minutos, para obtener la tabla 1 y la gr´afica 2, con una temperatura de ambiental _Tm_ = 24. Como se observa en tabla 1 la temperatura baja decrecientemente a 36,6 grados celsius. Se observa que la variaci´on de la temperatura frente al tiempo<sup>_dT_</sup> _dt_<sup><u>(</u></sup><sup>_t_</sup><sup><u>)</u></sup> _≈_<sup>_T_</sup><sup><u>(</u></sup><sup>_ti_</sup><sup><u>+1</u></sup> ∆<sup>_−_</sup> _t_<sup>_T_</sup><sup><u>(</u></sup><sup>_ti_</sup><sup><u>))</u></sup> y la resta de la temperatura _T_ ( _ti_ ) y la temperatura ambiente _Tm_ , se acerca a cero. Por ende, se puede ver que al final la raz´on entre las dos cantidades no varia demasiado, experimentalmente se puede “decir” que se encontr´o una constante de proporcionalidad. Se puede expresar el enfriamiento del baso con agua, con la siguiente ecuaci´on diferencial 

## _drdt_<sup>=</sup><sup>_k_(</sup><sup>_T−Tm_)(1)</sup> 

donde el valor _k_ representa la constante de proporcionalidad entre la dos expresiones<sup>_<u>dT</u>_</sup> _dt_<sup>y</sup><sup>_T−Tm_,yexperimentalmenteseencuentracomoelpromedio</sup> de la raz´on de los valores de la tabla 1, para este caso en especıfico. 



<!-- Start of picture text -->
DatosRl Tiempof@ Temperature  AT/At BA Tti)-TtmBd (O7/0t)/(1(ti)-tolka<br>0 0 80 -2,6667 50 -0,0533<br>1 3 72 -1,3333 42 -0,0317<br>2 6 68 -1,6667 38 -0,0439<br>3 9 63 -1,0000 33 -0,0303<br>4 12 60 -1,0000 30 -0,0333<br>5 15 57 -1,0000 27 -0,0370<br>6 18 54 -0,6667 24 -0,0278<br>7 21 52 -0,6667 22 -0,0303<br>8 24 50 -0,6667 20 -0,0333<br>9 27 48 -0,6000 18 -0,0333<br>[10 30 46,2 -0,4000 16,2 -0,0247<br>1 33 45 -0,3333 15 -0,0222<br>12 36 44 -0,6667 14 -0,0476<br>13 39 42 -0,3333 12 -0,0278<br>14 42 41 -0,3333 1 -0,0303<br>15 45 40 -0,3333 10 -0,0333<br>16 48 39 -0,3333 9 -0,0370<br>7 51 38 -0,1667 8 -0,0208<br>18 54 37.5 -0,1667 75 -0,0222<br>19 57 37 -0,1333 7 -0,0190<br>20 60 36,6 Promedio -0,0320<br><!-- End of picture text -->

Tabla 1: Temperatura _T_ vs Tiempo _t_ 

2 



<!-- Start of picture text -->
Grafica Temperatura vs tiempo<br>90<br>80 @<br>70 e °<br>e<br>60 e 6<br>50 fe f @ cee<br>40 eee e eeee<br>30<br>0 10 20 30 40 50 60<br><!-- End of picture text -->

De la ecuaci´on (1), obtenemos la soluci´on 

_T_ ( _t_ ) = ( _T_ 0 _− Tm_ ) _e_<sup>_kt_</sup> + _Tm_ 

Aplicando los valores del experimento simulado _T_ 0 = 80, _Tm_ = 30, _k_ = _−_ 0 _,_ 032, se obtiene la siguiente funci´on 



La siguiente gr´afica compara los datos experimentales con los datos teoricos arrojados por la ecuaci´on diferecial. 



<!-- Start of picture text -->
Grafico experimental vs tedrico<br>90<br>80<br>© 70<br>&<br>o 60<br>a<br>—<br>2 50<br>40<br>30<br>0 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60<br>tiempo<br>— Datos tedricos +9 —®=Datos experimentales<br><!-- End of picture text -->

3 

# **3 Concluciones** 

1. A medida que transcurre el tiempo, la temperatura de un objeto caliente, como un vaso con agua, desciende gradualmente hasta acercarse a la temperatura ambiental sin superarla. Este comportamiento puede representarse matem´aticamente para predecir el enfriamiento. 

2. Experimentalmente, se determin´o una constante de proporcionalidad que permite expresar el enfriamiento mediante una ecuaci´on diferencial, donde la variaci´on de la temperatura en funci´on del tiempo es proporcional a la diferencia entre la temperatura del objeto y la ambiental. 

3. Utilizando los valores experimentales y la constante de proporcionalidad, se obtuvo una funci´on exponencial que describe con precisi´on el enfriamiento. Esta funci´on se ajusta bien a los datos experimentales, validando el modelo te´orico y confirmando la efectividad de la Ley de Enfriamiento de Newton en predecir la temperatura de un objeto con el tiempo. 

4 

